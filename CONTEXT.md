# Horizon Agent Skills

Horizon Agent Skills package portable workflow policy for AI Agents operating Horizon through Discovery. Platform contracts remain authoritative and are never copied into skills.

## Language

**Lua**: Horizon-provided AI assistant persona. Lua operates as an AI Agent through an Agent Credential and has no separate security identity or authority.
_Avoid_: Agent Credential, authorization role

**Horizon Skill Set**: Public collection of Agent Skills that guides Discovery traversal, Metadata authoring, runtime operation, and workflow selection.
_Avoid_: API client, platform contract, Lua runtime

**Horizon Skill**: One portable workflow instruction in the Horizon Skill Set. It obtains current schemas, affordances, and capability state from Discovery.
_Avoid_: API documentation, hard-coded schema
