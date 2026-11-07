# Prepare a Design Brief

Read for a new Dashboard, Structure header, or an existing design exported for improvement. Apply the Metadata-only boundary in the parent skill throughout collection and generation.

## Select context

1. Record the requested outcome, chosen Installation alias (the label of the selected Connection Profile), Metadata Context, export timestamp, and relevant stable Metadata identities/revisions for the provenance footer. Avoid credentials and network addresses. Use an agreed output path, or a local `design-brief-rev<N>.md` under the current project's `.hrz` design directory, in a folder named for the design. Start at `design-brief-rev1.md`; for each new brief in that folder use the next revision number, and never overwrite an earlier revision. A design artifact does not trigger the saved implementation-plan workflow.
2. For a full platform Dashboard, which is one Widget, enumerate all authorized business Structures within the requested scope. Follow Metadata listing pagination and detail links until coverage is complete; do not silently select only Structures used by existing Data Sources. Report unavailable or excluded Metadata as coverage limits, never as proof that it does not exist.
3. For a Structure header, include its Fields, Expressions, direct Relations and target identities/meaning. Expand related Structure details only for requested related information. A Project header that summarizes Contracts needs the relevant Contract Metadata; a Project identity header does not need the entire Installation.
4. For an existing design, identify the Widget and selected usage context. Include all Widgets and placements when the request covers a composed Dashboard. Inspect the complete effective usage set so shared-change impact is visible; the requested placement is not necessarily the only consumer.

Completion: every requested Structure or design component is accounted for, all necessary Metadata pages are read, and inaccessible or intentionally unexpanded context is named.

## Collect Field-first Metadata

For each included Structure, collect discovered identity and meaning; Fields with exact codes, types, requiredness/nullability, static options, relevant constraints, units and formatting; Expressions with declared result types and safe descriptions of meaning; and Relations with direction, cardinality, ownership and target. Mark properties not supplied by Discovery as unknown rather than inferring them from labels. Metadata revisions are recorded per Structure; no single Installation revision is needed. Render every Structure in the same format: one Fields table (code, type/view, label, requiredness, notes), then Expressions, then Relations. Give each enum or multi-select Field its complete option list as a table of option code and label, plus a Color column and an Icon column whenever any option of that Field carries one, filled from every option and never from a sample. Never state that options have no colors or icons without checking every option of every Field. Never use a summary or count in place of the list.

The external agent creates no datasets and uses none, so do not collect Data Source declarations, outputs, query affordances or dataset capabilities for the brief. It only generates mock data. A new design may use any available Field.

Read current Widget authoring and presentation catalogs and their linked schemas/examples. Extract only what an offline external agent needs to produce markup, styles, lifecycle JavaScript and mock data that can be moved into a Widget unchanged:

- The deliverable: separate HTML, CSS and JavaScript sources plus mock data shaped as named collections of rows, whose column names the agent chooses from the data model and whose values use the value types the platform supports. Do not teach Widget definition declarations (library, asset, size, height or data-contract declaration properties); the integration step derives them.
- The exact JavaScript lifecycle signatures, the context members available to them, the shape of the data delivered, update and disposal behavior, and the rule against fetching or importing remote code.
- Theme tokens, light and dark behavior, and how the design adapts to the width of its container. Do not teach Page layout, group types or placement.
- Libraries: list the bundled libraries and their versions as optional help, with a note that plain HTML, CSS and JavaScript is often the better choice and that using a library is never required. Keep the note short. Do not describe how libraries are declared for the Widget.
- Typography: read the font media types from the Package assets link that the authoring section of Discovery advertises for a Package, and use it only through that link. When that contract supports fonts, tell the external agent that custom fonts are welcome for better layouts and design, without explaining how a font is attached to a Widget. State the font media types Discovery lists as supported and say the best-supported format works best for us; do not name a format from memory. Ask for free fonts under open licenses that allow embedding and redistribution, and tell the agent not to rely on proprietary or paid fonts. Mention that omitting a custom font inherits the platform default typography, so a font is never required.
- Interaction outputs and host intents only if Discovery states how a Widget emits them; otherwise leave them out of the brief.
- For headers: exact native navigation marker, reserved instance context, identity/Test presentation, ownership, content height, sticky configuration, native chrome boundaries and failure fallback.

Copy exact executable details into the generated brief only from these current contracts. Do not fill gaps from memory, source-code inspection, or a previously exported brief. State only what Discovery states and leave out what it does not: the brief never lists missing, undefined or unsupported items.

## Existing-design baseline

Include the current effective HTML, CSS and JavaScript as separate fenced sections, plus data contracts, presentation inputs, interaction outputs, library and asset dependencies, and sanitized selected placement configuration. Include relevant Data Source definitions and their output mappings and Filter bindings. Separate reusable Widget definition from each placement's configuration.

Record Widget identity, Package ownership, revision, context, placement identities and relevant dependency revisions when exposed. List shared usages and unchanged behavior that the requested improvement must preserve. A single reference Widget remains one Widget unless User requests a different composition.

Apply export inspection to every source and configuration section. Discard existing mocks entirely and ask the external agent to create new mock data from the contracts. Mark each sanitized or omitted region with a stable local reference and its reason without retaining the removed value. Preserve a distinction between original source and sanitized export: hashes of exported sections may establish the returned baseline, but cannot prove equality with current platform source. Do not create a second local copy of unsafe original content for this workflow.

If an asset or source section cannot be shared safely, include a dependency description and explain the preview limitation. Do not download asset bytes merely to improve fidelity. The external agent must preserve missing sections through integration instructions, not reconstruct them by guessing.

Completion: every included source section has been inspected, the baseline identifies its context and revision, shared impact is visible, and source omissions are explicitly separated from intended changes.

## Describe, never invent

The brief starts a Design Session: describe today's reality precisely and bring the open questions to the surface so the external agent does not have to discover them. Take every code, label, type, option and relation exactly from Metadata. Never guess a business meaning. Write meaning that User has confirmed as plain statements, and everything else as an open question with a default the agent may assume. Word a default as an assumption ("assume as stated in Metadata"), never as "confirmed", unless User confirmed it. Never phrase the data model or the platform contract as a reason to make the design smaller.

Facts that are not Metadata and must not be read from Business Data:

- **Record counts (required):** if a count cannot be read, stop, report a tooling error to User, and do not deliver the brief with counts missing. Read the total per included Structure through the query affordance advertised in that Structure's detail, in the entry for its data source, one explicit request per Structure with its own discovered path and no shell loop. Use a page window beyond the data so the response carries no records (a page number far beyond the data, in the request body, with the total in `pagination.totalItems`), take the number from the total in the response's pagination data, and record only that number with its date. If the response does not show where the total is, inspect only the keys other than the record list. Ask User for the expected size in a year, or mark it as an estimate to agree together. Counts are the only Business Data allowed in a brief. Report a zero count as zero, and note that the mock data is then the only picture of that Structure. Dashboards are usually designed before a new client has any Business Instances. When the counts are zero or show that the client has not started using the platform, say so plainly in the Goal section: this is a new client, no real volumes exist yet, and the expected number of records per Structure will be estimated together with User. Put the expected volumes in the open questions as estimates to agree, with a reasonable default, to be agreed together. When counts are non-zero, state them as today's size and still ask for the expected size in a year.
- **Business rules and the revenue or cost meaning and period of money fields:** ask User or raise an open question.
- **Scope:** one brief designs one dashboard. Take its scope from User's request, for example follow-up of one Structure and nothing about another, and state it as the Scope. Do not guess scope or intent, and do not invent an audience, roles, questions or priorities: they are defined with User in the Design Session agreement.
- **Locale:** take currency, default locale and timezone from the Installation's discovered setup. If the language variant (for example `pt-BR` versus `pt-PT`) is not stated, say what is stated, state your assumption and list it as an open question. Never write a bare language code as the whole answer.

## Run the metadata checks

The procedure is one ordered pass: Describe, never invent; collect Metadata and platform facts; run these checks; generate the brief; then verify and deliver. Run these checks on the collected Metadata. Every hit about the meaning of Metadata becomes an open question. Include only what exists: the brief shares the current Metadata and how to work with it, and never lists items that are missing or do not exist.

1. **Lifecycle fields:** when a Structure has more than one status-like enum, ask how they relate, which combinations are valid, and which values count as open, active, won, lost and closed. The default mapping must cover every value of every such enum, including values that fit more than one state, so that no stage or status is left without a meaning.
2. **Final states:** for every status enum, ask whether its final option separates success from failure and whether a reason is recorded.
3. **Time series date:** when a Structure has several dates, list them and say that each is valid for a different purpose; which one a chart uses is decided in the Design Session agreement.
4. **Money semantics:** for each currency field, revenue or cost, and one-time, monthly or yearly. Metadata rarely says which, so never call a field revenue or cost, or monthly, without Metadata or User saying so; otherwise state it as an assumption. When several Structures hold related amounts (for example a contract value, a project cost and an invoice amount), ask how they relate and which source is authoritative for contracted, billed and received, so the same money is not counted twice. Check every Expression for assumptions not stated in field notes and ask for confirmation.
5. **Optional enums:** state how an unset value arrives in a grouped row and which label to show.
6. **Computable defaults:** every default you give for an open question, and every rule you state, must be computable from Fields, Expressions and system fields that exist today. If it is not, rewrite it so it is, or leave the default out. A default expressed as a multiple of today's counts, such as twice the current volume, is computable and allowed.
7. **Contradictions:** compare the statements in the platform contract with each other and with the data model, for example a timezone, a rounding, a date format or a capability stated two ways. Resolve each contradiction from Discovery, or list it as an open question. Do not try to reconcile the audience questions with business defaults inside the brief: such differences are settled with User in the Design Session agreement.

## Collect platform facts

Request only links and paths that Discovery advertises, copied exactly. If a fact cannot be reached through an advertised link, leave it out of the brief; never try a guessed route to look for it, because any error stops the run.

Collect these from current Discovery and include only what Discovery states. Leave out what it does not state: do not mention missing, undefined or unsupported items in the brief. Never fill a gap from memory or from an earlier brief: build every brief from fresh reads, and read earlier revisions only to choose the next revision number. A brief thinner than this list is expected when Discovery states less.

- **System fields and history:** state that every Business Instance has `created_at`, `created_by`, `updated_at` and `updated_by`, and add whatever else Discovery exposes about system fields, their types and any change history. Never state or imply that system fields do not exist, and never propose a new field for what a system field already provides.
- **Option colors and icons:** the option tables already carry the colors and icons Metadata defines; state whether a Widget can use them only if Discovery says so.
- **Icons:** the icon codes in Metadata, such as those on enum options, are Iconify codes in the form `prefix:name`, for example `mdi:cancel`. Tell the agent they only name which icon Metadata means. A Widget has no platform icon component, so say plainly that the agent should deliver every icon it needs as inline SVG inside its own markup, matching the Metadata icon where it wants to mirror it, and may use any other open-licensed icon set. Never imply that a Widget can render an icon from its code at runtime unless Discovery says so.
- **Value formats on the wire:** for `date`, `datetime`, `month`, currency numbers, `boolean` and `null` group keys.
- **Lifecycle:** whether `mount` may be async, what `update` receives and when it is called, refresh cadence, and whether inputs can change while mounted.
- **Rendering environment:** shadow or regular DOM, style and identifier isolation between instances, container height behavior, pixel ranges for narrow, medium and wide, and how a theme change is signalled to canvas-based content.
- **Libraries and fonts:** the shape of the libraries argument as used inside the lifecycle functions, and how a Widget refers to a font file as far as Discovery says. Declaring libraries and fonts on the Widget is handled at integration.
- **Interaction:** whether a Widget can emit filters, drill-through or navigation, and how. Internal interactions (tabs, period selectors, tooltips) are allowed.
- **Accessibility:** a target level and expectations for focus, reduced motion and chart alternatives when Discovery or User states them.

## Generate the shareable document

Produce one self-contained Markdown Design Brief in English, with source blocks inside it so the external agent needs neither Core nor skills repository access. Keep user-facing labels in the Installation's language, exactly as Metadata has them. Use these sections in this order; adapt the audience questions for headers and improvements. For an existing design, add an **Existing implementation** section after the data model with the baseline source, placements, dependencies and shared usages:

1. **Goal and quality bar:** new Dashboard, new header or improvement, as one Widget. Include this sentence adapted to the design: "Aim for an excellent, polished, professional result. Nothing in this brief limits the design. The data model and the platform contract describe what exists today. Gaps are expected: record them in the gap register rather than designing around them." Do not state an audience, roles, the questions the dashboard must answer or their priority, and do not guess what User wants: the brief shares the current Metadata and how to work with it, and the Design Session agreement with User defines the rest. Say that in the Goal. Include visual direction (brand, colors, density, tone), the light and dark values of the theme tokens, or expected presentation inputs only when User or Discovery gave them. State the scope exactly as User defined it. For improvements, state intended changes and behavior to preserve.
2. **Language and locale:** language variant, currency code, number format, date format and how months are written, and the timezone that decides "today", "this month", "overdue" and "expired" with where the Widget gets "today".
3. **Scope:** the Structures included and the Structures intentionally left out with the reason; ownership stated once.
4. **System fields:** state that every Business Instance has `created_at`, `created_by`, `updated_at` and `updated_by`, plus the other system fields and change history that Discovery exposes, with their types.
5. **Data model:** one uniform block per Structure as described in Collect Field-first Metadata. Also give each Structure its record count (read as described above, plus User's expected size in a year when given), mark every Structure that describes real people and suggest favouring counts and trends over lists of personal details, include option colors and icons of enums when Metadata has them (otherwise say whether the agent chooses), give the scale of every rating field, note inconsistent formats in Metadata values such as colors with and without an alpha channel and ask whether they are intentional, and state that grouping by a multi-value field counts a record more than once. Describe Relations to out-of-scope Structures and what the agent may still show. Keep labels with typos, stray spaces or very long text verbatim and add a note.
6. **Business rules and open questions:** confirmed rules as statements, then a table of open questions with columns ID, Question, Why it matters and Default to assume.
7. **Platform contract as of today:** say that changes to it are proposed through the gap register, and that they describe how the code plugs into the platform, not what the design may show. Include the deliverable and host contract extracted for the offline agent (separate markup, styles and JavaScript, `mount` / `update` / `cleanup` as discovered, container-only DOM, no network, null as an explicit empty marker, group keys as codes not labels, theme tokens with fallbacks, container-based sizing), the optional-library note with pinned versions, the typography note, and everything collected under Collect platform facts.
8. **What to return:** see below.
9. **Design Session and agreement:** copy it from [Design Session section](design-session.md).
10. **Provenance:** a footer with the Installation alias, Metadata Context, export timestamp, relevant Metadata revisions and sanitization or coverage omissions. It is for the integration step, and the external agent may ignore it.

Ask the external agent, under **What to return**, to:

- Work in two steps. First deliver one self-contained `preview.html` (markup, styles, script and mock data inline) so we can approve the layout together. When we agree on it, generate the platform files below and include `preview.html` in the folder.
- Return the design as a folder with these files, so we can move it into the platform as it is: `widget.html` (markup), `widget.css` (styles), `widget.js` (lifecycle JavaScript following the host contract, without relying on libraries unless they help), `mock-data.json`, `gap-register.md`, `fonts/` when fonts are used, and a short `README.md` listing the fonts, icons, libraries and calculations.
- Deliver the gap register with the first revision.
- Return mock data; we derive the datasets from it at integration. The mock data is one object whose keys name collections and whose values are arrays of row objects, the shape the JavaScript receives as `data`. Choose the collections and columns the design needs from the data model, using the supported value types and marking nullability. A column or collection the design needs that does not exist in the data model yet may be included and is marked `proposed`; all others are `available`. State for each calculated value whether the Widget computes it from the rows.
- Keep the mock data as separate content from the rendering code, covering representative multi-row, empty, null, zero and long-label cases. The mock data must be fictional and must not suggest that real data looks like it. Include the proposed columns so the preview shows the target design.
- Give every proposed item the fallback the design uses if it is rejected, already designed and shown in the preview, for example through a mock-data switch.
- If custom fonts are used, list every one: family, weights, styles, character coverage, license and source, and supply the font files in the supported format so we can add them. Include only the fonts the design uses.
- Let rendering depend on the supplied data and context rather than on embedded records, and keep any standalone preview harness separate from production code.
- If icons are used, list each icon, its source set and license, and the Metadata icon code it mirrors when it does; the icons themselves are inline SVG in the markup.
- Check narrow and wide containers, light and dark themes, repeated placements, empty and null data, lifecycle cleanup and relevant header navigation, and report checks actually observed separately from suggested ones.
- List the mock data collections and columns, inputs, dependencies and calculations the design introduces.

For improvements, require preservation of existing contracts and behavior except explicitly requested changes. Identify every added or removed mock data collection, column, input and output, calculation change and new dependency. Preserve omitted baseline sections as integration requirements; returned placeholders are not replacements for platform content.

## Verify and deliver

Inspect the entire final document, including fenced source blocks and examples, for client Business Data, secrets, live identifiers, unsafe links and copied mocks. Check every claimed capability against collected Discovery evidence, and confirm every enum list is complete. Check requested Metadata coverage and source-section completeness. A scan alone does not prove that a business value is synthetic: verify its provenance.

If inspection finds unsafe content, remove or replace it before delivery; describe omissions without echoing removed content. If uncertainty remains, omit the affected section and note the limitation in the provenance footer. Save only the inspected shareable artifact. Report its path, coverage and unresolved gaps; do not upload, email or send it to an external design service.

Before delivery, confirm each item and fix the brief or turn the item into an open question when one fails:

- Every code, label and option matches Metadata exactly, every enum list is complete, and every color and icon an option carries is shown.
- Language variant, currency, formats and timezone are explicit.
- System fields are stated as User and Discovery describe them, never as absent.
- Each Structure has its record count, with the date it was read, and no other Business Data was retained.
- Each currency field says revenue or cost and its period, or has an open question.
- Each rating field has a scale or an open question.
- Every metadata check ran and each hit about the meaning of Metadata is an open question, including the computable-defaults and contradiction checks.
- The brief states no audience, roles, questions or priorities of its own.
- Every status value has a meaning, and related money fields say which source is authoritative.
- Every record count was read, or the work was stopped with a tooling error.
- The usability of option colors and icons is stated only if Discovery says so.
- Every open question has a default the agent may assume.
- Every platform fact above is stated only if Discovery states it, and no missing, undefined or unsupported item is listed.
- The Design Session section is included and the quality-bar sentence about gaps is present.
- Nothing tells the agent to reduce the design because of today's data.
- The brief contains no real business data, personal data, links or credentials.
