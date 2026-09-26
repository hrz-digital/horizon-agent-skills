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
    require("skills/horizon/SKILL.md", "references/cli-installation.md", "references/connections.md", "implement plan", "Executar o plano", "approved-to-implement")
    require("skills/horizon/references/cli-installation.md", "horizon version --check --json", "updateAvailable")
    require("skills/horizon-ask-for-guidance/SKILL.md", "Semantic engine", "Actual configured Metadata", "Published Metadata", "owned secondary Structure", "Completion:")
    require("skills/horizon/references/connections.md", "horizon connection list --check --json", "--connection")
    for skill in ("horizon-runtime", "horizon-metadata-authoring", "horizon-architecture-analysis"):
        require(f"skills/{skill}/SKILL.md", "Run `horizon` bootstrap")
    require("skills/horizon-interview/SKILL.md", "implementation-plan.md", "Planning gates", "Business Data mutation", "explicit confirmation", "#three-layer-metadata-proposal", "#structure-and-page-defaults")
    require("skills/horizon-interview/SKILL.md", "## Plan summary", "## Execution and User testing", "large work spanning multiple sessions with substantial dependencies or sequencing", "User explicitly requests a durable plan", "Multiple Structures, bulk work, and interview depth do not by themselves require a file", "pending User acceptance", "every additional Business Data mutation still needs explicit confirmation")
    require("skills/horizon-interview/SKILL.md", "New Structures alone do not imply a data-model-only request", "Always show all three headings", "Customer: <confirmed customer", "Installation: <selected live-valid", "only the three architecture layers belong under Metadata")
    summary = (ROOT / "skills/horizon-interview/SKILL.md").read_text().split("## Plan summary\n", 1)[1].split("## Execution and User testing", 1)[0]
    template = summary.split("```markdown\n", 1)[1].split("\n```", 1)[0]
    assert [line for line in template.splitlines() if line.startswith(("## ", "### "))] == [
        "## Scope", "## Metadata", "### Data Modeling", "### Visualization", "### Automation",
        "## Business Data", "## Execution", "## Complexity", "## Risks", "## Validation", "## Next",
    ]
    assert template.count("| Structure | Create inputs | List columns | Details groups and Field order |") == 1
    assert template.index("### Visualization") < template.index("| Structure | Create inputs") < template.index("### Automation")
    require("skills/horizon-interview/SKILL.md", "one row per new Structure", "one unlabeled Details group")
    require("skills/horizon-interview/references/implementation-plan.md", "### Metadata", "## Complexity", "out of scope (no configuration needed)", "| Structure | Create inputs | List columns | Details groups and Field order |")
    require("skills/horizon-metadata-authoring/SKILL.md", "one unlabeled group", "named groups only when they improve navigation")
    require("skills/horizon-interview/SKILL.md", "default currency in Visualization as display formatting")
    require("skills/horizon-metadata-authoring/SKILL.md", "without treating this display default as a restriction on stored values")
    require("skills/horizon/SKILL.md", "current session", "without looking for a file")
    for skill in ("horizon-metadata-authoring", "horizon-runtime"):
        require(f"skills/{skill}/SKILL.md", "#execution-and-user-testing")
    require("skills/horizon-interview/references/implementation-plan.md", "Status: awaiting-approval", "Status: approved-to-implement", "Connection:", "API URL:", "Execution complexity", "Session recommendation", "Approval gate", "Source column", "anonymized examples", "current Discovery remains source of truth")
    require("skills/horizon-ask-for-guidance/SKILL.md", "implement plan", "Executar o plano", "#planning-gates", "#implement-approved-plan")
    require("skills/horizon/SKILL.md", "#lifecycle", "Runtime-only work does not require a Workspace", "approved or previously selected", "recorded progress")
    require("skills/horizon-interview/references/implementation-plan.md", "Status: in-progress", "Status: draft", "Status: completed", "Approval gate `pending`", "Expected changes from completed steps are progress", "skip completed mutations", "Business Data: <targets", "Workspace code and selection decision only when applicable")
    require("skills/horizon-metadata-authoring/SKILL.md", "out of scope (User-directed)", "Apply only when Visualization is in scope", "all agreed Metadata changes", "Discover allowed Relation targets")
    require(
        "skills/horizon-metadata-authoring/SKILL.md", "Reuse an existing Widget", "when", "notWhen", "mock", "usages",
        "pinned immutable versions", "inherit the platform default", "ready before measurement",
        "Blocked third-party requests must still render", "never third-party downloads",
        "horizon metadata asset upload", "Register a new font or a new GeoJSON",
        "the schema it names", "Never take the href or the payload shape from memory",
        "font descriptors and attribution from the discovered asset contract",
        "authoring-conventions.md",
    )
    require(
        "skills/horizon/references/authoring-conventions.md",
        "defaultLocale", "PT, ES, and EN", "Omit an uncertain optional translation", "snake_case",
    )

    require("skills/horizon-metadata-authoring/SKILL.md",
            "prefer an available atomic batch-creation affordance",
            "keep different Structures in separate requests",
            "If batch creation is absent or unavailable",
            "track completed writes",
            "A failed batch commits no Fields",
            "never switch to singles to bypass a rejected batch",
            "skill installation alone does not establish platform capability")
    scenarios = json.loads((ROOT / "tests/scenarios.json").read_text())
    required = {
        "missing-cli", "unsupported-cli", "update-available", "install-refused", "zero-profiles", "one-profile", "many-profiles",
        "invalid", "unreachable", "error", "explicit-choice", "explicit-propagation",
        "safe-onboarding", "discovery-workflow", "acceptance-journey", "field-authoring-journey", "widget-authoring-journey",
        "package-asset-upload-journey",
        "simple-task-skips-interview",
        "complex-metadata-chat-plan",
        "business-data-confirmation", "data-model-only-scope", "page-only-completion",
        "durable-plan-request", "large-multi-session-plan", "workspace-resume-without-plan",
        "same-session-summary-and-adjustments",
        "three-structures-three-layers",
    }
    required.update({"field-batch-authoring", "field-batch-unavailable", "field-batch-rejected"})
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
