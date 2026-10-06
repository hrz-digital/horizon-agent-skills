---
name: horizon-metadata-authoring
description: Propose Horizon Metadata through Workspaces. Use when creating or changing Structures, Fields, Relations, Expressions, Structure Action bindings, Constraints, Data Sources, Pages, Views, Nodes, Semantic, Packages, navigation, Process Definitions, or implementing an Architectural Metadata Ticket.
compatibility: Requires HSC-owned Agent access through Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.5.0"
---

# Horizon Metadata Authoring

Execute agreed Metadata work through a Workspace. Apply the [interview and plan gates](../horizon-interview/SKILL.md#planning-gates) before mutation. Resume ordinary work through `horizon` Workspace selection and Activity; use its [approved-plan procedure](../horizon/SKILL.md#implement-approved-plan) for saved plans. Plan approval never authorizes Publication.

Author one coherent Metadata proposal from machine-readable Discovery contracts. Never infer database tables, Relation Edge storage, Action task behavior, request payloads, or supported catalog entries.

## Enter Workspace

1. Run `horizon` bootstrap and inspect relevant Metadata. Satisfy the planning gates, then follow its Workspace selection protocol; retain an already verified selection from approved-plan resume.
2. Pass selected profile through `--connection` on every request and Workspace context required by current Discovery on Metadata reads, Metadata writes, and the Test-scenario validation requests below.
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
- **`out of scope (no configuration needed)`:** no changes needed for the intended outcome; state why. A new Structure never settles Visualization this way, because its generated Pages stay unfinished until configured; use `agreed configuration` or `out of scope (User-directed)` instead.
- **`out of scope (User-directed)`:** User explicitly excludes the layer. Request to create Structures alone is not a data-model-only exclusion; propose Visualization defaults below.

An unresolved decision is none of these; return it to interview. User choices override defaults.

1. **Data Modeling — what state exists?** Identify owning Structures, Fields, types, Relations, cardinality, ownership, and Constraints. Resolve ambiguous meaning before choosing a Field type or Relation; confirm the relationship map before authoring.
2. **Visualization — how is state seen or entered?** Identify Data Sources, Pages, Views, Nodes, and Widgets. Apply the Page defaults below only when this layer is in scope. For financial presentation, discover Platform Setup `defaultCurrency` and use it for display unless User requests another currency or multi-currency behavior. In Data Modeling, specify the discovered monetary Field type without treating this display default as a restriction on stored values; model currency explicitly only when User intent and current Field contract require it.
3. **Automation — what behavior should run?** Use Package-owned Process Definitions for executable workflow, including their Structure Action bindings, triggers, operations, notification behavior and Human Interaction orchestration. Business state and Relations remain Data Modeling; Pages, Data Sources for presentation and visible placement remain Visualization. Treat requested alerts as business intent, not separate Structure-owned executable Metadata. Discover support before proposing triggers, operations, or notifications; Field names do not define executable behavior. A localized Field addition alone needs no Automation question. Revisit earlier layers only when automation requires a model or presentation change.

Execute in dependency order: Data Modeling → Visualization → Automation. Recheck contracts at each layer and carry discovered element codes and affordances forward. If a later layer requires a model change, revisit that decision, apply the plan lifecycle when relevant, and revalidate.

Completion: every layer has a settled outcome, only in-scope work is authored, and dependent Metadata resolves in Workspace validation.

## Active-execution protection

When concurrent runs for the same business inputs would interfere, select declared inputs that express that boundary through the definition's current authoring affordance. Confirm the intended grouping with the User when it is unclear; include every input needed to distinguish independent work. Read normalization, defaults, Data Scope, Publication, and lifecycle semantics from Discovery before promising which starts conflict. Validate the proposed selection and read it back through Discovery.

Treat active-execution protection as a concurrency policy. Express permanent business uniqueness and intentional repeat policy separately through the appropriate Metadata. A new definition revision alone does not justify assuming earlier work has finished.

Completion: the intended grouping is settled, the discovered protection selection is validated and read back, and business repeat policy remains explicit.

## Structure and Page defaults

Use these defaults in both interview proposals and execution. Ask only decisions not already settled by the request or current evidence.

### Modeling

- Clarify ambiguous person/contact concepts (manager, approver, responsible, email, phone): plain values on this Structure or a Relation to an existing User/concept? Discover available Structures beyond the requested new ones; verify identity-backed access, notification, and Action capabilities rather than inferring them from text Fields.
- For related Structures, propose Primary for an independent concept or Secondary for an owned child, then verify classifications and behavior through Discovery. Name each Relation's source, target, proposed code, cardinality, requiredness, and ownership. Confirm independent decisions, then the complete map. Names alone do not establish relationships. For example, propose Project → Task as owned and Project → Vendor as reference only if evidence supports them; ask separately whether Task references Vendor.
- Discover allowed Relation targets, cardinalities, lifecycle and deletion effects, and authorization for both edges and targets before recommending ownership. Follow the live code schema and [code conventions](../horizon/references/authoring-conventions.md#codes); keep map notation separate from authored codes.
- For new Structures, settle which Fields are required at creation before assigning Constraints. A single new Field on an existing Structure stays optional unless the request or existing rules require otherwise.

### Visualization

Apply only when Visualization is in scope. A Page whose `default` View carries no nodes is unfinished work, not a valid finish, because it renders nothing. Treat usable Create, List, and Details Pages for new Structures, plus parent Navigation to owned child lists, as the default end state rather than a recommendation. Show this baseline as proposed work, not a permission question; follow explicit placement overrides.

- **Create:** suitable editable inputs, including every confirmed required Field; include long text when required or useful, and exclude derived values.
- **List:** a table element bound to a Data Source over the owning Structure, carrying useful short columns drawn from that Data Source's outputs, plus a create trigger element that makes the Create Page reachable. Omit long text by default unless User requests it.
- **Details:** show every new Field, including long text, in a contextual sequence with identity/classification first. For few Fields forming one coherent flow, use one unlabeled group; add named groups only when they improve navigation and current Discovery supports the layout. Do not ask whether to display every Field.

After creating a Structure and its agreed Fields/Relations, inspect Structure detail to discover which Pages exist and which Data Source, Page, View Node, and Navigation affordances apply. Platform-generated default Pages arrive with empty node trees: configure them through their discovered update affordance instead of creating replacements, and reserve Page creation for additional Pages the request needs. A Page's default View holds an array of nodes, and each node type binds data through its own source: a List Page carries one element whose type is a table and whose source data binds to the Data Source code, while Create and Details Pages carry Field elements. Give a table element a stable node code, because the Platform derives that element's data binding from the code and otherwise falls back to a positional binding that shifts when nodes are reordered. Read the exact node and source-data vocabulary from the current Page schema and its examples rather than assuming these property names. Reach the Create Page with a create trigger element on the List or Details Page, or with a Navigation item for it, following whichever current Discovery and existing Metadata already use. Sequence the work as Structure → Fields → Data Source → Nodes, because a node cannot bind a Field that does not exist yet and a node bound to a missing, unauthorized, or read-only Field is silently dropped from the Page's requirements at read time. A Page update replaces the whole View list, so send the complete node tree. Data Sources are not generated: create one when the List Page needs it, and keep its declared outputs covering every Field placed on any Page bound to it, because output is a whole-array replace and an unlisted Field stays invisible. Keep Data Source output and Page node selection as separate decisions, and trim displayed columns by editing nodes rather than by trimming output. Prove each Page by reading it back and confirming its returned requirements list every expected Field, that the List table's Data Source resolves to the owning Structure, and that the Create Page is reachable from the Structure's Pages. The minimum useful set is one field node per required Field on Create, a table element bound to a Data Source on List, and every Field on Details; add no chart, Widget, filter, extra Page, or named group unless the request asks for it. For owned children, configure their lists and parent Navigation through discovered affordances.

Completion: modeling decisions are confirmed, every in-scope Page's default View carries nodes that resolve to usable data and controls, and parent Navigation reaches each in-scope owned-child list.

## Author

1. Use schema-required properties, immutable-property declarations, enum catalogs, examples, and concurrency requirements exactly. For multiple new Fields on one Structure, prefer an available atomic batch-creation affordance from current Structure authoring Discovery. Fetch its linked schema and send the whole group through its discovered method and href; keep different Structures in separate requests. If batch creation is absent or unavailable, use discovered single-Field creation for each Field and track completed writes. A failed batch commits no Fields: correct indexed issues or refresh after a concurrency conflict, then retry only after checking current Workspace state; never switch to singles to bypass a rejected batch. For one new Field, use the discovered single-Field affordance and linked schema. Fetch every payload shape from current Discovery; skill installation alone does not establish platform capability. Never construct authoring routes from memory. Before constructing labels, localized messages, or new codes, follow [Localized text and codes](../horizon/references/authoring-conventions.md). Transfer every file through the Horizon CLI, never raw HTTP: `horizon asset upload` for Business Data Assets, `horizon metadata asset upload --declare` for Metadata Assets. Register a new font or a new GeoJSON only this way: read the Package assets authoring affordance from current Discovery, upload through its href, and build `--declare` only from the domain fields of the schema it names.
2. Keep related Structures, Fields, Pages, Views, Process Definitions, and supporting Metadata in the same Workspace when they form one review outcome.
3. Re-read affected Semantic neighborhood after executable change.
4. Validate Workspace and request its discovered diff/report. Resolve every server-reported issue through its remediation affordance, then validate again; reported issues carry no severity, so treat each one as blocking until current Discovery shows otherwise. `default_nodes_required` on a Page's `views[].nodes.default` means that Page renders nothing, and expect it on every generated default Page from the moment its Structure is created; it clears only once that View carries nodes, so a Workspace with an unresolved `default_nodes_required` is not a completed proposal.
5. Show Attention to User. Leave Attention acknowledgement, approval, and Publication to human decision-makers.
6. Follow [Execution and User testing](../horizon-interview/SKILL.md#execution-and-user-testing): offer manual checks, apply requested adjustments, and revalidate. Submit the completed Workspace only when current Discovery exposes a human-review submission affordance.

Completion: all agreed Metadata changes exist in the selected Workspace, required validation and diff evidence is shown, no server-reported issue remains unresolved including `default_nodes_required` on any in-scope Page, unresolved human Attention is surfaced, and work stops before acknowledgement, approval, or Publication.

## Process Definitions

When authoring or changing a Process Definition:

1. Inspect current Discovery for Package-owned definitions that already express the requested outcome. Read candidate Semantic, declared inputs, behavior, and referenced Structures before choosing reuse or a minimal new definition. Keep only requested behavior supported by current Discovery; report unsupported requirements rather than inventing operations. Definition ownership remains with its Package, not a Structure.
2. Follow live Discovery links for Process Definition authoring, schemas, catalogs, Workspace lifecycle, and validation. Use only the currently exposed operation kinds and declared references. Never copy routes, schemas, payloads, error codes, or catalog values into this skill or infer them from examples elsewhere.
3. For manual launches, configure Structure Action bindings inside the Process Definition through the linked contract: target, stable Action identity, presentation, input mappings, and availability rules. Inspect derived capabilities through current authorization catalogs; binding creation does not grant launch authority. Validate duplicate binding identities and referenced elements. When overlap would be unsafe, follow **Active-execution protection** above.
4. Make edits in a Workspace. Treat the draft as Workspace-scoped: it must remain invisible in Published context until Publication. When current Discovery supports saving an unfinished definition, save its agreed identity first and report it as incomplete. Add valid operations before seeking successful Workspace validation and Publication; an empty draft is saved progress, not an executable process. Never invent a placeholder operation to make a draft appear complete. Validate before requesting human review; resolve broken references or unsupported operation kinds before Publication. Unknown kinds are rejected, not a cue to invent an executable shape. Broken references must fail validation before Publication; stop and report any mismatch between those expectations and live Discovery.
5. Exercise supported behavior through [Test scenarios](#test-scenarios). Discover whether the proposed definition can run in the selected Workspace; otherwise report it untested, never substitute a Real run. Surface the validated diff and hand off to an eligible human to review, approve, and publish. Agents propose and validate; never acknowledge, approve, publish, or approve their own proposal. If review or publication affordances are unavailable, leave the draft intact and tell the User what human action is needed.
6. Treat published releases as immutable. For corrections or removal, make a forward change through a new reviewed release; never rewrite published history. Check current Discovery for Package reference and transport impact before proposing removal.

For ordered conditional work, follow the current composition contracts. Keep operation identities stable while arranging order, declare outputs before referencing them, and validate every dependency and condition before human review. Choose a small linear flow for the requested outcome. Exercise true and false conditions, unavailable dynamic values, and a later failure in Test scope; report which earlier effects remain committed and whether dependent skipped outputs become unavailable. Discover recovery semantics instead of replaying successful work or switching an in-flight definition to a new release.

For query and transformation work, reuse a Data Source whose selection expresses the intended business set. Inspect its declared filters, outputs and supported Relation selection through current Discovery; bind only declared values and verify the fixed Data Scope. Declare the results a later operation needs and use the discovered script input/output convention. Keep scripts focused on transformation, with business effects expressed by explicit supported operations. Read current time and size limits before choosing a workload; use the available count-only selection when only a total is needed.

Exercise representative, empty and failed selections, object and array results, downstream use, and bounded failures in Test scope before human review. Verify a resumed execution uses persisted completed outputs even when upstream Business Data changes. Treat the definition snapshot and referenced Metadata as separate lifecycles: inspect the discovered behavior for changed Data Sources instead of promising that all data is frozen. Treat script and AI-derived HTML as untrusted; require sanitization wherever the proposed surface renders it, and discover host restrictions rather than promising hard memory isolation.

Completion for query and transformation work: selection and downstream contracts validate, relevant Test outcomes and recovery evidence are recorded, and unsupported selection or host capabilities are reported.

For Business Data effects from transformed results, discover the supported mutation and Relation contracts before authoring. Keep the target and delegated effects explicit in the definition, with scripts supplying transformation values. Validate targets, payloads and declared Relation intents through current Discovery; keep primary and secondary ownership, business Constraints and protected platform boundaries intact. Consume the committed Business Instance identity returned by an operation when later work needs that target, and discover its concurrency requirements instead of trusting an identity assembled by a script.

Exercise creation and linking followed by a downstream update in Test scope. Include invalid payloads, undeclared targets or effects, cross-scope attempts, nested creation where supported, and recovery before and after commit. Check that a refused operation leaves no partial Business Instance or Relation Edge, while earlier completed effects remain. Verify automation provenance and initiating business attribution independently. Use discovered recovery within the admitted execution; a fresh start can create another business outcome and does not establish business uniqueness.

Completion for transformed Business Data effects: the declared effects validate, committed identities and intended Relations are verified through authorized outcomes, relevant refusal and recovery cases are recorded, and unsupported effects remain explicit.

For a selected collection whose effects need coordinated progress and recovery within one Process Instance, discover the supported fan-out contract before choosing a sequence. Keep selection separate from iteration effects, declare each item's data context and stable identity through current Discovery, and choose a bounded concurrency and failure policy appropriate to the business outcome. Prefer continuing independent items when partial completion is useful; choose stopping when admitting more items after a failure would be inappropriate. Stopping preserves committed effects and may leave selected membership unfinished.

Exercise fan-out in Test scope with a valid selection, an invalid item, and an empty selection. Verify per-item outcomes, which effects committed, which selected items remain, and what already admitted work finishes after stopping. Change the source selection after execution begins and check that the admitted membership remains stable. Recover failed work through the same execution's current affordance and verify completed effects are not repeated; do not replace its definition snapshot or infer success from acceptance. Discover the Installation's current concurrency bounds and unsupported composition before proposing them.

Completion for coordinated fan-out: selection, sequence and failure policy validate; empty and partial outcomes, fixed membership, bounded progress and recovery evidence are recorded; complete success is claimed only when all selected work has completed under the current contract.

Completion: suitable existing definitions were reused or minimal new definition authored, Workspace validation passed with references intact, supported Test checks and untested behavior are reported, and the human handoff is explicit; stop before approval or Publication.

## Watched Business Data triggers

For automation driven by a Business Data change, settle the business event, owning Structure, watched attributes and qualifying state before authoring. Distinguish a transition into a state from merely remaining in that state: an unrelated edit or a repeated unchanged value should not repeat work. Keep the Process Definition responsible for its business and notification operations.

Read current trigger support, attribute kinds, shared condition language and matching semantics from Discovery. Choose whether a change to one selected attribute is enough or every selected attribute must change in the same Mutation. Keep watched-change selection separate from state conditions. Reject unavailable support rather than approximating an asset, Relation or Expression as a supported scalar attribute. Use declared inputs and target bindings that current validation permits, including the restrictions on deleted Business Instances.

Exercise the proposal explicitly against committed Test transitions through its discovered Workspace affordance. Compare a qualifying transition with an unrelated edit, an unchanged watched value and a condition that fails. For multiple watched attributes, demonstrate a transition satisfying only one selection under both intended matching policies. Record evidence that the original event values govern matching when a later edit occurs before processing, and that retrying the same exercise retains one admitted execution. Shared Test data never implies that every Workspace subscribes to its changes.

Before permitting process-produced changes to feed further automation, inspect the discovered causal safeguard and settle intentional business repetition separately from notification delivery retry. Include a bounded chain scenario and report a stopped chain as a visible failure outcome, preserving earlier committed effects. Keep Real activation with human Publication and verify the resulting durable trigger outcomes through authorized Discovery afterward.

Completion: the intended transition and matching policy validate, supported Test scenarios prove qualifying and nonqualifying events, original-event and retry evidence is recorded, causal stops remain explicit, and the Workspace proposal is ready for human review.

## One-time schedules

For a requested one-time start, discover current scheduling support before authoring. Settle the intended local date, wall clock, explicit timezone, parameters and any bound Business Instance with the User when the request leaves them unclear. Follow the live trigger schema and read the converted instant back through Discovery; verify that it expresses the intended local time. Correct field-specific refusals rather than guessing how daylight-saving gaps or repeated local times should resolve.

Keep the schedule's durable start intent separate from its eventual Process Instance. Discover identity and republication semantics before promising another start; a new release alone is not evidence that previously settled work will repeat. Apply [Active-execution protection](#active-execution-protection) to scheduled parameters whenever equivalent concurrent work could interfere.

Exercise the configuration explicitly in the selected Workspace against suitable Test fixtures through its current exercise affordance. Workspace schedules remain inactive automatically: demonstrate the business result without activating Real work. Include invalid parameters, timezone refusals and a protected-input conflict when relevant. Keep Publication with the eligible human; after their Publication, inspect only the occurrence and execution evidence current Discovery authorizes. Verify System initiation without attributing the start to an invented User or preserving the author's credentials.

Completion: the intended local time and converted instant agree, parameters and any target validate, explicit Test exercise and relevant refusal evidence are recorded, and the proposal remains ready for human review without automatic Real activation.

## Recurring schedules

For a recurring inconsistency or summary alert, use ordinary scheduled selection and notification in a Process Definition. Reuse a suitable Data Source to select the current business set and declare the typed results needed by the message. A later occurrence may intentionally notify the same recipients again: settle this business repeat policy independently from deduplication of delivery retries within one execution. Discover schedule and operation support before proposing configuration; report missing support rather than authoring obsolete Alert Metadata.

For recurring work, settle the business cadence, intended local clock time, timezone and start anchor before authoring. Discover the currently supported recurrence forms and edge policies; clarify how daylight-saving transitions and short months affect the requested intent rather than assuming calendar arithmetic. Verify the saved timezone and next intended occurrence through Discovery, including any default captured from User settings. Treat later User timezone changes as separate from an intentional edit to saved recurrence intent.

Settle missed-work intent explicitly when authoring or changing a schedule: operator review, latest-only catch-up, or omission can have different business effects. Obtain the current supported choices and default from Discovery, and clarify the business decision rather than inferring replay policy from what the process appears to do. Include downtime spanning multiple recurrences in the verification plan, checking preserved intended times, latest-only behavior where chosen, future advancement and active-execution refusals.

Read back the next planned occurrence rather than computing a client-side schedule or creating a speculative queue. Before proposing an edit, inspect its effect on unstarted work, accepted Process Instance snapshots and retained history through the current contract. Exercise the proposal explicitly in the Workspace with Test fixtures and relevant transition/refusal cases; keep Real activation with eligible human Publication.

Completion: discovered cadence and edge behavior match the business intent, saved timezone and next occurrence are verified, relevant Test evidence is recorded, and the effect of edits on existing work is understood before human review.

## Process notifications

When the requested process includes stakeholder messages or lifecycle summaries, discover supported recipients, channels, templates and delivery behavior before authoring. Keep notification recipients separate from Human Interaction responsibility. Include an initiating User only when meaningful; System initiation supplies no fabricated User. Resolve recipients as platform Users, including notification-only Users without login authority.

Bind message content to declared inputs and prior typed outputs. Validate nested dependencies through current schemas and handle unavailable or skipped values explicitly. Choose an explicit selection, transformation or iteration binding for multiple Business Instances before using a scalar value; never assume the first result. Require meaningful subject and body content, escape substitutions, and treat HTML as untrusted. Verify recipient content visibility and safe summary links rather than treating receipt as a Business Data grant.

Select the intended channel and a named email configuration explicitly through Discovery. Installation email settings and protected credentials stay outside Process Definition Metadata and Package publication. Discover administrative settings authority, redact credentials in evidence, and preserve omitted secrets when the current update contract supports it. Multiple available configurations do not justify an arbitrary default.

Validate supported Test recipients and channel restrictions before testing. Keep Workspace checks inside supported in-platform delivery until Discovery exposes safe external test destinations; use controlled provider boundaries for external-delivery verification. Exercise multiple recipients, duplicate resolution, missing values, channel failures, deletion and recovery, recording each outcome separately. Verify retries preserve successful inbox delivery and deleted items, and supplementary failures preserve committed business effects. Report provider acceptance without promising confirmed delivery or exactly-once SMTP dispatch.

Completion: recipient/content/channel contracts validate, relevant safe Test evidence and unsupported checks are recorded, and message receipt, summary participation, business completion and channel delivery remain distinct.

## Human Interaction responsibility and responses

When a process requires a User's decision or typed input, discover supported Human Interaction authoring and assigned-request behavior before choosing an operation. Identify one responsible platform User with usable Authentication and Login Access, the intended response meaning and declared inputs, the necessary contextual Business Instance reference, and where the request should be presented. Keep notification recipients and responsibility distinct; receiving information alone does not establish response authority.

Minimize contextual information and keep linked Business Data access under its own authority. Select response values explicitly rather than inferring approval from a Field name or status update. Discover whether request creation continues independently or an explicit wait is available; model continuation only when supported. Test using eligible Test Users and the authorized Workspace context, verifying assignment, input validation, durable acceptance, authenticated provenance and repeat behavior without adding process or CRUD grants to the responder.

Completion: responsibility, response meaning and placement are supported by current Discovery, safe Test evidence establishes the exact request authority, and notification receipt, Field mutation, response acceptance and process continuation remain distinct.

## Generation and response waiting

When proving a periodic process across generation, recovery, human responses, automatic starts and cleanup, follow [Integrated process proof](references/integrated-process-proof.md).

When a process generates requests before awaiting people, discover the current waiting and result-binding support before authoring. Separate generation, its stakeholder summary, the selected response wait, and final continuation. Bind the wait to the exact requests produced by the intended operation or iteration; a shared business period or contextual status does not define its membership. Choose a process-level aggregate wait when all generation should finish first, or an iteration wait when that item's later work depends on its answer.

Settle the business meaning of completion separately from response acceptance. Read the supported conditions and empty, unavailable and partial-generation outcomes from current Discovery. A received negative decision does not imply approval, and a generation failure must remain visible rather than becoming an all-generated announcement. Preserve committed effects and use discovered recovery within the admitted execution when generation is incomplete.

Exercise an early answer, restart during waiting, concurrent final answers and continuation recovery in the authorized Test context. Verify stable membership, retained early responses, released worker capacity and one final continuation. Include an empty request selection and partial generation under the chosen failure policy. Record generation progress, outstanding responses and final completion as separate evidence.

Completion: exact request selection and response meaning are settled, the discovered composition validates, representative Test evidence proves the separate stages and recovery, and unsupported completion policies remain explicit.

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

## Test scenarios

A new Structure or changed behavior is unvalidated until representative Test Business Instances exercise it, so a test scenario is a normal part of feature validation. Inspect existing Test instances before creating any, reuse a fixture that already represents the case, and create only the missing instances a Relation, Expression, or Action needs. A cosmetic-only change, such as a label or Page layout, needs no new instance when reuse already exercises it. Keep Test data fictional and free of personal or customer data.

1. Select the authorized Workspace through `horizon` and read the effective Metadata Context, supported Test operations, Data Scope selections, and Relation and Action scope rules from current Discovery. Follow the returned affordances; never guess a route, parameter, or capability to find out.
2. For a new Structure, create one representative Test instance, read it back through the runtime contract behind the Details Page, and confirm creation, listing, and the read-back agree. Verify UI behavior through current tooling when it exists, and state plainly that it was not observed when no such tooling exists.
3. Keep the scenario inside supported Test behavior. Discover assignment and recipient eligibility before selecting fixtures; follow **Test User fixtures** below when people participate. Validation never mutates Real Business Instances or treats a fixture reference as authority over their business graph. When a needed Test operation is unsupported or denied, report the reason and stop that check; published Real creation is not a fallback.
4. Exercise what the feature does: feature-relevant Constraints including one meaningful failure case, Relations, Expressions, and the Actions current Discovery reports as available for Test data. Report a refused or unsupported effect as refused and suppressed; never claim an external delivery or notification that did not happen.
5. Keep the fixtures. A Test instance outlives publication and Workspace deletion while its Structure exists, and Structure removal is what deletes it. Inspect current cleanup impact before proposing Structure removal, and route that destructive confirmation or approval to the User through the affordance Discovery exposes; an Agent acknowledges, approves, and publishes nothing.

Test data is one Installation-wide scope shared by concurrent Workspaces, so another Workspace can change the totals a check reads. Report that interference when observed instead of proposing a per-Workspace copy or sandbox.

Record reused and created fixtures with their purpose in Workspace Activity, so later sessions extend the scenario instead of rebuilding it.

### Test User fixtures

A Test User is an ordinary platform User designated for testing, not a sandbox identity or authorization role. Reuse an intentionally designated recipient and discover its current assignment, response and delivery eligibility. If preparation requires User administration that Agent governance withholds, ask an authorized human to prepare the User; do not invent credentials, duplicate identities or broaden grants to make a fixture work. Login needs depend on the interaction, not on the testing designation. When current Discovery permits a Test Business Instance to reference a designated ordinary User, use that narrow reference exception only for the agreed fixture. It grants no Real mutation, graph traversal or cross-scope calculation authority. Discover the available logical initiator override separately; it changes business attribution while preserving the authenticated requester audit. An assigned responder still needs actual usable authentication and current request eligibility; a logical initiator override cannot answer for them. Report unavailable authentication as untested response behavior and ask an eligible human for preparation through current authority.

Confirm recipient intent before using an offered fixture assignment. Exercise both an eligible assignment and a meaningful refusal through supported operations, and inspect related business state for unintended effects. Selection never substitutes for server-side revalidation or independently authorized access to linked Business Data.

If designation or availability changes, rediscover eligibility and report blocked testing. Preserve existing Business Data and prior evidence; remove an obsolete assignment only under the agreed mutation scope and current authority. Never silently delete fixtures, restore eligibility without consent, or substitute an unrelated recipient to complete a check.

Completion: intended recipients and authorized preparation are confirmed, eligible and refused cases are recorded, related business state remains intact, and stale eligibility is reported without identity substitution.

Completion: the report names reused and created fixtures, the checks run and their results, validation failures, and behavior left untested or unsupported, and separates observed runtime facts from suggested manual UI checks.

Completion: Workspace validates, evidence is recorded, unresolved human Attention is surfaced, linked AMTs remain traceable to the Workspace, and the proposal is either submitted through a current review affordance or clearly ready for User-directed continuation.
