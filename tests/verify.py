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
    require("skills/horizon/references/cli-installation.md", "horizon version --check --json", "updateAvailable")
    require("skills/horizon-ask-for-guidance/SKILL.md", "Semantic engine", "Actual configured Metadata", "Published Metadata", "owned secondary Structure", "Completion:")
    require("skills/horizon/references/connections.md", "horizon connection list --check --json", "--connection")
    for skill in ("horizon-runtime", "horizon-metadata-authoring", "horizon-architecture-analysis"):
        require(f"skills/{skill}/SKILL.md", "Run `horizon` bootstrap")
    require("skills/horizon-interview/SKILL.md", "implementation-plan.md", "awaiting-approval", "Business Data mutation", "explicit confirmation", "After completion, recommend User purge")
    require("skills/horizon-interview/references/implementation-plan.md", "Status: awaiting-approval", "Approval gate", "Source column", "anonymized examples", "current Discovery remains source of truth")
    require(
        "skills/horizon-metadata-authoring/SKILL.md", "Reuse an existing Widget", "when", "notWhen", "mock", "usages",
        "pinned immutable versions", "inherit the platform default", "ready before measurement",
        "Blocked third-party requests must still render", "never third-party downloads",
        "horizon metadata asset upload", "Register a new font or a new GeoJSON",
        "the schema it names", "Never take the href or the payload shape from memory",
        "font descriptors and attribution from the discovered asset contract",
        "authoring-conventions.md", "defaultLocale", "never invent uncertain translations", "snake_case",
    )
    require(
        "skills/horizon/references/authoring-conventions.md",
        "defaultLocale", "PT, ES, and EN", "Omit an uncertain optional translation", "snake_case",
    )

    scenarios = json.loads((ROOT / "tests/scenarios.json").read_text())
    required = {
        "missing-cli", "unsupported-cli", "update-available", "install-refused", "zero-profiles", "one-profile", "many-profiles",
        "invalid", "unreachable", "error", "explicit-choice", "explicit-propagation",
        "safe-onboarding", "discovery-workflow", "acceptance-journey", "field-authoring-journey", "widget-authoring-journey",
        "package-asset-upload-journey",
        "simple-task-skips-interview",
        "complex-metadata-plan-gate",
        "business-data-confirmation",
    }
    assert required == {scenario["id"] for scenario in scenarios}

    stub = ROOT / "tests/stub-horizon"
    for scenario in scenarios:
        if "stub" not in scenario:
            continue
        with tempfile.TemporaryDirectory() as directory:
            state = pathlib.Path(directory) / "state.json"
            state.write_text(json.dumps(scenario["stub"]))
            version_check = subprocess.run(
                [stub, "version", "--check", "--json"],
                env={"HORIZON_STUB_STATE": str(state)}, text=True, capture_output=True,
            )
            assert version_check.returncode == 0, scenario["id"]
            status = json.loads(version_check.stdout)
            assert set(status) == {"current", "latest", "available", "updateAvailable"}, scenario["id"]
            result = subprocess.run(
                [stub, "connection", "list", "--check", "--json"],
                env={"HORIZON_STUB_STATE": str(state)}, text=True, capture_output=True,
            )
            assert result.returncode == 0, scenario["id"]
            expected = scenario["stub"].get("profiles", scenario["stub"].get("profileLists", [[]])[0])
            assert json.loads(result.stdout) == expected
            if len(scenario["stub"].get("profileLists", [])) > 1:
                result = subprocess.run(
                    [stub, "connection", "list", "--check", "--json"],
                    env={"HORIZON_STUB_STATE": str(state)}, text=True, capture_output=True,
                )
                assert json.loads(result.stdout) == scenario["stub"]["profileLists"][1]


if __name__ == "__main__":
    main()
