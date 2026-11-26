# Organize a Page form

Use this workflow when asked to organize, tidy, or review the form layout of an existing Page. It builds on the boolean View, Row Group, and `controlHeight` defaults in [Structure and Page defaults](../SKILL.md#structure-and-page-defaults). Current Horizon Discovery remains authoritative for every route, schema, Field View catalog, layout size vocabulary, size derivation, `controlHeight` class, and Row Group behavior.

## Workflow

1. **Check authoring availability from Discovery.** Start at current Discovery. When Discovery omits `authoring` or withholds Page authoring for the caller, report that authoring is unavailable so you can only analyse: inspect the Page and layout rules read-only if readable, evaluate **Layout rules** below, present the read-only findings and suggested changes, and stop without creating a Workspace or attempting any write.
2. **Select Workspace and read the Page.** Follow `horizon`'s Workspace selection protocol, refresh Discovery in that Workspace context, and verify `metadataContext` before following authoring links. Read the target Page's current Views and Nodes together with the referenced Fields and Relations on the owning Structure so you know each Element's label length, type, View, and meaning.
3. **Read current layout rules.** Fetch current Discovery's Page layout rules for supported Element and Group sizes, size derivation (outside and inside Row Groups), `controlHeight` classes, Row Group behavior, and validation restrictions.
4. **Detect layout issues.** Evaluate every form Group and Element in the Page against every rule in **Layout rules** below. Preserve tree order where meaning depends on sequence (for example, a Field that qualifies or explains the Field immediately before it). Propose a reorder only when layout alignment improves without altering meaning, and record every reorder for the summary.
5. **Propose the changes in the Workspace.** Apply the agreed improvements through discovered update affordances and linked schemas in the selected Workspace:
   - Update the Page by resending its complete View list and node tree, preserving unrelated Views, Groups, Elements, bindings, visibility rules, and stable node codes.
   - When a rule changes a boolean Field to a label-beside View, update that Field through its discovered Field update affordance in the same Workspace and record that the Field View change affects every Page where that Field renders.
6. **Validate and read back.** Run Workspace validation, resolve every issue the proposal introduced, and read back the saved Page, any updated Field, and the Workspace diff.
7. **Present a before/after summary for HSA acceptance.** Show the before/after layout organized by Group, naming each applied rule and affected Node or Field, every explicit reorder and why meaning stays intact, any Field-level View scope impact, and validation/diff evidence. Hand off to the HSA to review and accept; leave Attention acknowledgement, approval, and Publication to an eligible human.

Completion: every rule in **Layout rules** has been evaluated against current Discovery layout rules; when authoring is omitted, read-only findings are reported with no writes; otherwise the Workspace holds the validated, read-back Page and Field changes, the before/after summary states every applied rule, reorder, and Field-level scope impact, and work stops before acknowledgement, approval, or Publication.

## Layout rules

Evaluate every rule below. Keep this list extensible: later rules join as peer subsections with **Detect**, **Propose**, and **Why**.

### Lone label-over boolean

- **Detect:** A label-over boolean Element placed directly in a multi-column Section grid cell without a companion input (leaving most of its grid cell empty), or carrying a sentence-like label that reads poorly above a compact control.
- **Propose:** When the boolean belongs beside a neighbouring single-line input of the same `controlHeight` class, wrap them in a Row Group using the Row Group sizing guidance in [Structure and Page defaults](../SKILL.md#structure-and-page-defaults). When the boolean has a long, sentence-like label or has no natural companion input, switch the Field to a label-beside View supported by current Discovery (in the same Workspace) and give the Element a larger tier size from Discovery if the label needs room.
- **Why:** A label-over boolean derives a compact grid track and leaves wasted horizontal space beside a narrow control; pairing it in a Row Group lets the neighbouring input absorb the line, while a label-beside View gives longer labels readable width without a separate Row Group.

### Mixed control heights on one line

- **Detect:** Elements sharing a visual line (inside a Row Group or consecutively on a Section row) whose `controlHeight` classes in current Discovery differ — especially taller pickers (such as Relation or asset pickers) placed beside single-line inputs or buttons.
- **Propose:** Regroup controls by `controlHeight` class so pickers sit beside pickers and single-line inputs sit beside single-line inputs, while preserving tree order wherever meaning depends on sequence. State every resulting reorder explicitly in the before/after summary.
- **Why:** Controls from different `controlHeight` classes misalign labels, baselines, and row rhythm when placed on the same line.

### Boolean-only Row Group

- **Detect:** A Row Group whose direct children are only label-over booleans (or only intrinsic-width `content` Elements with no stretching tier-sized input).
- **Propose:** Pair the booleans with a neighbouring stretching input in the Row Group, switch long-label booleans to a label-beside View in the containing Section, or unwrap the Row Group when no input belongs beside them.
- **Why:** Intrinsic-width `content` children do not stretch; without a tier-sized input to absorb the remaining width, the Row Group leaves trailing empty space and breaks Section alignment.

### Redundant authored size

- **Detect:** An explicit `size` authored on an Element or Row Group that already matches what current Discovery's size derivation and defaults give in its current parent context. Check parent context before flagging: outside a Row Group, compare against Discovery's Element derivation; on a Row Group itself, compare against its discovered default; inside a Row Group, keep an explicit tier `size` because omitting `size` there derives `content` instead of stretching.
- **Propose:** Remove the redundant `size` property from the Node so current Discovery derivation governs it.
- **Why:** Authored sizes that duplicate derivation add metadata noise and prevent future derivation updates from applying automatically.
