---
name: horizon-interview
description: Plan unclear, broad, multi-step, bulk, relational, destructive, or cross-surface Horizon work before execution. Use for complex Metadata proposals and Business Data mutations; skip for small, unambiguous requests.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1 when platform facts are needed.
metadata:
  author: hrz-digital
  version: "1.5.2"
---

# Horizon Interview

Settle intent before execution. Current Discovery supplies platform contracts and evidence; this skill owns clarification and plan approval. Show a clarification round only when the agent holds at least one real question. When it holds none, go straight to the Plan summary and wait for approval; never show an empty round.

## Planning gates

Apply these gates after `horizon` bootstrap and initial Discovery/Metadata inspection:

- **Clarification:** interview unresolved or substantial Metadata work and unclear, broad, multi-step, bulk, relational, destructive, or cross-surface runtime work. Ask only what inspection and the request cannot settle. Fully specified localized work can proceed directly.
- **Default:** show a concise plan summary in chat, confirm clarified decisions and required approvals, then execute in the same session. Skip the interview round when the agent has no question, and wait for approval before proposing any mutation. Multiple Structures, bulk work, and interview depth do not by themselves require a file.
- **Business Data:** every Business Data mutation needs explicit confirmation of target, records, values, and intended effect, whether planned in chat or in a file.
- **Plan file:** use one only for large work spanning multiple sessions with substantial dependencies or sequencing, or when User explicitly requests a durable plan. Routine interruptions do not require a file; use Workspace Activity for Metadata continuity.

## Interview

1. Use the explicit live-valid Installation selected through `horizon` bootstrap. If the request does not identify what to inspect, ask only the minimum orientation needed. No implementation plan yet.
2. Inspect relevant Discovery, Metadata, Semantic, and Workspace state when applicable. For ordinary Metadata inventory, use the authoring links to Structures and Workspaces, not Architecture Analysis. Follow returned methods, hrefs, schemas, catalogs, and availability; decide whether to extend existing concepts or create new ones.
3. For Metadata, use authoring's [three-layer proposal](../horizon-metadata-authoring/SKILL.md#three-layer-metadata-proposal) and [Structure and Page defaults](../horizon-metadata-authoring/SKILL.md#structure-and-page-defaults) as planning reference, not permission to execute. Show a recommendation for each layer and, when Visualization is in scope for new Structures, the Page table below. Always show all three layers. New Structures alone do not imply a data-model-only request. Propose usable Visualization by default: Create/List/Details Pages, Data Sources, Views/Nodes, the create trigger that makes each new Structure's Create Page reachable, and owned-child navigation where applicable. Settle each layer as agreed configuration, `out of scope (no configuration needed)` with reason, or `out of scope (User-directed)` only for explicit exclusions; a new Structure's Visualization settles as agreed configuration or `out of scope (User-directed)` only. Keep Installation default currency in Visualization as display formatting, not a Data Modeling commitment to a currency; cite current Discovery and User preference. Show defaults as proposed work, not permission questions.
For Automation, inspect existing Process Definition Semantic and typed contracts before asking workflow questions. Prefer suitable existing behavior; settle trigger intent, typed inputs/results, explicit effects, people, repeat policy and evidence only where unresolved. Business state and Relations belong to Data Modeling; Pages and visible placement belong to Visualization. Preserve agreed layer outcomes and explicit exclusions. Revisit an earlier decision only when an actual automation dependency requires it; a cosmetic-only edit does not reopen the Automation interview. Include authorized Test fixtures, participant preparation and unsupported checks in the reviewed plan.

4. Ask every currently unblocked decision in numbered rounds; ask none and go straight to the Plan summary when inspection and the request already settle everything. Each item asks one independent question followed by a `recommendation:` statement with a specific choice and reason, or the evidence needed. Split decisions whose answers could differ, including Relation cardinality versus requiredness and required Fields on different Structures. Omit decisions already settled unless Discovery reveals a conflict. Wait for answers, then make targeted Discovery rechecks of their implications. Repeat until no material decision remains unresolved.
5. For Business Data changes, settle destination, identity, relationships, values, validation, duplicate/update behavior, failure handling, scope, and effects. For spreadsheet imports, map every source column to a destination or an explicit ignore decision; record counts and anonymized examples, never raw records.
6. Show the **Plan summary** below and obtain confirmation of clarified decisions and required mutation approvals, then wait for that approval before any mutation. Existing explicit instructions count as settled decisions; do not ask again without conflicting evidence. Only when the plan-file gate applies, follow [implementation-plan.md](references/implementation-plan.md) for storage, privacy, and lifecycle, and obtain explicit approval of its reviewed summary.
7. Continue through the appropriate execution skill in the same session, then follow **Execution and User testing** below. Ordinary execution needs neither a fresh session nor a saved file. For later Metadata sessions, use `horizon` Workspace selection and Activity; use its [approved-plan procedure](../horizon/SKILL.md#implement-approved-plan) when resuming a saved plan.

## Metadata interview response

Use this shape only when a round actually has questions. When no decision is unresolved, skip the interview round and show the Plan summary directly, because it already carries all three layers; an empty round only repeats the summary. In a round, always show all three headings, even when one layer has no questions. The fenced block below shows the reply's structure, not a literal code fence: emit it as rendered Markdown. Number questions continuously across layers; omit settled questions and omit the Page table when no new Structure's Visualization is in scope.

```markdown
Installation: <selected name>; inspected: <relevant existing Metadata>

## Data Modeling
Proposed: <model and existing patterns, or settled layer outcome>
1. <one unresolved decision?>
   recommendation: <choice and reason; no further question>

## Visualization
Proposed: <Create/List/Details Pages → Views → Nodes with Data Sources, the create trigger reaching each Create Page, and owned-child navigation, or out of scope with reason>
| Structure | Create inputs | List table, columns, and create trigger | Details groups and Field order |
| --- | --- | --- | --- |
| <each new Structure> | <editable inputs, including required Fields> | <table element on the Data Source with useful short columns, plus the create trigger reaching the Create Page> | <one unlabeled group in contextual order when sufficient; otherwise named groups with Fields> |

## Automation
Proposed: <behavior, or out of scope with reason (User-directed or no configuration needed)>
2. <one unresolved decision, if any?>
   recommendation: <choice and reason; no further question>

Next: <targeted Discovery recheck, plan approval, or execution>
```

A layer with no questions still shows its proposed or agreed outcome. A recommendation ends with a statement, never another question. For both interview and plan tables, include one row per new Structure when Visualization is in scope. For few Fields that form one coherent flow, use one unlabeled Details group with Fields in contextual order; name and split groups only when that improves navigation. Verify grouping affordances through Discovery.

## Plan summary

Summarize agreed intent in chat using Markdown headings exactly as below. Keep every top-level section as a peer of Metadata, not a nested bullet; only the three architecture layers belong under Metadata. Use `not applicable` with brief reason when needed. For new Structures with Visualization in scope, include the placement table below with actual per-Structure inputs, columns, and Details group/Field order; omit the table only when Visualization is out of scope. Treat Installation default currency as presentation, not a fixed-currency modeling decision or risk unless User and current contract require it:

```markdown
# Plan summary
Customer: <confirmed customer; or not applicable — reason>
Installation: <selected live-valid Installation; or not applicable — reason>

## Scope
<goal, included work, exclusions>

## Metadata
### Data Modeling
<Structures, Fields, Relations, Constraints; or out of scope — reason>

### Visualization
<Data Sources; Create/List/Details Pages → Views → Nodes, bindings, the create trigger reaching each Create Page, and owned-child navigation; or out of scope — reason>
| Structure | Create inputs | List table, columns, and create trigger | Details groups and Field order |
| --- | --- | --- | --- |
| <each new Structure> | <editable inputs, including required Fields> | <table element on the Data Source with useful short columns, plus the create trigger reaching the Create Page> | <one unlabeled group in contextual order when sufficient; otherwise named groups with Fields> |

### Automation
<Process Definitions, Structure Action bindings, supported triggers/operations and effects; or out of scope — reason>

## Business Data
<targets, record scope, values, effects, failure handling; or not applicable — reason>

## Execution
<steps, dependencies, Workspace choice for Metadata; or not applicable — reason>

## Complexity
<execution and validation workload with reason, even if small>

## Risks
<material effects and limits; or not applicable — reason>

## Validation
<Agent checks and safe manual checks for User, including the Test instances the checks reuse or create; or not applicable — reason>

## Next
<required confirmation or same-session execution>
```

Use counts, mappings, and anonymized examples rather than raw records in summaries. Approval permits agreed execution, not Workspace acknowledgement, human review approval, or Publication.

## Execution and User testing

1. Execute agreed work through the appropriate skill and current Discovery; report validation evidence and any limits.
2. Offer focused manual checks and ask User to test and report adjustments. Distinguish Agent validation from pending User acceptance; never claim User testing occurred without feedback.
3. Apply requested adjustments and validate again. Reopen clarification or approval only when scope, effects, or material evidence changes; every additional Business Data mutation still needs explicit confirmation. Do not replay successful mutations as a test. A test scenario is a normal part of feature validation: name the Test instances it reuses or creates in the plan summary so approval covers them, then follow `horizon-metadata-authoring`'s [test scenarios](../horizon-metadata-authoring/SKILL.md#test-scenarios). Fixtures beyond that set need fresh confirmation.
4. Record Metadata decisions, progress, User feedback, and remaining work in Workspace Activity. A routine interruption resumes there without creating a plan file. For runtime-only work, reconcile current state and confirm remaining intent if session context is lost; do not invent a Workspace or replay mutations.

Completion: in-scope decisions and required approvals are settled, the summary is sufficient for execution, and no platform mutation occurs while understanding remains unresolved. A file is required only by the plan-file gate.
