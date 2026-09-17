# Implementation plan

Use one file per effort:

`.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md`

This relative path and `/` separator work on Windows, macOS, and Linux; use native separators when accessing it.

Keep plan concise. It captures shared understanding, not platform truth. Re-read current Discovery before every execution step.

```markdown
# <title>

Status: awaiting-approval
Customer: <customer-code>
Installation: <installation-code>
Created: <date>

## Goal
<desired outcome>

## Scope
- In scope: <...>
- Out of scope: <...>

## Decisions
- <decision and rationale>

## Affected work
- Metadata: <structures, fields, relations, pages, views, actions, etc.>
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
<optional; include whether new session is recommended>
```

For spreadsheet or bulk Business Data work, add a compact mapping table under **Affected work**:

| Source column | Destination | Transform/validation | Missing or invalid handling |
|---|---|---|---|
| `<column>` | `<Field/Relation or Ignore>` | `<rule>` | `<decision>` |

Record row counts and anonymized examples only. Never copy raw records, credentials, tokens, or secrets.

When scope changes or new evidence changes a decision, set `Status: draft`, update plan, and obtain approval again. When work finishes, recommend purging plan; current Discovery remains source of truth.
