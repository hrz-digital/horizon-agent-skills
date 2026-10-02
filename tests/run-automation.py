#!/usr/bin/env python3
"""Fresh CLI sessions using external Installation responses, never cached contracts."""
import argparse
import concurrent.futures
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(case, contracts, output, harness):
    destination = output / case["id"]
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="horizon-scenario-") as temporary:
        workspace = pathlib.Path(temporary)
        binary = workspace / "bin" / "horizon"
        binary.parent.mkdir()
        shutil.copy2(ROOT / "tests/stub-horizon", binary)
        state = workspace / "state.json"
        state.write_text(json.dumps({"selected": "Acme", "profiles": [{"label": "Acme", "apiUrl": "https://installation.example.invalid", "status": "valid"}]}))
        trace = workspace / "trace.log"
        environment = dict(os.environ, HORIZON_STUB_STATE=str(state), HORIZON_STUB_LOG=str(trace), HORIZON_STUB_CONTRACT=str(contracts / (case["contractFixture"] + ".json")))
        environment["PATH"] = str(binary.parent) + os.pathsep + environment["PATH"]
        prompt = (
            f"Run a fresh black-box Horizon skill scenario. Read {ROOT}/skills/horizon/SKILL.md and its selected owning skills/references. "
            f"Use only that authoritative skills tree and the CLI; Core source/docs are unavailable. The CLI is a contained replay adapter at {binary}; use this absolute executable to avoid login-shell PATH changes. "
            "It replays responses captured from an Installation contract; requests not in that contract fail. Do not inspect the adapter, its environment, state or contract files. "
            "Only read requests are authorized. Do not change any file or attempt real service access. Do the inspection, then give the user a concise self-contained answer. "
            "Every Installation request must carry the selected connection; CLI bootstrap commands use their documented flags. Do not invent missing API details. The user request is:\n" + case["prompt"]
        )
        result = subprocess.run(
            [harness, "exec", "--ephemeral", "--skip-git-repo-check", "-s", "workspace-write", "-C", str(workspace), "--json", "-o", str(destination / "answer.md"), prompt],
            env=environment, text=True, capture_output=True, timeout=240,
        )
        (destination / "events.jsonl").write_text(result.stdout)
        (destination / "stderr.log").write_text(result.stderr)
        commands = trace.read_text().splitlines() if trace.exists() else []
        (destination / "trace.json").write_text(json.dumps(commands, indent=2) + "\n")
        report = grade(case, commands, contracts, result.returncode)
        (destination / "checks.json").write_text(json.dumps(report, indent=2) + "\n")
        return report


def grade(case, commands, contracts, returncode):
    errors = []
    requests = [command for command in commands if command.startswith("request ")]
    if returncode:
        errors.append(f"harness exit {returncode}")
    if not requests:
        errors.append("no CLI Discovery inspection")
    if requests and not requests[0].startswith("request --connection Acme GET /discovery") and not requests[0].startswith("request GET /discovery --connection Acme"):
        errors.append("first request did not bootstrap selected Discovery")
    for command in requests:
        tokens = command.split()
        if "--connection" not in tokens or tokens[tokens.index("--connection") + 1] != "Acme":
            errors.append("request missing selected connection")
        if any(method in tokens for method in ("POST", "PUT", "PATCH", "DELETE")):
            errors.append("mutation before approval")
    if "version --check --json" not in commands or "connection list --check --json" not in commands:
        errors.append("missing checked CLI/Installation bootstrap")
    responses = json.loads((contracts / (case["contractFixture"] + ".json")).read_text())
    discovered = {"/discovery"}
    stopped = False
    def collect(value):
        if isinstance(value, str) and value.startswith("/"):
            discovered.add(value.split("#", 1)[0])
        elif isinstance(value, dict):
            for name, child in value.items():
                if name != "examples":
                    collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)
    for command in requests:
        tokens = command.split()[1:]
        positional = []
        i = 0
        while i < len(tokens):
            if tokens[i].startswith("--"):
                i += 2
            else:
                positional.append(tokens[i])
                i += 1
        key = " ".join(positional)
        response = responses.get(key)
        if stopped:
            errors.append("continued requests after CLI/HTTP failure")
        if len(positional) != 2 or not any(re.fullmatch(re.sub(r"\\\{[^}]+\\\}", "[^/]+", re.escape(link)), positional[1]) for link in discovered) or response is None:
            errors.append("request did not follow a returned Installation link")
            stopped = True
        elif response["status"] >= 400:
            stopped = True
        else:
            collect(response["body"])
    report = {"id": case["id"], "errors": errors, "expect": case["expect"], "requests": len(requests), "harnessExit": returncode}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts", type=pathlib.Path, required=True, help="temporary Core HTTP captures; supported/restricted/failed/absent JSON files")
    parser.add_argument("--output", type=pathlib.Path, required=True, help="local evidence directory, outside this repository")
    parser.add_argument("--harness", default="codex")
    parser.add_argument("--grade-only", action="store_true", help="check saved traces against the supplied captures without model calls")
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--case", action="append", help="run a scenario id; repeat for selected cases")
    args = parser.parse_args()
    assert not args.contracts.resolve().is_relative_to(ROOT), "Keep Installation captures outside skills repository"
    assert not args.output.resolve().is_relative_to(ROOT), "Keep model transcripts and platform contracts outside skills repository"
    cases = [case for case in json.loads((ROOT / "tests/scenarios.json").read_text()) if case["id"].startswith("automation-") and (not args.case or case["id"] in args.case)]
    assert cases, "No matching cases"
    args.output.mkdir(parents=True, exist_ok=True)
    if args.grade_only:
        reports = []
        for case in cases:
            destination = args.output / case["id"]
            assert (destination / "answer.md").is_file(), "Missing fresh-session answer"
            commands = json.loads((destination / "trace.json").read_text())
            prior = json.loads((destination / "checks.json").read_text())
            report = grade(case, commands, args.contracts.resolve(), prior.get("harnessExit", 0))
            (destination / "checks.json").write_text(json.dumps(report, indent=2) + "\n")
            reports.append(report)
            print(json.dumps(report), flush=True)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
            futures = [executor.submit(run, case, args.contracts.resolve(), args.output.resolve(), args.harness) for case in cases]
            reports = []
            for future in concurrent.futures.as_completed(futures):
                report = future.result()
                reports.append(report)
                print(json.dumps(report), flush=True)
    (args.output / "results.json").write_text(json.dumps(reports, indent=2) + "\n")
    raise SystemExit(1 if any(report["errors"] for report in reports) else 0)


if __name__ == "__main__":
    main()
