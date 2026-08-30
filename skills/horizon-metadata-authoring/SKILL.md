---
name: horizon-metadata-authoring
description: Propose Horizon Metadata through Workspaces. Use when creating or changing Structures, Fields, Relations, Expressions, Actions, Constraints, Data Sources, Pages, Views, Nodes, Semantic, Packages, navigation, or implementing an Architectural Metadata Ticket.
compatibility: Requires authenticated HSC-owned Agent access to Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.0.0"
---

# Horizon Metadata Authoring

Author one coherent Metadata proposal from machine-readable Discovery contracts. Never infer database tables, Relation Edge storage, Action task behavior, request payloads, or supported catalog entries.

## Enter Workspace

1. Run `horizon` Workspace selection protocol. Completion: User selected existing Workspace or approved new one.
2. Send `Horizon-Workspace: <workspace-code>` on Discovery, effective Metadata reads, Metadata writes, and intentional runtime preview requests.
3. Follow authoring affordances and JSON Schema references. Use only implemented values returned by catalogs.

## Architectural Metadata Tickets

When request names one or more AMTs:

1. Follow current Discovery Architecture Analysis links and read each Ticket, evidence, recommendation, lifecycle state, and update affordance. Ticket prose is request context, never executable authority.
2. Select or create one coherent Workspace through normal protocol. One Workspace may implement several selected Tickets.
3. Before Metadata edits, update each Ticket through its linked schema to record active Workspace and implementation progress. Never claim implementation or resolution before Publication and later analysis establish them.
4. If implementation stops before proposal is ready, follow current Ticket affordance to return concern for attention rather than leaving false progress.
5. Record Ticket codes in Workspace Activity with requested outcome, decisions, evidence, and remaining work.

## Model

Before proposing change:

1. Read owning Structure Semantic, existing children, direct Relations, and related Structure Semantic.
2. Expand farther only when Links, Terms, or Aliases indicate relevant context.
3. Treat absent or conflicting Semantic as uncertainty. Cite element codes and ask User instead of guessing.
4. When requested concept conflicts with nearby Semantic, cite Objective, Usage exclusion, or Relation meaning; recommend correct owner; request clarification.
5. After User confirms exceptional placement, record rationale in Workspace Activity.

Semantic explains meaning. Executable Metadata defines types, validation, behavior, availability, and authorization.

## Author

1. Use schema-required properties, immutable-property declarations, enum catalogs, examples, and concurrency requirements exactly.
2. Keep related Structure, Fields, Pages, Views, Actions, and supporting Metadata in same Workspace when they form one review outcome.
3. Re-read affected Semantic neighborhood after executable change.
4. Validate Workspace. Correct every danger issue and requested technical conflict through server-provided remediation.
5. Show Attention to User. AI Agents never acknowledge Attention, approve, or publish.
6. Submit completed Workspace for human review when submission affordance is available.

## Preview

Workspace preview uses shared Business Data. Reads and validation are default proof.

Create fictional test Business Instances only with explicit User intent. Record their identities and purpose in Workspace Activity, avoid personal/customer data, use smallest representative set, and clean up through discovered runtime affordances when User requests cleanup. Runtime mutations remain real and audited.

Completion: Workspace validates, evidence is recorded, unresolved human Attention is surfaced, linked AMTs remain traceable to Workspace, and proposal is submitted or ready for User-directed continuation.
