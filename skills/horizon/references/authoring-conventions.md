# Localized text and codes

Apply before creating a Workspace or constructing authored labels, localized messages, or new codes. Current Discovery remains the contract authority; these are authoring preferences, not replacement schemas.

## Localized text

1. Follow current Discovery to the Installation's Platform Setup and resolve the shared `localized-text` schema, including references from the request schema. Read `defaultLocale`; use the locale keys and value shape that current schemas accept. Refresh this context after changing Installation or Platform Setup. Chat language does not select the required locale.
2. Supply meaningful, non-blank text in the configured default locale. Other translations are optional unless the current contract says otherwise; PT, ES, and EN are not universally required.
3. Prefer adding PT, ES, and EN translations when those locales are accepted and the meaning is known. Reuse established terminology from nearby labels and Semantic Terms/Aliases; otherwise translate faithfully when confident. Preserve proper names and domain distinctions. A translation must not add business facts, expand an unexplained acronym, or guess what an ambiguous term means.
4. Omit an uncertain optional translation rather than filling it with a guess, placeholder, or copied text presented as a translation. If the required default-locale meaning is unclear, ask User before authoring. Note meaningful translation gaps in the handoff.
5. On updates, preserve correct existing translations. When meaning changes, update affected translations coherently; ask User how to handle any translation you cannot confidently revise instead of leaving stale meaning or silently deleting it.

Apply the same procedure to every property whose schema references `localized-text`, including labels and user-facing localized messages. Keep ordinary prose and plain-string properties in their discovered shape.

Completion: required default-locale text is present, every supplied translation preserves the known meaning, optional gaps are explicit, and payload follows the live schema.

## Codes

- Prefer lowercase ASCII `snake_case` for new authored codes: `purchase_order`, `due_date`, `total_amount`. Choose a short, stable concept name from established Metadata vocabulary, then verify the property's live schema and uniqueness scope before sending it.
- Keep readable, translated wording in labels. A label or language change does not rename a code. Reuse existing codes exactly when referencing Metadata; preserve externally assigned Business Instance identifiers.
- Apply this convention to authored code values, not JSON property names, locale keys, enum literals, reserved identifiers, or returned links. Preserve those exactly as Discovery specifies. If a schema or automatic code-generation rule governs a value, follow that rule rather than forcing snake_case.

Completion: new codes follow snake_case where the current contract permits it, fit their uniqueness scope, and existing identifiers and contract-defined spellings remain unchanged.
