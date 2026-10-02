# Changelog

## v1.5.0 (Unreleased)

### Added
- Added Discovery-grounded Workspace process-exercise guidance: effective-definition and eligible-participant discovery, explicit Test-scope runs without fallback, logical-initiator selection with retained requester provenance, contained delivery and Workspace-gated requests, explicit-only automation, and failure and refusal reporting with restart and retry confirmation.
- Added Discovery-grounded cancellation guidance: administrative privilege discovery and stable refusals, confirmed intent before stopping queued work or invalidating pending requests, honest stopping versus finished reporting, retained committed effects, persistence across restart, and no replacement execution for deliberately stopped work.
- Added Discovery-grounded Test User fixture guidance for intentional recipients, authorized human preparation, meaningful refusals, unchanged business authority and safe recovery after eligibility changes.
- Added Discovery-grounded request reassignment and deadline-recovery guidance: confirm administrative intent and replacement eligibility, preserve current-assignee privacy and durable race winners, and distinguish overdue work and explicit non-response outcomes from User answers or approval.
- Added Discovery-grounded guidance and scenarios for exact response-wait membership, separate generation and completion evidence, early answers, restart and concurrent continuation checks, and explicit empty or partial-generation outcomes.
- Added Discovery-grounded Human Interaction guidance for explicit responsibility and response meaning, assigned request authority, authenticated responder/Agent provenance, safe contextual access, durable acceptance, and retry versus stale-response recovery.
- Added Discovery-grounded process notification guidance for recipient/content bindings, explicit email configuration, safe Test checks, independent channel outcomes, recipient-owned inbox recovery, and honest provider acceptance.
- Added Discovery-grounded guidance and scenarios for coordinated fan-out: bounded iteration work, continue or stop intent, stable admitted selection, explicit empty and partial outcomes, retained committed effects, and same-instance recovery without repeating completed work.
- Added Discovery-grounded guidance and scenarios for transformed Business Data effects, declared target authority, committed identities, Relation ownership and nested creation, contained refusals, durable recovery, and independent automation attribution.
- Added Discovery-grounded guidance for Process Data Source selection and bounded transformations, declared downstream results, empty and failed selections, persisted-output recovery, referenced Metadata changes, and untrusted HTML.
- Added Discovery-grounded guidance for ordered conditional Process Definitions, declared prior outputs, skipped dependencies, partial commits, and durable recovery.
- Added guidance and scenarios for independent Action starts over an explicit selection: bounded dispatch, partial acceptance, progress tracking, stopping remaining dispatch, transport uncertainty, and coordinated fan-out intent.
- Added Discovery-grounded guidance for selecting active-execution protection inputs, respecting admission conflicts, and distinguishing operation recovery from new starts and permanent business uniqueness.

### Changed
- Process inspection now distinguishes generated requests, outstanding human responses and final completion, preserving accepted answers and the admitted execution during recovery.
- Completed Discovery-grounded Process Definition routing, reuse and authoring, definition-owned Action bindings, direct-run retry safety, and execution provenance guidance. Added scenarios for authoring, execution, delegation, protection, and missing or unavailable support.
- Runtime guidance covers authorized Process Instance summaries, delegated oversight limits, context containment, linked Business Data authority, and durable refresh after missed live notices.
- Runtime guidance covers process-backed Action delegation, server-bound inputs, accepted versus completed work, and ambiguous-start retry safety using current Discovery.
- Synced `VERSION` and every skill's metadata version to `1.5.0`.

## v1.4.0

### Added
- Added three-layer Metadata planning guidance (Data Modeling → Visualization → Automation), Discovery-grounded relationship mapping, Page placement defaults, and explicit `no configuration needed` outcomes.
- Added per-Structure Create/List/Details placement recommendations, reviewable plan summaries, execution/session guidance, approved-plan lookup and resume, and skill-set usage guidance for approval and handoff.
- Added Discovery-grounded Test scenario validation: reuse suitable Test instances, create only minimal missing fixtures, cover runtime behavior and capability limits, and keep Real Business Instances read-only. Documented fixture lifetime and shared Installation-wide scope.

### Changed
- Clarified interview gates: inspect Discovery before asking questions, recheck between rounds, ask only unresolved decisions, and proceed to plan summary when no clarification is needed. Plans and mutations require approval.
- Made usable Create/List/Details Pages part of new-Structure completion. Configure generated Pages through supported update affordances; verify returned Views and required nodes. List Pages use a table bound to the Structure's Data Source and stable node codes; keep Create Page reachable where applicable. Treat unresolved Workspace issues, including `default_nodes_required`, as blocking.
- Clarified Structure, Field, Relation, and Page defaults, including owned-child navigation and Create/List field guidance.
- Require numbered verified Installation choices, verbatim Discovery authoring links, stopping on request/CLI errors, and reading default language and currency from Platform Setup.
- Synced `VERSION` and every skill's metadata version to `1.4.0`.

## v1.3.1

### Added
- Added Metadata authoring conventions: resolve `defaultLocale` through Discovery Platform Setup, provide required default-locale text, translate only when meaning is known, prefer `snake_case` for new codes, and preserve contract-defined identifiers.

## v1.3.0

### Added
- Added `horizon-interview` for planning unclear, complex, bulk, relational, destructive, and cross-surface work.
- Added local redacted plans at `.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md`, with approval gates and purge guidance.
- Added Business Data mutation confirmation and scope-change reapproval rules.

### Changed
- Updated Horizon routing, authoring, and runtime skills to require approved plans for complex work.

## v1.2.2

### Added
- Added Horizon bootstrap error reporting: relay error status and message as-is, stop, and do not retry with workarounds or guessed variants.

## v1.2.1

### Added
- Added CLI-only file transfer for Business Data and Metadata assets, plus a black-box asset-upload scenario.

### Changed
- Updated Widget authoring guidance for reuse, binding, preview, usage repair, review handoff, assets, typography, layout, visibility, governance, and publication boundaries.
- Added a black-box Widget authoring scenario.

## v1.1.0

### Added
- Added read-only `horizon-ask-for-guidance` support for Horizon Metadata architecture decisions.
- Added guidance for choosing Fields, Structures, Relations, and platform Users; explaining Installation-specific Metadata and authorization; and treating executable Metadata as authoritative.
- Added evidence, uncertainty, human-gate, safe-next-step, and Horizon CLI update guidance.

### Changed
- Clarified that guidance remains read-only and routes Metadata and runtime mutations to dedicated skills.
- Standardized release titles to use version tags directly, such as `v1.1.0`.
