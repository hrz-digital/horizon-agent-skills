---
name: horizon-ask-for-guidance
description: Ask for guidance choosing Horizon skill workflow.
disable-model-invocation: true
compatibility: Requires Horizon Agent Skills installed.
metadata:
  author: hrz-digital
  version: "1.0.0"
---

# Ask for guidance

Router over Horizon Skill Set. Recommend flow; do not perform platform work here.

## Choose flow

- “Approve Project 001”, update Business Data, manage Relations or Assets, run Data Source, execute Action → `horizon-runtime`.
- Create or change Structure, Field, Relation, Expression, Action definition, Constraint, Data Source, Page, View, Node, Package, Semantic, or navigation → `horizon` then `horizon-metadata-authoring`.
- Audit Published Metadata architecture or verify implemented AMTs → `horizon-architecture-analysis`; no authoring Workspace and no Published Metadata mutation.
- Implement selected AMT recommendation → `horizon` then `horizon-metadata-authoring`; use Ticket evidence as request context and normal human Publication gate.
- Continue work from earlier session → `horizon`; inspect open Workspaces before creating one.
- Test proposed Metadata → `horizon-metadata-authoring` preview branch; remind User that Business Data accessed during Workspace preview is shared and audited.
- Explain missing authority → report the current Discovery-provided reason. Do not recreate authorization evaluation or invent a local diagnosis.

Completion: one workflow is recommended without performing platform work in this router.

## Best-practice answer

Give User:

1. Recommended skill and why.
2. Which Metadata context applies: Published Metadata or an explicit Workspace.
3. Human decision required before proceeding.
4. Smallest safe next step.

If request mixes runtime and Metadata work, split sequence: propose Metadata in Workspace, obtain human Publication, re-discover Published contract, then perform runtime work.

Completion: User knows recommended flow, Metadata context, human gate, and next skill.
