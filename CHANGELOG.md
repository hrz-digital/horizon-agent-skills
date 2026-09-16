# Changelog

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
