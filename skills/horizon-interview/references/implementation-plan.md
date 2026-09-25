# Implementation plan

Use one file per effort:

`.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md`

This relative path and `/` separator work on Windows, macOS, and Linux; use native separators when accessing it.

Create the plan only after selecting the Installation, inspecting its Discovery and existing Metadata, and resolving decisions through interview ↔ targeted Discovery checks. Keep plan concise. It captures shared understanding, not platform truth. Re-read current Discovery before every execution step.

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
- Data Modeling: <agreed Structures, Fields, Relations, Constraints, or no configuration needed (agreed)>
- Visualization: <agreed Data Sources, Pages, Views, Nodes, Widgets, or no configuration needed (agreed)>
- Automation: <agreed Actions, Alerts, executable rules, or no configuration needed (agreed)>
- Business Data: <types, scope, intended create/update/delete effects, or none>

## Steps
1. <step>

## Risks and unresolved questions
- <risk or None>

## Validation evidence
- <Discovery links, schema/catalog evidence, preview or validation result>

## Approval gate
Explicit approval required before mutation: <pending|approved>

## Resume notes
<session recommendation; when work starts, record Workspace code, completed steps, and next step>
```

Before requesting approval, show User a concise review summary from this plan (not only its path):

```markdown
Plan: <path> — awaiting approval
Data Modeling: <Structures and Primary/Secondary classifications; source → target Relations, cardinalities, ownership; required and derived Fields>
Visualization: <per-Structure Create inputs, List columns, Details groups; parent-to-child Navigation>
Automation: <agreed behavior or no configuration needed>
Execution: <Workspace reuse/new, order, validation and diff>
Risks/unresolved decisions: <none, or return to interview>
Execution complexity: <small/moderate/large — concrete authoring and validation workload>
Session recommendation: <continue / fresh session — reason>
No Metadata or Business Data changes made. Approval starts authoring, not Publication.
```

After explicit approval of the reviewed plan, set `Status: approved-to-implement` and Approval gate to `approved`. On execution start, set `Status: in-progress` and record Workspace and progress in Resume notes so later sessions can resume rather than replay edits. A changed scope or material evidence returns Status to `draft` and Approval gate to `pending` for renewed approval. Confirm Customer and Installation with User rather than splitting a Connection Profile label. Store the selected profile label and checked non-secret API URL so a later session can verify the intended Installation without guessing.

For spreadsheet or bulk Business Data work, add a compact mapping table under **Affected work**:

| Source column | Destination | Transform/validation | Missing or invalid handling |
|---|---|---|---|
| `<column>` | `<Field/Relation or Ignore>` | `<rule>` | `<decision>` |

Record row counts and anonymized examples only. Never copy raw records, credentials, tokens, or secrets.

After agreed execution and validation, mark `Status: completed` so it is no longer offered for implementation; recommend purging the plan; current Discovery remains source of truth.
