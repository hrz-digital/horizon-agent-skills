# Changelog

## v1.4.1

### Changed

- Made a non-empty Create/List/Details Page set the required end state for every new Structure. A Page whose `default` View carries no nodes is unfinished work, generated default Pages are configured through their update affordance instead of recreated, and Visualization no longer settles as `out of scope (no configuration needed)` for a new Structure.
- Added the authoring sequence Structure → Fields → Data Source → Nodes, the whole-View-list replacement rule for Page updates, the Data Source output coverage rule, and Page read-back proof through returned requirements, with a minimum useful node set that excludes unrequested charts, Widgets, filters, extra Pages, and named groups.
- Specified what a usable List Page carries: one table element bound to a Data Source over the owning Structure, with a stable node code because the Platform otherwise derives a positional data binding that shifts when nodes are reordered, plus a create trigger or Navigation item that keeps the Create Page reachable. Create trigger absence was never a validation error, so an unreachable Create Page previously passed unnoticed.
- Show a clarification round only when the agent actually holds a question; otherwise go straight to the Plan summary, which already carries all three layers, and wait for approval before any mutation. Stated in the skill intro, the Default planning gate, the interview steps, and the response shape, with the interview template marked as the reply's structure rather than a literal code fence.
- Treat every server-reported Workspace issue as blocking, since reported issues carry no severity. `default_nodes_required` is named as the signal that a generated Page renders nothing, expected from Structure creation until configured, and a Workspace with it unresolved is not a completed proposal.

## v1.4.0

### Added

- Added three-layer Metadata planning and authoring guidance: Data Modeling → Visualization → Automation, with Discovery-grounded relationship mapping, Page placement defaults, and agreed `no configuration needed` outcomes.
- Added per-Structure Create/List/Details placement recommendations and a consistent three-layer interview response format with one decision and grounded recommendation per question.
- Added reviewable plan summaries, execution complexity/session advice, approved-plan lookup by "implement plan" / "Executar o plano", and resume from recorded Workspace progress without requiring the plan path.
- Added user-invoked skill-set usage guidance explaining planning, approval, fresh-session handoff, and implementation.

### Changed

- Select Installation and inspect Discovery before asking questions already answered by existing Metadata; recheck Discovery between interview rounds. Interview only for unresolved decisions or substantial execution; written plans depend on execution workload or handoff risk.
- Clarified Primary/Secondary Structures, owned/reference Relations, User-linked person Fields, required Create inputs, and long-text defaults (allowed on Create, excluded from List unless requested). New Structures get usable default Pages and owned-child navigation as baseline work.
- Show checked Installations as numbered name/URL/status choices; follow authoring hrefs verbatim and stop all requests on any HTTP error or CLI failure.
- Read default language and currency through the linked Platform Setup instead of guessing values or asking for the default currency.

## v1.3.1

### Added

- Added `authoring-conventions` reference for Metadata authoring: resolve `defaultLocale` from current Discovery Platform Setup, supply required default-locale text, add PT/ES/EN translations only when meaning is known and never invent uncertain translations, and prefer `snake_case` for new authored codes while preserving existing identifiers and contract-defined spellings.

## v1.3.0

### Added

- Added `horizon-interview` for planning unclear, complex, bulk, relational, destructive, or cross-surface work before execution.
- Added local redacted plans at `.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md` with explicit approval gates and purge guidance.
- Added Business Data mutation confirmation and scope-change reapproval rules.

### Changed

- Updated Horizon routing and authoring/runtime skills to require approved plans for complex work.


## v1.2.2

### Added

- Added error-reporting rule to `horizon` bootstrap: the normal scenario has no errors; agents report error status and message back to the user as-is and stop for the user to treat it, never retrying with workarounds, guessed variants, or silent fallbacks.

## v1.2.1

### Added

- Added Horizon CLI file-transfer rule to `horizon-metadata-authoring`: every file moves through the CLI, never raw HTTP (`horizon asset upload` for Business Data Assets, `horizon metadata asset upload --declare` for Metadata Assets). Registering a new font or GeoJSON goes through the Package assets authoring affordance from current Discovery, with `--declare` built from the domain fields of the schema it names. Added `package-asset-upload-journey` black-box scenario.

### Changed

- Removed contract field names from the Widget font guidance: agents verify font descriptors, attribution, and CSS bindings from the discovered asset contract instead of named fields. Skills carry workflow policy only; every route, schema, field, and payload shape comes from current Discovery.

## v1.2.0

### Added

- Added complete Widget workflow to `horizon-metadata-authoring`: reuse-first discovery, library selection through Semantic `when`/`notWhen` with installed bindings, named dataset binding with explicit mappings, standalone mock versus live Node-context preview, local geographic and font assets with platform-default-first typography, shared-identity usage inspection and repair, layout default inheritance with Visibility-tab mobile exclusion, trusted main-realm governance, and the human acknowledgement, approval, and Publication boundary.
- Added `widget-authoring-journey` black-box scenario covering Widget reuse, binding, preview, usage repair, and review handoff.

## v1.1.0

### Added

- Added read-only `horizon-ask-for-guidance` support for Horizon Metadata architecture decisions.
- Added guidance for choosing Fields, Structures, owned Relations, reference Relations, and platform Users.
- Added Installation-specific explanations of configured Structures, Fields, Relations, Constraints, Actions, lifecycle rules, and authorization.
- Added Semantic engine guidance with executable Metadata as authoritative source.
- Added explicit evidence, uncertainty, human-gate, and safe-next-step requirements.
- Added Horizon CLI update checks and setup/update guidance.

### Changed

- Clarified that guidance remains read-only and routes Metadata or runtime mutations to dedicated Skills.
- Release titles now use the version tag directly, such as `v1.1.0`.
