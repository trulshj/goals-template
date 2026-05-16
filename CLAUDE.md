# Goals Workspace

This directory is a personal OKR and goal-tracking system.

## Files

- **`inbox.md`** — drop raw thoughts, ideas, reflections, or notes here at any time
- **`goals.md`** — structured OKRs organized by quarter and area
- **`log.md`** — running log of completed actions, workouts, check-ins, and milestones

## Session startup (always do this)

1. Check `inbox.md`. If it has unprocessed content, process it (see below).
2. Check `reminders.md` for any active reminders due today or within the next 7 days. Surface them prominently. Mark any past-due reminders as overdue.
3. After inbox is clear (or if it was already empty), scan `goals.md` for the current quarter:
   - Flag any KRs that are behind, overdue, or have no recent log entry in `log.md`
   - Prompt the user about 1–3 specific things they should act on or log today
   - Keep it concrete: "You haven't logged a workout since May 3 — did you train this week?" not generic encouragement

## Inbox processing

When the user says "process my inbox" or inbox has content at session start:
1. Read all items in `inbox.md`
2. For each item, propose: new Objective, new Key Result on an existing O, a log entry, or discard
3. Confirm with user before writing anything
4. Update `goals.md` and/or `log.md` as agreed
5. Clear processed content from `inbox.md`

## Goals structure (OKR format)

`goals.md` is organized by **quarter**, then **area** (Personal / Professional), then **Objectives** with **Key Results**.

```markdown
# Q2 2026 (Apr – Jun)

## Personal

### O1: Objective title
- KR1: Description — target: X | current: Y
- KR2: Description — target: X | current: Y

## Professional

### O1: Objective title
- KR1: Description — target: X | current: Y
```

- Objectives are qualitative outcomes ("Be consistently fit")
- Key Results are measurable and time-bound ("Run 3x/week for 8 of 13 weeks")
- Update KR `current` values when logging progress
- At quarter end, mark the quarter `## Achieved` or `## Missed` with a short retro note
- Monthly goals go under `# [Month] YYYY` sections, same format

## Log format

`log.md` entries are short, dated, and tied to a KR:

```markdown
## 2026-05-07
- [Personal / O1 / KR1] Ran 8km, felt strong
- [Professional / O2 / KR2] Finished stakeholder doc
```

## Commands

Custom slash commands live in `.claude/commands/goals/`. Invoke them as `/goals:<verb>`.

| Command | What it does |
|---|---|
| `/goals:process` | Process inbox.md, integrate into goals.md / log.md, then prompt about today's priorities |
| `/goals:triage` | Print a color-coded status overview of all current quarter goals, plus top priorities |
| `/goals:food [description]` | Estimate calories, protein, carbs, and fat for a meal, with a Cronometer logging tip |
| `/goals:remind [description] by [date]` | Add a reminder to reminders.md, surfaced at session startup when due within 7 days |

To add a new command: create `.claude/commands/goals/<verb>.md` with instructions, and add a row here.

## Working with goals in conversation

- "add a goal" → ask: area, quarter/month, objective, measurable KRs, deadline
- "log X" → add entry to `log.md`, update relevant KR current value in `goals.md`
- "how am I doing" → summarize current quarter KR progress vs targets
- "mark KR done" → update current value to target, note date in `log.md`

## Tone

Direct and practical. No motivational filler. When prompting about things to act on, be specific and brief — one sentence per prompt.
