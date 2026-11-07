# Prepare a Design Brief

Read for a new Dashboard, Structure header, or an existing design exported for improvement. Apply the Metadata-only boundary in the parent skill throughout collection and generation.

## Select context

1. Record the requested outcome, chosen Installation alias, Metadata Context, export timestamp, and relevant stable Metadata identities/revisions for the provenance footer. Avoid credentials and network addresses. Use an agreed output path, or a local `design-brief.md` under the current project's `.hrz` design directory; avoid overwriting an earlier brief. A design artifact does not trigger the saved implementation-plan workflow.
2. For a full platform Dashboard, which is one Widget, enumerate all authorized business Structures within the requested scope. Follow Metadata listing pagination and detail links until coverage is complete; do not silently select only Structures used by existing Data Sources. Report unavailable or excluded Metadata as coverage limits, never as proof that it does not exist.
3. For a Structure header, include its Fields, Expressions, direct Relations and target identities/meaning. Expand related Structure details only for requested related information or existing dataset dependencies. A Project header that summarizes Contracts needs the relevant Contract Metadata; a Project identity header does not need the entire Installation.
4. For an existing design, identify the Widget and selected usage context. Include all Widgets and placements when the request covers a composed Dashboard. Inspect the complete effective usage set so shared-change impact is visible; the requested placement is not necessarily the only consumer.

Completion: every requested Structure or design component is accounted for, all necessary Metadata pages are read, and inaccessible or intentionally unexpanded context is named.

## Collect Field-first Metadata

For each included Structure, collect discovered identity and meaning; Fields with exact codes, types, requiredness/nullability, static options, relevant constraints, units and formatting; Expressions with declared result types and safe descriptions of meaning; and Relations with direction, cardinality, ownership and target. Mark properties not supplied by Discovery as unknown rather than inferring them from labels. Render every Structure in the same format: one Fields table (code, type/view, label, requiredness, notes), then Expressions, then Relations. Give each enum or multi-select Field its complete option list as a `code → label` table, never codes alone and never a summary or count in place of the list.

Collect relevant existing Data Source declarations as optional reuse context only. Do not collect query limits, pagination, aggregation rules or completeness semantics for the brief; those belong to integration. A new design may use any available Field, not only current outputs.

Read current Widget authoring and presentation catalogs and their linked schemas/examples. Extract only what an offline external agent needs to produce markup, styles, lifecycle JavaScript and mock data that can be moved into a Widget unchanged:

- The deliverable: separate HTML, CSS and JavaScript sources plus mock data, with the dataset names, column names and value types the mock data must use. Do not teach Widget definition declarations (library, asset, size, height or data-contract declaration properties); the integration step derives them.
- The exact JavaScript lifecycle signatures, the context members available to them, the shape of the data delivered, update and disposal behavior, and the rule against fetching or importing remote code.
- Theme tokens, light and dark behavior, and how the design adapts to the width of its container. Do not teach Page layout, group types or placement.
- Libraries: list the bundled libraries and their versions as optional help, with a note that plain HTML, CSS and JavaScript is often the better choice and that using a library is never required. Keep the note short. Do not describe how libraries are declared for the Widget.
- Interaction outputs and host intents only if the request needs them and Discovery states how a Widget emits them; otherwise omit them.
- For headers: exact native navigation marker, reserved instance context, identity/Test presentation, ownership, content height, sticky configuration, native chrome boundaries and failure fallback.

Copy exact executable details into the generated brief only from these current contracts. Do not fill gaps from memory, source-code inspection, or a previously exported brief. If a contract the design truly needs is unavailable, say so briefly in the provenance footer and do not promise a fully compatible implementation.

## Existing-design baseline

Include the current effective HTML, CSS and JavaScript as separate fenced sections, plus data contracts, presentation inputs, interaction outputs, library and asset dependencies, and sanitized selected placement configuration. Include relevant Data Source definitions and their output mappings and Filter bindings. Separate reusable Widget definition from each placement's configuration.

Record Widget identity, Package ownership, revision, context, placement identities and relevant dependency revisions when exposed. List shared usages and unchanged behavior that the requested improvement must preserve. A single reference Widget remains one Widget unless User requests a different composition.

Apply export inspection to every source and configuration section. Discard existing mocks entirely and ask the external agent to create new mock data from the contracts. Mark each sanitized or omitted region with a stable local reference and its reason without retaining the removed value. Preserve a distinction between original source and sanitized export: hashes of exported sections may establish the returned baseline, but cannot prove equality with current platform source. Do not create a second local copy of unsafe original content for this workflow.

If an asset or source section cannot be shared safely, include a dependency description and explain the preview limitation. Do not download asset bytes merely to improve fidelity. The external agent must preserve missing sections through integration instructions, not reconstruct them by guessing.

Completion: every included source section has been inspected, the baseline identifies its context and revision, shared impact is visible, and source omissions are explicitly separated from intended changes.

## Generate the shareable document

Produce one self-contained Markdown Design Brief, with source blocks inside it so the external agent needs neither Core nor skills repository access. Write it as context for a high-quality design, not as a list of limitations. Use these sections, omitting only those marked conditional:

1. **Goal and quality bar:** new Dashboard, new header or improvement, as one Widget. Say that the target is an excellent, polished, professional result, that the agent should propose the best design for the audience and purpose, and that the platform will be enhanced if the design needs something not yet available. For improvements, state the intended changes and the behavior to preserve.
2. **Scope:** the Structures included, and the Structures intentionally left out. One short list, not a revision table.
3. **Available Metadata:** one uniform block per Structure as described in Collect Field-first Metadata, preserving exact schema codes, with Relation context.
4. **How your code runs:** the deliverable and host contract extracted above, with compact safe examples, and the optional-library note. Keep it brief. These are a snapshot, not future API authority.
5. **Existing implementation:** conditional baseline source, placements, dependencies and shared usages.
6. **What to return:** the requested source components and notes, listed below.
7. **Provenance:** a short footer with the Installation alias, Metadata Context, export timestamp, relevant Metadata revisions, sanitization or coverage omissions, and any missing contract. It is for the integration step, and the external agent may ignore it.

Do not write sections for proposed datasets, query limits, unsupported requirements or ready-made fixtures. In **What to return**, ask the external agent to:

- Deliver separate markup, styles and lifecycle JavaScript that follow the host contract, without relying on libraries unless they help.
- Define the datasets the design needs: for each, a name, one row's meaning, and the columns with their types and nullability, derived from the available Metadata. The agent chooses the datasets freely and is not limited to current Data Sources.
- Create the mock data itself for those datasets, as separate content from the rendering code, covering representative multi-row, empty, null, zero and long-label cases. The mock data must be fictional and must not suggest that real data looks like it.
- Keep rendering dependent only on the supplied data and context, never on embedded records, and keep any standalone preview harness separate from production code.
- Check narrow and wide containers, light and dark themes, repeated placements, empty and null data, lifecycle cleanup and relevant header navigation, and report checks actually observed separately from suggested ones.
- List the datasets, columns, inputs, dependencies and calculations the design introduces, and for each calculation say whether it assumes a complete dataset.

For improvements, require preservation of existing contracts and behavior except explicitly requested changes. Identify every added or removed dataset, column, input and output, calculation change and new dependency. Preserve omitted baseline sections as integration requirements; returned placeholders are not replacements for platform content.

## Verify and deliver

Inspect the entire final document, including fenced source blocks and examples, for client Business Data, secrets, live identifiers, unsafe links and copied mocks. Check every claimed capability against collected Discovery evidence, and confirm every enum list is complete. Check requested Metadata coverage and source-section completeness. A scan alone does not prove that a business value is synthetic: verify its provenance.

If inspection finds unsafe content, remove or replace it before delivery; describe omissions without echoing removed content. If uncertainty remains, omit the affected section and note the limitation in the provenance footer. Save only the inspected shareable artifact. Report its path, coverage and unresolved gaps; do not upload, email or send it to an external design service.
