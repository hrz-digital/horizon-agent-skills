#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def require(path, *texts):
    value = (ROOT / path).read_text()
    for text in texts:
        assert text in value, f"{path}: missing {text!r}"


def main():
    require("skills/horizon/SKILL.md", "references/cli-installation.md", "references/connections.md")
    require("skills/horizon/references/connections.md", "horizon connection list --check --json", "--connection")
    for skill in ("horizon-runtime", "horizon-metadata-authoring", "horizon-architecture-analysis"):
        require(f"skills/{skill}/SKILL.md", "Run `horizon` bootstrap")

    scenarios = json.loads((ROOT / "tests/scenarios.json").read_text())
    required = {
        "missing-cli", "unsupported-cli", "install-refused", "zero-profiles", "one-profile", "many-profiles",
        "invalid", "unreachable", "error", "explicit-choice", "explicit-propagation",
        "safe-onboarding", "discovery-workflow", "acceptance-journey",
    }
    assert required == {scenario["id"] for scenario in scenarios}

    stub = ROOT / "tests/stub-horizon"
    for scenario in scenarios:
        if "stub" not in scenario:
            continue
        with tempfile.TemporaryDirectory() as directory:
            state = pathlib.Path(directory) / "state.json"
            state.write_text(json.dumps(scenario["stub"]))
            result = subprocess.run(
                [stub, "connection", "list", "--check", "--json"],
                env={"HORIZON_STUB_STATE": str(state)}, text=True, capture_output=True,
            )
            assert result.returncode == 0, scenario["id"]
            assert json.loads(result.stdout) == scenario["stub"].get("profiles", [])


if __name__ == "__main__":
    main()
