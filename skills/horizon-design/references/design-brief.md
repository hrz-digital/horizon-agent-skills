# Prepare a Design Brief

Read for a new Dashboard, Structure header, or an existing design exported for improvement. Apply the Metadata-only boundary in the parent skill throughout collection and generation.

## Select context

1. Record the requested outcome, chosen Installation alias, Metadata Context, export timestamp, and relevant stable Metadata identities/revisions. Avoid credentials and network addresses. Use an agreed output path, or a local `design-brief.md` under the current project's `.hrz` design directory; avoid overwriting an earlier brief. A design artifact does not trigger the saved implementation-plan workflow.
2. For a full platform Dashboard, enumerate all authorized business Structures within the requested scope. Follow Metadata listing pagination and detail links until coverage is complete; do not silently select only Structures used by existing Data Sources. Report unavailable or excluded Metadata as coverage limits, never as proof that it does not exist.
3. For a Structure header, include its Fields, Expressions, direct Relations and target identities/meaning. Expand related Structure details only for requested related information or existing dataset dependencies. A Project header that summarizes Contracts needs the relevant Contract Metadata; a Project identity header does not need the entire Installation.
4. For an existing design, identify the Widget and selected usage context. Include all Widgets and placements when the request covers a composed Dashboard. Inspect the complete effective usage set so shared-change impact is visible; the requested placement is not necessarily the only consumer.

Completion: every requested Structure or design component is accounted for, all necessary Metadata pages are read, and inaccessible or intentionally unexpanded context is named.

## Collect Field-first Metadata

For each included Structure, collect discovered identity and meaning; Fields with exact codes, types, requiredness/nullability, static options, relevant constraints, units and formatting; Expressions with declared result types and safe descriptions of meaning; and Relations with direction, cardinality, ownership and target. Mark properties not supplied by Discovery as unknown rather than inferring them from labels.

Collect relevant existing Data Source declarations, Filters, outputs, grain and completeness semantics as optional reuse context. A new design may request any available Field that current authoring supports exposing, not only current outputs. Distinguish a Field available on a Structure from a proven supported Relation traversal or derived result.

Read current Widget authoring and presentation catalogs and their linked schemas/examples. Extract only the contracts needed to teach an offline external agent:

- Definition components, presentation inputs, localization, data contracts, mapping direction and compatibility rules.
- Exact JavaScript lifecycle signatures, context members, data/result envelopes, updates, disposal and refresh behavior.
- HTML/CSS placement rules, scoping, theme tokens, sizing and responsive behavior.
- Approved library versions/modules and lifecycle guidance; asset declarations and availability without copying asset bytes or download links.
- Declared interaction outputs and host intent contracts.
- For headers: exact native navigation marker, reserved instance context, identity/Test presentation, ownership, content height, sticky configuration, dataset selector rules, native chrome boundaries and failure fallback.
- Preview mocks versus bound/live results, including required/optional dataset rules and Published behavior.

Copy exact executable details into the generated brief only from these current contracts. Do not fill gaps from memory, source-code inspection, or a previously exported brief. If a necessary contract is unavailable, label that part unsupported/unverified and explain what the integrating agent must obtain; do not promise a fully compatible implementation.

## Existing-design baseline

Include the current effective HTML, CSS and JavaScript as separate fenced sections, plus data contracts, presentation inputs, interaction outputs, library/asset declarations, layout defaults, and sanitized selected placement configuration. Include relevant Data Source definitions and their output mappings and Filter bindings. Separate reusable Widget definition from each placement's configuration.

Record Widget identity, Package ownership, revision, context, placement identities and relevant dependency revisions when exposed. List shared usages and unchanged behavior that the requested improvement must preserve. A single reference Widget remains one Widget unless User requests a different composition.

Apply export inspection to every source and configuration section. Discard existing mocks entirely and generate new fictional fixtures from the contracts. Mark each sanitized or omitted region with a stable local reference and its reason without retaining the removed value. Preserve a distinction between original source and sanitized export: hashes of exported sections may establish the returned baseline, but cannot prove equality with current platform source. Do not create a second local copy of unsafe original content for this workflow.

If an asset or source section cannot be shared safely, include a dependency description and explain the preview limitation. Do not download asset bytes merely to improve fidelity. The external agent must preserve missing sections through integration instructions, not reconstruct them by guessing.

Completion: every included source section has been inspected, the baseline identifies its context and revision, shared impact is visible, and source omissions are explicitly separated from intended changes.

## Generate the shareable document

Produce one self-contained Markdown Design Brief, with source blocks inside it so the external agent needs neither Core nor skills repository access. Use these sections, omitting only those marked conditional:

1. **Goal and scope:** new Dashboard, new header or improvement; intended changes and behavior to preserve.
2. **Snapshot and coverage:** context, timestamp, identities/revisions, included Structures, exclusions and unavailable evidence.
3. **Available Metadata:** Field-first tables and Relation context, preserving exact schema codes.
4. **Design Guide:** current discovered rendering, styling, lifecycle, library, interaction and header contracts with compact safe examples. These are a snapshot, not future API authority.
5. **Existing implementation:** conditional baseline source, placements, dependencies and shared usages.
6. **Data requirements:** for each proposed dataset, consumers, row grain, source Fields/Relations, types/nullability, units, Filters, sorting, completeness, calculation location and unsupported requirements. Separate existing bindings from proposals. Use multiple named datasets where grains or query contexts differ; do not force one Data Source per card.
7. **Synthetic fixtures:** independently invented examples matching declared types, including empty, null, zero, long-label and representative multi-row cases. Mock schemas may include unimplemented proposed outputs only when clearly labeled. Keep fixture loading separate from rendering and never treat a fixture as evidence of live query completeness.
8. **Return instructions:** requested source components, contract changes, checks and integration notes.
9. **Omissions and readiness:** sanitization/coverage limitations and unresolved capability gaps; state whether the brief is sufficient for the requested design.

In the return instructions, require separate markup, styles and lifecycle JavaScript using the discovered host contract, plus input/data/output declarations, dependencies, synthetic fixtures, and a change list. A standalone preview harness must use the same exported source and remain separate from production code. Keep rendering dependent on supplied context, not embedded records. Require narrow/wide containers, light/dark themes, multiple placements, empty/null data, lifecycle cleanup and relevant header navigation checks; report checks actually observed separately from suggested checks.

For improvements, require preservation of existing contracts and behavior except explicitly requested changes. Identify every added or removed dataset/column/input/output, calculation change and new dependency. Preserve omitted baseline sections as integration requirements; returned placeholders are not replacements for platform content.

## Verify and deliver

Inspect the entire final document, including fenced source and fixture blocks, for client Business Data, secrets, live identifiers, unsafe links and copied mocks. Check every dataset example against its declared schema and every claimed capability against collected Discovery evidence. Check requested Metadata coverage and source-section completeness. A scan alone does not prove that a business value is synthetic: verify its provenance.

If inspection finds unsafe content, remove or replace it before delivery; describe omissions without echoing removed content. If uncertainty remains, omit the affected section and clearly downgrade readiness. Save only the inspected shareable artifact. Report its path, coverage and unresolved gaps; do not upload, email or send it to an external design service.
