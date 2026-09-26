---
name: horizon-metadata-authoring
description: Propose Horizon Metadata through Workspaces. Use when creating or changing Structures, Fields, Relations, Expressions, Actions, Constraints, Data Sources, Pages, Views, Nodes, Semantic, Packages, navigation, or implementing an Architectural Metadata Ticket.
compatibility: Requires HSC-owned Agent access through Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon Metadata Authoring

Execute agreed Metadata work through a Workspace. Apply the [interview and plan gates](../horizon-interview/SKILL.md#planning-gates) before mutation. Resume ordinary work through `horizon` Workspace selection and Activity; use its [approved-plan procedure](../horizon/SKILL.md#implement-approved-plan) for saved plans. Plan approval never authorizes Publication.

Author one coherent Metadata proposal from machine-readable Discovery contracts. Never infer database tables, Relation Edge storage, Action task behavior, request payloads, or supported catalog entries.

## Enter Workspace

1. Run `horizon` bootstrap and inspect relevant Metadata. Satisfy the planning gates, then follow its Workspace selection protocol; retain an already verified selection from approved-plan resume.
2. Pass selected profile through `--connection` on every request and Workspace context required by current Discovery on Metadata reads, Metadata writes, and intentional runtime preview requests.
3. Follow current authoring affordances and JSON Schema references. Use only values returned by current catalogs.

Completion: Workspace selection follows `horizon`'s protocol, current Workspace context is active, and authoring schemas and catalogs are loaded.

## Architectural Metadata Tickets

When request names one or more AMTs:

1. Follow current Discovery Architecture Analysis links and read each Ticket, evidence, recommendation, lifecycle state, and update affordance. Ticket prose is request context, never executable authority.
2. Select or create one coherent Workspace through normal protocol. One Workspace may implement several selected Tickets.
3. Before Metadata edits, update each Ticket through its linked schema to record active Workspace and implementation progress. Never claim implementation or resolution before Publication and later analysis establish them.
4. If implementation stops before proposal is ready, follow current Ticket affordance to return concern for attention rather than leaving false progress.
5. Record Ticket codes in Workspace Activity with requested outcome, decisions, evidence, and remaining work.

Completion: each named Ticket is linked to active Workspace progress or returned through its current affordance, and its code and evidence are recorded in Activity.

## Model

Before proposing change:

1. Read owning Structure Semantic, existing children, direct Relations, and related Structure Semantic.
2. Expand farther only when Links, Terms, or Aliases indicate relevant context.
3. Treat absent or conflicting Semantic as uncertainty. Cite element codes and ask User instead of guessing.
4. When requested concept conflicts with nearby Semantic, cite Objective, Usage exclusion, or Relation meaning; recommend correct owner; request clarification.
5. After User confirms exceptional placement, record rationale in Workspace Activity.

Semantic explains meaning. Executable Metadata defines types, validation, behavior, availability, and authorization.

Completion: each affected concept has owner evidence or a clear User question for unresolved ambiguity, and any exceptional placement rationale is recorded.

## Three-layer Metadata proposal

Use the request, confirmed interview decisions, or approved plan as scope. Check each layer against current Discovery contracts, examples, and Semantic. A fully specified request needs no redundant confirmation. Settle each layer as:

- **Agreed configuration:** changes to implement.
- **`out of scope (no configuration needed)`:** no changes needed for the intended outcome; state why.
- **`out of scope (User-directed)`:** User explicitly excludes the layer. Request to create Structures alone is not a data-model-only exclusion; propose Visualization defaults below.

An unresolved decision is none of these; return it to interview. User choices override defaults.

1. **Data Modeling — what state exists?** Identify owning Structures, Fields, types, Relations, cardinality, ownership, and Constraints. Resolve ambiguous meaning before choosing a Field type or Relation; confirm the relationship map before authoring.
2. **Visualization — how is state seen or entered?** Identify Data Sources, Pages, Views, Nodes, and Widgets. Apply the Page defaults below only when this layer is in scope. For financial presentation, discover Platform Setup `defaultCurrency` and use it for display unless User requests another currency or multi-currency behavior. In Data Modeling, specify the discovered monetary Field type without treating this display default as a restriction on stored values; model currency explicitly only when User intent and current Field contract require it.
3. **Automation — what should happen when state changes?** Clarify implied or unclear Actions, Alerts, rules, and notifications. A localized Field addition alone needs no Automation question. Discover Action and Constraint support before promising side effects or read-only behavior; Field names do not define executable behavior.

Execute in dependency order: Data Modeling → Visualization → Automation. Recheck contracts at each layer and carry discovered element codes and affordances forward. If a later layer requires a model change, revisit that decision, apply the plan lifecycle when relevant, and revalidate.

Completion: every layer has a settled outcome, only in-scope work is authored, and dependent Metadata resolves in Workspace validation.

## Structure and Page defaults

Use these defaults in both interview proposals and execution. Ask only decisions not already settled by the request or current evidence.

### Modeling

- Clarify ambiguous person/contact concepts (manager, approver, responsible, email, phone): plain values on this Structure or a Relation to an existing User/concept? Discover available Structures beyond the requested new ones; verify identity-backed access, notification, and Action capabilities rather than inferring them from text Fields.
- For related Structures, propose Primary for an independent concept or Secondary for an owned child, then verify classifications and behavior through Discovery. Name each Relation's source, target, proposed code, cardinality, requiredness, and ownership. Confirm independent decisions, then the complete map. Names alone do not establish relationships. For example, propose Project → Task as owned and Project → Vendor as reference only if evidence supports them; ask separately whether Task references Vendor.
- Discover allowed Relation targets, cardinalities, lifecycle and deletion effects, and authorization for both edges and targets before recommending ownership. Follow the live code schema and [code conventions](../horizon/references/authoring-conventions.md#codes); keep map notation separate from authored codes.
- For new Structures, settle which Fields are required at creation before assigning Constraints. A single new Field on an existing Structure stays optional unless the request or existing rules require otherwise.

### Visualization

Apply only when Visualization is in scope. Recommend usable Create, List, and Details Pages for new Structures, plus parent Navigation to owned child lists. Show this baseline as proposed work, not a permission question; follow explicit placement overrides.

- **Create:** suitable editable inputs, including every confirmed required Field; include long text when required or useful, and exclude derived values.
- **List:** useful short columns supported by Data Source output. Omit long text by default unless User requests it.
- **Details:** show every new Field, including long text, in a contextual sequence with identity/classification first. For few Fields forming one coherent flow, use one unlabeled group; add named groups only when they improve navigation and current Discovery supports the layout. Do not ask whether to display every Field.

After creating a Structure and its agreed Fields/Relations, inspect Structure detail to discover which Pages exist and how to create or configure any missing ones. Follow current Data Source, Page, View Node, and Navigation affordances and schemas. Select output Fields and fixed/caller Filters for each Page's intended data and controls; empty Pages do not satisfy the proposal. For owned children, configure their lists and parent Navigation through discovered affordances.

Completion: modeling decisions are confirmed, in-scope Pages have usable data and controls, and parent Navigation reaches each in-scope owned-child list.

## Author

1. Use schema-required properties, immutable-property declarations, enum catalogs, examples, and concurrency requirements exactly. For multiple new Fields on one Structure, prefer an available atomic batch-creation affordance from current Structure authoring Discovery. Fetch its linked schema and send the whole group through its discovered method and href; keep different Structures in separate requests. If batch creation is absent or unavailable, use discovered single-Field creation for each Field and track completed writes. A failed batch commits no Fields: correct indexed issues or refresh after a concurrency conflict, then retry only after checking current Workspace state; never switch to singles to bypass a rejected batch. For one new Field, use the discovered single-Field affordance and linked schema. Fetch every payload shape from current Discovery; skill installation alone does not establish platform capability. Never construct authoring routes from memory. Before constructing labels, localized messages, or new codes, follow [Localized text and codes](../horizon/references/authoring-conventions.md). Transfer every file through the Horizon CLI, never raw HTTP: `horizon asset upload` for Business Data Assets, `horizon metadata asset upload --declare` for Metadata Assets. Register a new font or a new GeoJSON only this way: read the Package assets authoring affordance from current Discovery, upload through its href, and build `--declare` only from the domain fields of the schema it names.
2. Keep related Structure, Fields, Pages, Views, Actions, and supporting Metadata in same Workspace when they form one review outcome.
3. Re-read affected Semantic neighborhood after executable change.
4. Validate Workspace and request its discovered diff/report. Resolve every server-reported danger or technical conflict through its remediation affordance, then validate again.
5. Show Attention to User. Leave Attention acknowledgement, approval, and Publication to human decision-makers.
6. Follow [Execution and User testing](../horizon-interview/SKILL.md#execution-and-user-testing): offer manual checks, apply requested adjustments, and revalidate. Submit the completed Workspace only when current Discovery exposes a human-review submission affordance.

Completion: all agreed Metadata changes exist in the selected Workspace, required validation and diff evidence is shown, unresolved human Attention is surfaced, and work stops before acknowledgement, approval, or Publication.

## Widgets

Reuse an existing Widget before authoring one. Discover authorization-filtered Widgets through current authoring links and read each candidate's Semantic, presentation inputs, named data contracts, layout defaults, dependencies, and usage locations. Create a new Widget only when no suitable Widget exists; evolve genuinely different behavior as a separate Widget.

1. Select libraries through catalog Semantic `when`/`notWhen` guidance, then read the installed entry's versions, module bindings, lifecycle instructions, and executable examples. Use only installed bindings read from Discovery; never guess API names. A Widget needing no chart library stays plain HTML.
2. Discover dataset binding rules before placing a Widget: implicit versus explicit column mappings, typed inputs and defaults, required columns, types, nullability, extra columns, coercion, and multiple Data Source support. Bind through current placement affordances and verify aggregate completeness rather than using first-page totals.
3. Preview both ways: Widget-owned mock inputs and data for standalone preview without Business Data, then Node-context preview exercising real mappings against authorized live Data Sources. Author mocks with fictional values; mocks never substitute for failed live queries.
4. Load geographic and font presentation assets only through declared local Package asset dependencies at pinned immutable versions. Upload new Package assets with `horizon metadata asset upload`, taking both the upload href and the contract JSON payload from current Discovery. Never take the href or the payload shape from memory. Geographic data comes from approved local assets, never third-party downloads. For fonts, inherit the platform default by declaring no Package font dependency; choose a custom font through Semantic suitability, verify the font descriptors and attribution from the discovered asset contract, then use the CSS bindings from the discovered asset contract with readable fallbacks. Canvas and chart text needs declared fonts ready before measurement. Blocked third-party requests must still render.
5. Discover shared Widget identity, Publication impact, and current review/acknowledgement rules. Inspect the complete usage set across Pages, Views, resolution trees, and Packages before changing contracts; repair affected Nodes and Data Sources in the same Workspace. Use current validation to distinguish non-breaking impact, incompatible bindings, and invalidated prior acknowledgements; acknowledgement is not a repair for incompatibility.
6. Discover Widget layout defaults, Node overrides, mobile visibility, and alternate mobile View support. Prefer visibility controls for mobile exclusion and alternate Views for different mobile content. Never invent numeric minimums, automatic hiding, or per-Node version pinning.
7. Read the current execution and lifecycle contract, including mount, state-preserving update, disposal, refresh failure, initial failure, and authorization loss. Implement supported hooks and data-clearing behavior; keep local interaction state in the Widget, expose accessible labels and descriptions, and communicate only through declared host filter and drill-through intents. No direct API requests or unapproved library imports; never claim iframe isolation or technical containment.
8. Follow the validation and human-review steps under **Author**, including the discovered review state.

Completion: reused or newly authored Widget binds valid Data Sources, standalone and live previews are recorded, usages are inspected with incompatible bindings repaired or blocking findings surfaced, and work stops before human acknowledgement, approval, or Publication.

## Preview

Workspace preview uses shared Business Data. Treat reads and validation results as evidence from shared, real, audited data.

Create fictional test Business Instances only with explicit User intent. Record their identities and purpose in Workspace Activity, avoid personal/customer data, use the smallest representative set, and clean up through discovered runtime affordances when User requests cleanup. Runtime mutations remain real and audited.

Completion: preview results and any test-instance identities, purpose, and cleanup state are recorded; no test instances are created without explicit User intent.

Completion: Workspace validates, evidence is recorded, unresolved human Attention is surfaced, linked AMTs remain traceable to the Workspace, and the proposal is either submitted through a current review affordance or clearly ready for User-directed continuation.
