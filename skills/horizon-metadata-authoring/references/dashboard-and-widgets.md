# Dashboard and Widget authoring

Use this reference when a Dashboard request needs Widget composition, a supplied HTML dashboard, or a mock-first review. Current Workspace Discovery remains the authority for every authoring affordance, schema, catalog value, and availability result.

## Choose Widget composition

For a business-use-case request without a complete functional HTML reference:

1. Inspect the existing Dashboard, its Page/View trees and sources, candidate Widgets, Widget data contracts, and relevant Data Sources. For an existing Widget that needs changes, follow that Widget's discovered update affordance and linked schema; read its current definition first, preserve fields outside the requested change, and report the exact unavailable reason if update is withheld. Never infer an update URL or use a create affordance to silently replace an existing identity.
2. Decide whether the requested page needs one or several Widget placements. Prefer multiple Widgets for independently useful or reusable sections, independently bound datasets, or distinct interactions. Prefer one Widget when its elements and interactions form one cohesive experience sharing data and lifecycle. Do not default to one Widget per card or one giant Widget for unrelated sections.
3. Reuse suitable existing Widgets first. Create only the Widget definitions and Data Sources needed for the requested experience.

## Presentation inputs

Use presentation inputs for values callers intentionally configure per Widget placement, such as a reusable KPI's title, accent, or display mode. Declare only inputs needed by the agreed use; reuse alone does not require configurable labels or settings.

For a single-purpose Widget with fixed presentation, keep labels in HTML, styling in CSS, and fixed behavior/settings in JavaScript. Use empty `presentationInputs` and `mockInputs` when no placement configuration is required. Localization alone does not require a presentation input.

Keep dataset values in declared data contracts and mock datasets, regardless of Widget reuse. Follow the platform theme by default; expose a theme override only when requested.

Completion: every declared input has an agreed placement-level configuration purpose; fixed presentation remains in the implementation and dataset values remain in the data contracts.

## Convert a supplied functional HTML dashboard

When User supplies a complete functional HTML dashboard with embedded demo data, use exactly one Widget for that reference, even if it contains many cards, charts, tables, filters, or panels.

- Separate the supplied document into the corresponding Widget definition fields for markup, styles, executable behavior, demo data, and only the agreed placement-level presentation inputs under **Presentation inputs** above. Read current authoring schema for exact field names and shape; never paste the whole document into one field or invent a parallel payload.
- Preserve embedded demo records in Widget-owned mock data and define matching Widget data contracts.
- Preserve supplied demo data rather than inventing records. Treat it only as fixture/mock data, never as Business Data. Remove or replace unsupported remote loading with the local Widget lifecycle and currently approved dependencies.
- Keep implementation inside one Widget; do not split the reference's elements into separate Widgets unless User changes the requirement.

## Complete the Dashboard Page

Widget authoring is not complete until requested Widget(s) are placed on the intended Dashboard Page and the saved presentation is read back.

1. Refresh Discovery in the selected Workspace context and verify the returned Metadata Context. Follow its Dashboard listing, detail, presentation, and Widget-placement links; preserve unrelated authored trees and sources, plus existing translations.
2. Add the Widget placement(s) to the intended Page/View. Select the entry Page explicitly. Use only current presentation contracts and supported controls. A Widget alone does not establish Data Source behavior.
3. For a mock-first design review, leave Widget dataset bindings unbound so Workspace preview uses the Widget's mock data. Build the Widget standalone first, then preview it in the Dashboard Page in Workspace context. Do not create Business Data or claim the fixture is live.
4. When real data is in scope, create or reuse declared Data Sources whose outputs satisfy Widget data contracts, then bind each dataset through the discovered placement contract. Query each source under current authority and verify live mappings in Workspace preview. A failed live query is reported, never hidden by mock data.
5. Read back the saved Dashboard presentation and verify Page, View, placements, bindings, entry Page, and expected data requirements. Run available validation and report blockers separately from authoring availability. Do not bypass human-only acknowledgement or claim validation success when blocked.

Workspace preview can retain mock data for unbound Widget datasets. Published context strips mock data, so complete live Data Source bindings before Publication when users need live results. A mock-first Workspace draft is for layout/design feedback, not a promise that a published Dashboard will show those fixtures.

## Structure headers

A Structure header replaces only the instance identity and navigation area of a Business Instance page. Breadcrumbs, Actions, and save status stay platform-owned. Use it when a Structure needs business context beside identity; use the standard header when identity and navigation alone suffice.

1. Reuse before authoring. Discover the shared header Widget candidates through current Widget links and read each candidate's usages before attaching it. One Widget may serve several Structures, but each Structure owns its own header placement, presentation inputs, data bindings, and sticky setting. Never copy a Widget per Structure to vary those values.
2. Keep ownership with the Structure whose instance is displayed. A related collection keeps its parent's header; an individual related instance uses its own Structure's header. Do not place header configuration on a Page or View.
3. Build identity in the Widget. The Widget receives the loaded, authorized instance as reserved instance context and renders code, display label, and Test status itself. Do not name a Data Source `instance`, and do not expect any mandatory native identity or Test slot.
4. Place exactly one canonical native navigation marker in the Widget markup. The platform mounts real Structure navigation there. Zero or duplicate markers, and noncanonical marker markup, are validation failures; never reimplement navigation in Widget scripts.
5. Bind only what the header needs. Explicit current-instance filters scope instance totals and rows; a deliberately Structure-wide comparison stays unscoped. Read the discovered binding and selector rules, then read back the bindings rather than assuming them.
6. Let content set height and let the layout respond to container width. Keep sticky behavior a Structure setting: it defaults on, and an agent chooses it explicitly when the header should scroll with the page.
7. Preview in the Workspace before handoff. A failed custom header falls back to the standard header with the same sticky setting, so validation must describe the fallback rather than assume the custom header always renders.

Completion: each header placement's Widget reference, inputs, bindings, and sticky setting are read back and validated; marker and reserved-name findings are repaired; and the shared Widget's other usages are checked before human review.

## Completion

Dashboard Page contains the chosen Widget composition, source reference HTML is represented by exactly one Widget when supplied, mock data matches its declared contract and is visibly treated as demo data, requested live bindings are configured and exercised when in scope, saved presentation is read back, and human review/Publication gates remain intact.
