# Horizon Agent Skills

Horizon Agent Skills package portable workflow policy for AI Agents operating Horizon through Discovery. Platform contracts remain authoritative and are never copied into skills.

## Language

**Lua**: Horizon-provided AI assistant persona. Lua operates as an AI Agent through an Agent Credential and has no separate security identity or authority.
_Avoid_: Agent Credential, authorization role

**Integration**: A non-human, Installation-owned identity that an external platform's server uses through an Integration Credential. A change it makes is shown as "via <Integration label>", never as a User, and only human HSA or HSC Users manage it.
_Avoid_: technical User, Agent Credential, Browser Client

**Horizon Skill Set**: Public collection of Agent Skills that guides Discovery traversal, Metadata authoring, runtime operation, and workflow selection.
_Avoid_: API client, platform contract, Lua runtime

**Horizon Skill**: One portable workflow instruction in the Horizon Skill Set. It obtains current schemas, affordances, and capability state from Discovery.
_Avoid_: API documentation, hard-coded schema

**Metadata Architecture Analysis**: A complete review of one Installation's Published Metadata for conceptual overlap, misplaced meaning, and Structure boundaries that may warrant consolidation.
_Avoid_: Source-code review, Workspace validation, automatic Metadata repair

**Architectural Metadata Ticket**: A durable Metadata architecture quality concern created or reconfirmed by Metadata Architecture Analysis and tracked through implementation, verification, resolution, or reasoned acceptance.
_Avoid_: Workspace Attention Item, issue tracker ticket, analysis report

**Version**: The published state of a Metadata item (Structure, Process Definition, Widget, Dashboard, Profile Feedback Definition). It advances once per Publication that changes the item; v0 means awaiting first Publication. A Package has its own published Version. An Asset's content versions are upload snapshots, not Publication Versions.
_Avoid_: revision, save counter, Asset content version

**Revision**: The saved-change counter of one record. It advances on every save and is the optimistic-concurrency token an Agent reads and sends back when saving; shown as rev.N. A Structure's effective revision is an opaque token, never a number to compute.
_Avoid_: Version, published state, counter to increment locally

**Design Brief**: A shareable document describing the goal, available Metadata, design constraints and, for improvements, the existing presentation baseline. It supports external design and return integration without client Business Data.
_Avoid_: Design Package, platform Package, implementation plan

**Design Guide**: The reusable compatibility instructions included in a Design Brief, grounded in the selected Installation's current discovered contracts.
_Avoid_: Design Brief, API authority
