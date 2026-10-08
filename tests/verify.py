#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile
import uuid

ROOT = pathlib.Path(__file__).resolve().parents[1]


def require(path, *texts):
    value = (ROOT / path).read_text()
    for text in texts:
        assert text in value, f"{path}: missing {text!r}"


def main():
    require("skills/horizon-metadata-authoring/SKILL.md", "## Dashboard proposals", "Package-owned Installation presentation", "both the new and previous default", "human Publication remains pending")
    require("skills/horizon-runtime/SKILL.md", "## Inspect Dashboards", "without silently selecting another Dashboard", "do not invent additional Data Source read grants")
    version = (ROOT / "VERSION").read_text().strip()
    for skill in (ROOT / "skills").glob("*/SKILL.md"):
        frontmatter = skill.read_text().split("---", 2)[1]
        assert f'  version: "{version}"' in frontmatter, f"{skill}: metadata version differs from VERSION"
    require("skills/horizon-metadata-authoring/SKILL.md", "references/integrated-process-proof.md")
    require("skills/horizon-metadata-authoring/references/integrated-process-proof.md", "Completed iterations can undercount", "qualifying rolled-back transition", "unchanged Real data", "Completion:")
    require("skills/horizon/SKILL.md", "references/cli-installation.md", "references/connections.md", "implement plan", "Executar o plano", "approved-to-implement")
    require("skills/horizon/references/cli-installation.md", "horizon version --check --json", "updateAvailable")
    require("skills/horizon-ask-for-guidance/SKILL.md", "Semantic engine", "Actual configured Metadata", "Published Metadata", "owned secondary Structure", "Completion:")
    require("skills/horizon/references/connections.md", "horizon connection list --check --json", "--connection")
    for skill in ("horizon-runtime", "horizon-metadata-authoring", "horizon-architecture-analysis"):
        require(f"skills/{skill}/SKILL.md", "Run `horizon` bootstrap")
    require("skills/horizon-interview/SKILL.md", "implementation-plan.md", "Planning gates", "Business Data mutation", "explicit confirmation", "#three-layer-metadata-proposal", "#structure-and-page-defaults")
    require("skills/horizon-interview/SKILL.md", "## Plan summary", "## Execution and User testing", "large work spanning multiple sessions with substantial dependencies or sequencing", "User explicitly requests a durable plan", "Multiple Structures, bulk work, and interview depth do not by themselves require a file", "pending User acceptance", "every additional Business Data mutation still needs explicit confirmation")
    require("skills/horizon-interview/SKILL.md", "New Structures alone do not imply a data-model-only request", "always show all three headings, even when one layer has no questions", "Customer: <confirmed customer", "Installation: <selected live-valid", "only the three architecture layers belong under Metadata")
    summary = (ROOT / "skills/horizon-interview/SKILL.md").read_text().split("## Plan summary\n", 1)[1].split("## Execution and User testing", 1)[0]
    template = summary.split("```markdown\n", 1)[1].split("\n```", 1)[0]
    assert [line for line in template.splitlines() if line.startswith(("## ", "### "))] == [
        "## Scope", "## Metadata", "### Data Modeling", "### Visualization", "### Automation",
        "## Business Data", "## Execution", "## Complexity", "## Risks", "## Validation", "## Next",
    ]
    assert template.count("| Structure | Create inputs | List table, columns, and create trigger | Details groups and Field order |") == 1
    assert template.index("### Visualization") < template.index("| Structure | Create inputs") < template.index("### Automation")
    require("skills/horizon-interview/SKILL.md", "one row per new Structure", "one unlabeled Details group")
    require("skills/horizon-interview/references/implementation-plan.md", "### Metadata", "## Complexity", "out of scope (no configuration needed)", "| Structure | Create inputs | List table, columns, and create trigger | Details groups and Field order |")
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
    require("skills/horizon-metadata-authoring/SKILL.md",
            "unfinished work, not a valid finish",
            "A new Structure never settles Visualization this way",
            "Sequence the work as Structure → Fields → Data Source → Nodes",
            "A Page update replaces the whole View list",
            "Keep Data Source output and Page node selection as separate decisions",
            "Prove each Page by reading it back",
            "reported issues carry no severity",
            "treat each one as blocking",
            "is not a completed proposal",
            "no server-reported issue remains unresolved",
            "The minimum useful set is one field node per required Field on Create",
            "a table element bound to a Data Source over the owning Structure",
            "Give a table element a stable node code",
            "falls back to a positional binding that shifts when nodes are reordered",
            "Reach the Create Page with a create trigger element",
            "that the List table's Data Source resolves to the owning Structure",
            "that the Create Page is reachable from the Structure's Pages",
            "Read the exact node and source-data vocabulary from the current Page schema",
            "default_nodes_required")
    require("skills/horizon-interview/SKILL.md",
            "a new Structure's Visualization settles as agreed configuration or `out of scope (User-directed)` only",
            "the create trigger that makes each new Structure's Create Page reachable",
            "plus the create trigger reaching the Create Page",
            "Create/List/Details Pages → Views → Nodes, bindings, the create trigger reaching each Create Page",
            "Use this shape only when a round actually has questions.",
            "skip the interview round and show the Plan summary directly",
            "not a literal code fence",
            "ask none and go straight to the Plan summary when inspection and the request already settle everything",
            "Show a clarification round only when the agent holds at least one real question",
            "never show an empty round",
            "Skip the interview round when the agent has no question, and wait for approval before proposing any mutation",
            "wait for that approval before any mutation")
    require("skills/horizon-interview/references/implementation-plan.md",
            "A new Structure's Visualization settles as agreed configuration or `out of scope (User-directed)` only",
            "its generated Pages stay unfinished until configured",
            "the create trigger reaching each Create Page",
            "plus the create trigger reaching the Create Page")
    require("skills/horizon-metadata-authoring/SKILL.md",
            "## Test scenarios",
            "a test scenario is a normal part of feature validation",
            "Inspect existing Test instances before creating any",
            "cosmetic-only change",
            "supported Test operations",
            "never guess a route, parameter, or capability",
            "one meaningful failure case",
            "published Real creation is not a fallback",
            "Report a refused or unsupported effect as refused and suppressed",
            "outlives publication and Workspace deletion while its Structure exists",
            "route that destructive confirmation or approval to the User",
            "an Agent acknowledges, approves, and publishes nothing",
            "one Installation-wide scope shared by concurrent Workspaces",
            "instead of proposing a per-Workspace copy or sandbox",
            "separates observed runtime facts from suggested manual UI checks",
            "state plainly that it was not observed when no such tooling exists")
    require("skills/horizon-runtime/SKILL.md",
            "#test-scenarios",
            "creation there produces Test Business Instances while Real ones stay read-only",
            "read them instead of learning them by submitting a Real identifier",
            "is the fallback-free path when a Test operation is unsupported or denied")
    require("skills/horizon-interview/SKILL.md",
            "#test-scenarios",
            "name the Test instances it reuses or creates in the plan summary so approval covers them",
            "Fixtures beyond that set need fresh confirmation",
            "including the Test instances the checks reuse or create")
    require("skills/horizon-ask-for-guidance/SKILL.md", "test scenarios; explain that Workspace context validates against Test Business Instances")
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
        "three-structures-three-layers", "new-structure-page-defaults",
    }
    required.update({"field-batch-authoring", "field-batch-unavailable", "field-batch-rejected"})
    required.update({
        "test-scenario-new-structure", "test-scenario-fixture-reuse", "test-scenario-cross-scope-rejection",
        "test-scenario-unsupported-capability", "test-scenario-destructive-cleanup",
    })
    required.update({
        "process-empty-draft", "process-authoring-reuse", "process-authoring-workspace", "process-direct-run",
        "process-start-ambiguous", "process-action-delegation", "process-protection-authoring",
        "process-protection-conflict", "process-support-absent", "process-start-unavailable",
        "process-summary-oversight", "process-summary-missed-notice",
        "process-actions-selection-partial", "process-actions-selection-stop-uncertain",
        "process-actions-selection-coordinated", "process-conditional-composition",
        "process-query-transformation", "process-transformed-business-effects",
        "process-fan-out-authoring", "process-fan-out-recovery",
        "process-operation-labels-preserve", "process-json-starters-authoring",
        "process-json-starters-preserve-draft", "process-mutation-value-source-choice",
        "process-response-wait-authoring", "process-response-wait-inspection",
        "process-cancellation",
        "process-test-execution-purge",
        "process-test-execution-purge-refusals",
    })
    require("skills/horizon/SKILL.md", "Process Instance listing/inspection", "Process Definition or its Structure Action bindings")
    require("skills/horizon-metadata-authoring/SKILL.md",
            "Use Package-owned Process Definitions for executable workflow",
            "Read candidate Semantic", "configure Structure Action bindings inside the Process Definition",
            "binding creation does not grant launch authority", "## Active-execution protection",
            "Validate the proposed selection and read it back through Discovery",
            "otherwise report it untested, never substitute a Real run")
    require("skills/horizon-runtime/SKILL.md",
            "## Process runs", "direct or Action-backed", "ambiguous start response",
            "actual requesting Actor, Process Initiator, and automation Actor distinct",
            "Terminal settlement may permit the same inputs again",
            "## Inspect Process Instances", "linked summary contract", "actual caller's authority",
            "Live notices are hints", "Visibility through recipients or assignees")
    require("skills/horizon-metadata-authoring/SKILL.md",
            "For query and transformation work", "supported Relation selection",
            "current time and size limits", "persisted completed outputs",
            "require sanitization wherever", "hard memory isolation")
    require("skills/horizon-metadata-authoring/SKILL.md",
            "independent per-property draft scaffolds", "check defaults against the agreed business intent",
            "Preserve authored JSON when current starters change", "preserve existing translations",
            "Read labels, stable codes and affected references back", "guard reference to an earlier Condition identity",
            "Discover Query cardinality", "Script object results do not establish whole-object Query support",
            "silently choosing the first row", "prefer direct Field mappings",
            "Choose one supported mutation value source", "creation does not reuse an update target")
    require("skills/horizon-runtime/SKILL.md",
            "For query and transformation runs", "bounded failures",
            "does not freeze referenced Metadata or Business Data")
    require("skills/horizon-runtime/SKILL.md",
            "For cancellation, discover whether the acting identity actually holds the administrative privilege",
            "are not undone", "report stopping and finished separately",
            "settle rather than revive cancelled work")
    required.update({
        "process-one-time-schedule-authoring",
        "process-one-time-schedule-workspace-exercise",
        "process-one-time-schedule-inspection-recovery",
        "process-recurring-schedule-authoring",
        "process-recurring-schedule-edit-recovery",
        "process-missed-schedule-policy",
        "process-scheduled-recovery-controls",
    })
    require("skills/horizon-metadata-authoring/SKILL.md",
            "## One-time schedules", "read the converted instant back through Discovery",
            "Workspace schedules remain inactive automatically",
            "Keep Publication with the eligible human")
    require("skills/horizon-runtime/SKILL.md",
            "### Scheduled starts", "System initiation and schedule/occurrence provenance",
            "preserve that boundary instead of launching equivalent work manually",
            "inspect durable occurrence and execution state",
            "make no real-time dispatch promise")
    require("skills/horizon-metadata-authoring/SKILL.md", "Settle missed-work intent explicitly", "downtime spanning multiple recurrences")
    require("skills/horizon-runtime/SKILL.md", "discovered lateness tolerance", "administrative Actor audit", "committed winner", "Delegated summary oversight alone")
    required.update({
        "process-watched-trigger-authoring",
        "process-watched-trigger-delayed-recovery",
        "process-watched-trigger-workspace-exercise",
    })
    require("skills/horizon-metadata-authoring/SKILL.md",
            "## Watched Business Data triggers", "watched-change selection separate from state conditions",
            "original event values govern matching", "notification delivery retry")
    require("skills/horizon-runtime/SKILL.md",
            "### Event-triggered process inspection", "original Mutation and Actor",
            "a causal safeguard stop preserves earlier effects", "An exercise is not a subscription")
    required.update({"integrated-periodic-process-proof", "integrated-partial-generation-recovery"})
    automation = [scenario for scenario in scenarios if scenario["id"].startswith("automation-")]
    assert len(automation) == 12
    assert {scenario["contractFixture"] for scenario in automation} == {"supported", "restricted", "failed", "absent"}
    for scenario in automation:
        assert scenario["trace"] == {"connection": "Acme", "readOnly": True, "startAtDiscovery": True, "followReturnedLinks": True}
        assert len(scenario["expect"]) >= 3
    required.update(scenario["id"] for scenario in automation)
    require("skills/horizon-interview/SKILL.md", "cosmetic-only edit", "actual automation dependency")
    require("skills/horizon-metadata-authoring/SKILL.md", "ordinary scheduled selection and notification", "narrow reference exception", "logical initiator override cannot answer")
    require("skills/horizon-runtime/SKILL.md", "unavailable reason without a link", "response eligibility", "supported in-platform notifications")
    required.update({"smtp-configure-test-feedback", "smtp-test-unavailable-or-uncertain"})
    require("skills/horizon-runtime/SKILL.md", "## Configure and test an SMTP server",
            "preserve their values", "trusted secret-input channel", "provider acceptance", "Test the saved configuration", "Installation-wide saved settings", "Keep Process testing restrictions separate", "wait for that explicit confirmation before saving acknowledgment", "After the User explicitly confirms successful receipt", "register the agreed definition, test the saved configuration, give feedback and ask for receipt confirmation")
    require("skills/horizon/SKILL.md", "Installation SMTP configuration or email delivery check")
    required.update({"dashboard-presentation-workspace-journey", "dashboard-independent-source-refusal", "dashboard-package-default-proposal", "dashboard-independent-authority", "dashboard-unavailable-default", "dashboard-unavailable-authoring"})
    require("skills/horizon-metadata-authoring/SKILL.md", "preserve unrelated authored trees and sources", "Select the entry Page explicitly", "Follow discovered validation and submission affordances")
    require("skills/horizon-runtime/SKILL.md", "Query sources independently", "never retry through a Relation context")
    assert required == {scenario["id"] for scenario in scenarios}

    stub = ROOT / "tests/stub-horizon"
    # Adapter transport checks use generated paths, not a cached Horizon feature contract.
    with tempfile.TemporaryDirectory() as directory:
        base = pathlib.Path(directory)
        linked = "/" + uuid.uuid4().hex
        hidden = "/" + uuid.uuid4().hex
        state = base / "state.json"
        state.write_text(json.dumps({"selected": "Acme"}))
        contracts = base / "contracts.json"
        contracts.write_text(json.dumps({
            "GET /discovery": {"status": 200, "body": {"link": {"hrefTemplate": linked + "/{identity}"}}},
            "GET " + linked + "/sample": {"status": 200, "body": {"ok": True}},
            "GET " + hidden: {"status": 200, "body": {"ok": True}},
        }))
        environment = {"HORIZON_STUB_STATE": str(state), "HORIZON_STUB_CONTRACT": str(contracts)}
        for path, success in [(hidden, False), ("/discovery", True), (linked + "/sample", True)]:
            response = subprocess.run([stub, "request", "--connection", "Acme", "GET", path], env=environment, text=True, capture_output=True)
            assert (response.returncode == 0) == success, response.stderr

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
