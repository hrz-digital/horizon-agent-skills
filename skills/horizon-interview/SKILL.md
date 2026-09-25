---
name: horizon-interview
description: Plan unclear, broad, multi-step, bulk, relational, destructive, or cross-surface Horizon work before execution. Use for complex Metadata proposals and Business Data mutations; skip for small, unambiguous requests.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1 when platform facts are needed.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon Interview

Reach shared understanding before execution. This is a planning gate, not a replacement for Discovery. Platform contracts, schemas, catalogs, routes, availability, authorization, and Metadata Context remain authoritative in current Discovery.

## Interview depth and written plan

For Metadata, enter this workflow after initial Installation selection and Discovery inspection only when a decision remains, execution is substantial, or a handoff is likely. A clear localized change with no conflicting evidence proceeds directly to authoring. Ask only unresolved decisions: one round may settle a change; uncertain meaning may take many rounds. Separately, judge execution workload after understanding is settled. Few localized Metadata edits can proceed without a plan file, even after a deep interview. Multiple related Structures, substantial cross-surface authoring, or likely session handoff need a written plan, even when intent was easy to understand.

For every Business Data mutation, obtain explicit confirmation of target, records, values, and intended effect; require an approved written plan for bulk, relational, destructive, or ambiguous work.

## Interview

1. Use the explicit live-valid customer Installation selected through `horizon` bootstrap. If the request does not identify what to inspect, ask only the minimum orientation needed. No implementation plan yet.
2. Inspect or refresh current Discovery and relevant Published Metadata, Workspace state, Semantic, schemas, catalogs, affordances, and availability. For Metadata authoring, follow the Discovery authoring links to list Structures and Workspaces and read relevant Structure detail; Architecture Analysis is for audits and Tickets, not this inventory. Use each returned method and href unchanged, including its prefix. Determine whether the request extends existing Structures or patterns or creates genuinely new ones. Ask User only about decisions this inspection cannot settle. Follow root Discovery `platformSetup` link for `defaultLocale` and `defaultCurrency`. For financial presentation, use that default currency unless User requests a different currency or multi-currency behavior; do not ask for its default value.
3. For Metadata requests, frame decisions in three layers: **Data Modeling** (Structures, Fields, Relations, types, Constraints), **Visualization** (Data Sources, Pages, Views, Nodes, Widgets), **Automation** (Actions, Alerts, executable rules and supported side effects). Show User a recommendation for each layer. For new Structures, the Visualization proposal includes configuring usable Create, List, and Details Pages and parent Navigation to owned child lists by default. After inspection, show this as proposed work using Discovery contracts. For each new Structure, show a compact table with columns `Structure | Create inputs | List columns | Details groups`; name suitable Create inputs, useful List columns, and all Fields on Details grouped by context (identity/classification first). Put every long-text Field on Details and omit it from List columns by default unless User requests otherwise. Create may include useful long text and must include confirmed required Fields; exclude derived values from Create inputs. Refine proposals as inspection continues; ask about specific additional screens or placement only when relevant. An explicit User request for a data-model-only scope overrides this default; absent that request, do not turn Page configuration into a choice or call Visualization `no configuration needed`. Clarify each layer's intended outcome; record `no configuration needed` only when User agrees no change is needed in that layer, never as a substitute for unresolved understanding. A requested list of new Structures does not exclude existing platform concepts such as User; discover availability before recommending a link. Ask only decisions that affect the requested outcome; accept explicit User overrides of defaults. For new Fields, clarify genuinely ambiguous meaning before choosing a type. For new Structures, confirm which Fields are required at creation; for a single Field on an existing Structure, keep it optional unless the request or existing rules say otherwise. For multiple Structures, propose a relationship map with Primary/Secondary classification and each Relation's source, target, cardinality, and ownership; confirm independent Relation decisions separately, then confirm the complete map before authoring. A proposed relationship from names is never a decision.
4. Work questions in rounds using the Metadata response format below. Each numbered item asks one independent decision: split any clauses whose answers could differ, including cardinality versus requiredness on the same Relation and required Fields on different Structures. Omit questions already answered by User (such as supplied enum options) unless Discovery finds a conflict. Immediately below it put a grounded `recommendation:` line with a specific choice and reason, or what evidence must be clarified; this line ends the item, with no second question. Show baseline work as a proposal, not a permission question. Ask every currently unblocked decision, wait for answers, then use targeted Discovery reads to check what the response implies before the next round. Revise recommendations against existing Installation patterns; repeat interview ↔ Discovery until no material decision remains unresolved. Do not silently assume unresolved answers.
5. For Business Data creation or change, make destination, identity, relationships, values, validation, duplicate/update behavior, failure handling, scope, and intended effects explicit. For spreadsheet imports, map every source column to a destination or an explicit ignore decision; record counts and anonymized examples, never raw records.
6. Once Installation inspection and interview ↔ Discovery have settled decisions, assess execution workload independently of interview difficulty. For substantial Metadata work, complex Business Data work, or likely handoff, write a concise plan using [implementation-plan.md guidance](references/implementation-plan.md) at `.hrz/<customer-code>/<installation-code>/<feature-slug>/implementation-plan.md`. Normalize path components to lowercase `[a-z0-9._-]`; replace other characters with `-`; reject empty values and `..`, `/`, or `\\`. For a few localized Metadata edits, show agreed layer outcomes and continue without a file.
7. For written plans, set status to `awaiting-approval` and show the review summary in [implementation-plan.md guidance](references/implementation-plan.md): agreed decisions for each layer, risks, execution complexity based on work to author and validate, and whether a fresh session is recommended. Show contents, not just the file path. Wait for explicit approval of the reviewed plan, then set status to `approved-to-implement` and Approval gate to `approved` before handoff or execution. For work without a plan file, proceed only after User confirms any clarified decisions; do not add a file-approval gate.
8. If a written plan's scope or material evidence changes, return it to `draft` with Approval gate `pending`, update it, and request approval again. After completion, recommend User purge the plan to prevent stale guidance; Discovery remains the only source of truth.

## Metadata interview response

Use this shape for each round; number questions continuously across layers, omit questions already settled, and include the table when creating Structures:

```markdown
Installation: <selected name>; inspected: <relevant existing Metadata>

## Data Modeling
Proposed: <model and existing patterns>
1. <one unresolved decision?>
   recommendation: <choice and reason; no further question>

## Visualization
Proposed: <baseline Pages and access to owned children>
| Structure | Create inputs | List columns | Details groups |
| --- | --- | --- | --- |
| <name> | <inputs, including required Fields> | <useful short columns> | <all Fields grouped by context> |

## Automation
Proposed: <behavior or candidate for no configuration needed>
2. <one unresolved decision, if any?>
   recommendation: <choice and reason; no further question>

Next: <targeted Discovery recheck, plan approval, or authoring>
```

A layer with no questions still shows its proposed or agreed outcome. A recommendation ends with a statement, never another question.

Plans are local and personal. Do not add host `.gitignore` entries automatically. Never write credentials, tokens, raw Business Data, or raw spreadsheet contents to a plan.

Completion: Metadata decisions are settled in each layer as agreed configuration or `no configuration needed`; substantial execution has an approved written plan, localized execution has confirmed decisions without a file, and no platform mutation occurs while understanding remains unresolved.
