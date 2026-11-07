# Design Session section

Copy the block below into the brief as the Design Session section, giving the heading the next section number in the brief and adjusting references to it. Do not shorten it.

```markdown
## Design Session and agreement

This brief starts a Design Session, not a fixed specification. The data model
describes what exists today. It is a starting point, not a limit.

### How the session works

1. **First revision: design for the ideal.** Design the dashboard that best
   serves the audience, assuming any field, mock data collection or platform capability
   you need. Do not reduce the design to fit today's data.
2. **Make every dependency visible.** Mark each mock data collection, column, calculation
   and business rule as `available` (exists in this brief) or `proposed`
   (new). Mock data includes proposed columns, so the preview shows the target.
3. **Deliver a gap register** with the first revision (format below).
4. **Agreement.** We review the register together and decide each item:
   `accepted` (we add it to the platform), `adapted` (we agree another shape)
   or `rejected` (the design uses its fallback).
5. **Second revision.** The design is aligned to the agreed register. The
   register becomes the integration checklist.

### What to put in the gap register

| Kind | Examples |
| --- | --- |
| Business rule | What a final status means; how status fields relate; which date drives a time series |
| New field | Created date, due date, request status, loss reason, a value scale |
| New data shape | Group by month, join across a Relation, unnest a multi-value field, date-range filter |
| Platform contract | Interaction events, theme-change signal, font loading, container height |
| Data-protection decision | Whether a personal field may appear, and in what aggregated form |

For each item give:

- **ID** and **kind** (from the table above)
- **What the design needs**, in one or two sentences
- **Why**: which audience question it serves, and what the user loses without it
- **Proposal**: an exact field code, type, options or mock data shape
- **Fallback**: what the design shows if the item is rejected
- **Priority**: `essential`, `valuable` or `nice-to-have`
- **Decision**: left empty; filled in during the agreement

The open questions in this brief are the first entries of
the register. Answer them with your assumption and add your own.

### Questions are welcome at any time

Business-rule questions are expected. When an answer is not available, make
the most reasonable assumption, state it in the register and keep designing.
Do not wait for an answer.

### Definition of done

The session is complete when every register item has a decision, the second
revision uses only accepted or fallback items, and the required checks pass
against that revision.
```
