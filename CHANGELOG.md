# Changelog

## v1.5.2 (Unreleased)

### Added
- Added Discovery-grounded Dashboard guidance and scenarios for Package ownership, stable identity and translations, Installation-wide default proposals, complete Workspace diffs, human Publication, and independent Dashboard/source Structure authority.

### Changed
- Routed Dashboard proposals to Metadata authoring and authorized inspection to runtime; unavailable authoring and defaults remain explicit refusals.
- Synced VERSION and every skill metadata version to 1.5.2.

## v1.5.1 (unpublished)

### Added
- Added Process Definition scenarios for localized-label edits with stable references, selective JSON starter completion, authored-draft preservation after starter changes, and mutually exclusive Mutation value sources.
- Added structural verification for the new authoring guidance and scenarios, and consistent skill-set metadata versions.

### Changed
- Clarified JSON starters as independent per-property draft scaffolds: select only needed parts, complete declared references, verify defaults against User intent, and preserve authored configuration.
- Clarified direct Field mappings versus prepared object results for Mutation authoring, one value source per operation, and creation versus update target requirements.
- Distinguished Query cardinality and supported extraction from Script object/array results; unsupported whole-object extraction cannot silently select the first row.
- Sharpened prior-Condition guard references and localized-label readback without changing stable identities, authored translations or behavior.
- Synced `VERSION` and every skill's metadata version to `1.5.1`.

## v1.5.0

### Added
- Added Discovery-grounded JSON starter guidance: complete current draft scaffolds, validate proposals, preserve authored configuration, and respect mutually exclusive choices.
- Added Discovery-grounded operation label and guard guidance: stable codes versus localized presentation, persisted readback, discovered run-or-skip behavior, and explicit skipped-output dependencies.
- Added Discovery-grounded SMTP setup and testing guidance: preserve existing definitions and secrets, save the agreed server, test only to an authorized recipient through the shared notification sender, respect external-send and context limits, and report storage, provider acceptance and inbox receipt separately.
- Added Discovery-grounded integrated periodic-process proof guidance and scenarios: truthful partial committed-effect and delivery summaries, exact response membership across recovery, processed-work exclusion versus active overlap, independent bulk Actions, scoped oversight, recurring and watched-change evidence, and equivalent Test exercise with preserved fixtures and requester attribution.
- Added Discovery-grounded terminal Test execution purge guidance and scenarios: permanent target-specific intent, administrative authority and current availability, race refusals and safe recovery, retained fixtures and committed effects, compact deletion accountability, stale-work verification and list cleanup.
- Added Discovery-grounded watched Business Data trigger guidance and scenarios: transitions versus existing state, supported attribute and matching-policy discovery, explicit committed Test exercises, original-event and definition-snapshot evidence, idempotent admission, truthful Actor and initiator provenance, bounded causal stops, and separate notification retry and business repetition.
- Added Discovery-grounded recurring schedule guidance and scenarios: business cadence and start anchors, saved-timezone and next-occurrence readback, discovered daylight-saving and short-month policies, safe edits with retained history and accepted snapshots, independent unresolved-occurrence inspection, and durable advancement verification after restart or concurrent retry.
- Added Discovery-grounded one-time scheduling guidance and scenarios: explicit local time and timezone with converted-instant readback, durable intent versus accepted execution, System provenance, inactive Workspace schedules with explicit Test exercise, protected-input refusals, conservative overdue handling, and inspection before restart or repeat decisions.
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
- Clarified incremental Process Definition authoring: save an unfinished identity-only draft when Discovery permits it, preserve its incomplete state, and add valid operations before Workspace validation and human Publication.
- SMTP registration now follows an explicit register → test → User feedback and receipt-confirmation request → persist acknowledgment sequence, with a wait for the User’s confirmation before marking the setup as tested.
- SMTP setup guidance now records receipt acknowledgment only after explicit recipient confirmation, verifies canonical persistence, and treats confirmation as stale after settings or credential changes.
- Clarified that SMTP administration tests Installation-wide saved settings independently of the author’s selected Workspace when current Discovery permits the check; Process external-effect restrictions remain separate.
- Horizon routing and runtime skill discovery now include Installation SMTP configuration and delivery checks.
- Completed Automation-layer process guidance across routing, interviews, plans, authoring and runtime: preserve settled layer scope, reuse suitable definitions, model recurring summary alerts as scheduled selection and notification, honor unavailable administrative controls, and exercise narrow Test User references and authenticated responses through current Discovery. Extended behavioral scenarios for supported, missing and restricted Installations.
- Expanded Discovery-grounded schedule recovery guidance and scenarios: explicit missed-work intent, discovered lateness tolerance, retained per-occurrence history, latest-only catch-up, audited administrative Run now and Skip decisions, current eligibility refusals, durable race winners, and accepted execution failure versus start problems.
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
