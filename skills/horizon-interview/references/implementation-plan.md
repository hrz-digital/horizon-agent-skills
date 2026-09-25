# Implementation plan

Use this reference only when the [plan-file gate](../SKILL.md#planning-gates) applies: large multi-session work with substantial dependencies or sequencing, or an explicit User request for a durable plan. Otherwise use the in-chat summary and execute in the same session.

A local plan records agreed intent and progress, not platform contracts or executable authority. Create it after Installation inspection and clarification; execute through current Discovery and the appropriate skill.

## Location and privacy

Use one file per effort: `.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md`. Normalize components to lowercase `[a-z0-9._-]`, replace other characters with `-`, and reject empty, `.` or `..` components and path separators. Use native separators when accessing the path.

Confirm Customer and Installation with User rather than splitting a Connection Profile label. Store the selected profile label and checked non-secret API URL for later identity verification.

Plans are local and personal. Do not add host `.gitignore` entries automatically. Never store credentials, tokens, raw Business Data, or raw spreadsheet contents. Use counts and anonymized examples only.

## Contents

For Metadata layer outcomes, use the [three-layer proposal](../../horizon-metadata-authoring/SKILL.md#three-layer-metadata-proposal): agreed configuration, `out of scope (no configuration needed)` with reason, or `out of scope (User-directed)` for explicit exclusion. A new Structure normally includes proposed Visualization. When Visualization is in scope for new Structures, fill one table row per Structure; omit table when out of scope.

```markdown
# <title>

Status: awaiting-approval
Customer: <confirmed customer-code>
Installation: <confirmed installation-code>
Connection: <exact selected Connection Profile label>
API URL: <checked non-secret apiUrl>
Created: <date>

## Goal
<desired outcome>

## Scope
- In scope: <...>
- Out of scope: <...>

## Decisions
- <decision and rationale>

## Affected work
### Metadata
- Data Modeling: <Structures, Fields, Relations, Constraints; or out of scope — reason>
- Visualization: <Data Sources; per-Structure Create/List/Details Pages → Views → Nodes, bindings and navigation; or out of scope — reason>

| Structure | Create inputs | List columns | Details groups and Field order |
| --- | --- | --- | --- |
| <each new Structure> | <editable inputs, including required Fields> | <useful short columns> | <one unlabeled group in contextual order when sufficient; otherwise named groups with Fields> |

- Automation: <Actions, rules and effects; or out of scope — reason>
### Business Data
- Business Data: <targets, record scope, values, intended effects, failure handling; or not applicable — reason>

## Steps
1. <step>

## Complexity
<execution and validation workload with reason, even if small>

## Risks and unresolved questions
- <risk or None; unresolved decisions block approval>

## Validation evidence
- <Discovery links, schema/catalog evidence, preview or validation result>

## Approval gate
Explicit approval required before mutation: <pending|approved>

## Resume notes
<session recommendation; completed steps and evidence, next step; Workspace code and selection decision only when applicable>
```

For spreadsheet or bulk Business Data work, add under **Affected work**:

| Source column | Destination | Transform/validation | Missing or invalid handling |
|---|---|---|---|
| `<column>` | `<Field/Relation or Ignore>` | `<rule>` | `<decision>` |

## Approval summary

Show the [Plan summary](../SKILL.md#plan-summary), not just the path, with these file-specific additions:

```markdown
Plan: <path> — awaiting approval
Persistence reason: <large multi-session dependencies/sequencing or User request>
Execution complexity: <concrete execution and validation workload>
Session recommendation: <continue / handoff — reason>
Mutation state: <none yet, or completed work when reviewing a revised plan>
```

Approval allows execution in the same session; saving a file does not require a fresh session. User testing and adjustments follow the interview skill's execution loop.

## Lifecycle

- **Draft:** unresolved decisions or unexpected material changes block execution. Set `Status: draft` and Approval gate `pending`.
- **Review:** when decisions are settled, set `Status: awaiting-approval`, keep Approval gate `pending`, and show the approval summary.
- **Approval:** after explicit approval of that summary, set `Status: approved-to-implement` and Approval gate `approved`.
- **Execution:** set `Status: in-progress` when work starts. Record completed steps, evidence, and next step in Resume notes; include Workspace identity and selection decision only for Metadata work. Update progress as steps complete.
- **Completion:** after agreed execution and validation, set `Status: completed`; it is no longer eligible for implementation. Recommend User purge the plan; current Discovery remains source of truth.

On resume, compare current evidence with approved scope **and recorded progress**. Expected changes from completed steps are progress, not approval-invalidating drift. Verify their results and skip completed mutations; if completion is uncertain, reconcile current state before continuing. Unexpected changes affecting remaining work return the plan to Draft, preserve completed-step evidence, and require an updated review and approval before further mutation.

Resume through `horizon`'s [approved-plan procedure](../../horizon/SKILL.md#implement-approved-plan) for target verification, conditional Workspace selection, and execution routing.
