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
- Continue work from earlier session → `horizon`; inspect open Workspaces before creating one.
- Test proposed Metadata → `horizon-metadata-authoring` preview branch; remind User Workspace Business Data is shared and audited.
- Explain missing authority → use Discovery reason; eligible HSC-owned Agent may follow Authorization Diagnosis. Never reproduce authorization evaluation.

## Best-practice answer

Give User:

1. Recommended skill and why.
2. Whether task uses Published metadata or explicit Workspace.
3. Human decision required before proceeding.
4. Smallest safe next step.

If request mixes runtime and Metadata work, split sequence: propose Metadata in Workspace, obtain human Publication, re-discover Published contract, then perform runtime work.

Completion: User knows flow, context, human gate, and next skill.
