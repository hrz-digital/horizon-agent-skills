---
name: horizon-interview
description: Plan unclear, broad, multi-step, bulk, relational, destructive, or cross-surface Horizon work before execution. Use for complex Metadata proposals and Business Data mutations; skip for small, unambiguous requests.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1 when platform facts are needed.
metadata:
  author: hrz-digital
  version: "1.3.1"
---

# Horizon Interview

Reach shared understanding before execution. This is a planning gate, not a replacement for Discovery. Platform contracts, schemas, catalogs, routes, availability, authorization, and Metadata Context remain authoritative in current Discovery.

## Decide whether to interview

Use a full interview when the request is unclear, broad, multi-step, bulk, relational, destructive, or spans multiple Metadata surfaces or sessions. Examples include a Structure with Fields, Data Sources, Pages, Views, and Actions, or importing a spreadsheet into Business Data.

For a small, unambiguous Metadata change, proceed without a full interview. For every Business Data mutation, obtain explicit confirmation of target, records, values, and intended effect; use a full interview for bulk, relational, destructive, or ambiguous work.

## Interview

1. Before bootstrap, clarify goal, scope, outcome, constraints, and what is out of scope. Ask only decisions; find environmental facts yourself.
2. Bootstrap Horizon after initial intent is clear. Select an explicit live-valid customer Installation.
3. Inspect current Discovery, Published Metadata, relevant Workspace state, schemas, catalogs, runtime affordances, and availability. Ask User only about decisions Discovery cannot settle.
4. For Metadata requests, frame decisions in three layers: **Data Modeling** (Structures, Fields, Relations, types, Constraints), **Visualization** (Data Sources, Pages, Views, Nodes, Widgets), **Automation** (Actions, Alerts, executable rules and supported side effects). Show User a recommendation for each layer, including `none` when no work is needed. Ask only decisions that affect the requested outcome; accept `none` and explicit User overrides of defaults. For multiple Structures, propose a relationship map with Primary/Secondary classification and each Relation's source, target, cardinality, and ownership; confirm it before authoring. A proposed relationship from names is never a decision.
5. Work questions in rounds. Ask every currently unblocked decision, include a recommendation, wait for answers, and recompute the remaining questions. Do not silently assume unresolved answers.
6. For Business Data creation or change, make destination, identity, relationships, values, validation, duplicate/update behavior, failure handling, scope, and intended effects explicit. For spreadsheet imports, map every source column to a destination or an explicit ignore decision; record counts and anonymized examples, never raw records.
7. Write a concise plan using [implementation-plan.md guidance](references/implementation-plan.md) at `.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md` after Installation selection. Normalize path components to lowercase `[a-z0-9._-]`; replace other characters with `-`; reject empty values and `..`, `/`, or `\\`.
8. Set plan status to `awaiting-approval` and show User unresolved questions, risks, intended mutations, and whether a new session is recommended. Wait for explicit approval.
9. On scope or material-evidence change, return plan to `draft`, update it, and request approval again. After completion, recommend User purge the plan to prevent stale guidance; Discovery remains the only source of truth.

Plans are local and personal. Do not add host `.gitignore` entries automatically. Never write credentials, tokens, raw Business Data, or raw spreadsheet contents to a plan.

Completion: Metadata plan records agreed decisions or `none` for each layer, plus scope, evidence, risks, validation, and approval gate; User explicitly approves before execution; no platform mutation occurs during interview.
