# Project Spec — Scratchpad Todo App

**Version**: 1.0  
**Status**: Complete  
**Stack**: Vanilla HTML / CSS / JS (single file)

---

## Overview

Scratchpad is a browser-based personal task manager. The core experience is intentionally analog — it looks and feels like a physical ruled notebook, making everyday task management calmer and more enjoyable than typical productivity apps.

---

## Goals

| Goal         | Description                                             |
| ------------ | ------------------------------------------------------- |
| Fast capture | Add a task in under 2 seconds                           |
| Low friction | No login, no sync, no setup                             |
| Personality  | Distinctive visual identity — not another white card UI |
| Persistence  | Tasks survive browser refresh via localStorage          |

---

## Core Features (v1.0)

### Task Management

- Create tasks with free-form text (max 120 chars)
- Mark tasks as done / undone (toggle)
- Delete tasks individually
- Inline rename (double-click to edit)
- Clear all completed tasks at once

### Priority

- Three levels: high 🔴, medium 🟡, low 🟢
- Set per-task at creation via emoji selector
- Shown as a colored dot next to each task

### Filtering

- All tasks
- Active only
- Done only

### Persistence

- All data stored in `localStorage` under `scratchpad-tasks`
- No backend, no accounts

---

## Out of Scope (v1.0)

- Due dates / reminders
- Drag-and-drop reordering
- Sub-tasks or nested lists
- Cloud sync or multi-device
- Dark mode

---

## Design Decisions

**Single HTML file** — zero install, zero dependencies, runs anywhere. The constraint forces simplicity.

**Ruled notebook aesthetic** — Most todo apps look like dashboards. Scratchpad leans into paper nostalgia to reduce the "productivity app dread" that makes people avoid opening them.

**Caveat + Libre Baskerville** — Handwriting font for task text gives the app warmth; the serif for UI chrome adds editorial refinement without being cold.

**Red strikethrough on done tasks** — Mimics crossing something off with a red pen — more satisfying than a grey fade.

---

## Future Ideas (v2.0+)

- Drag-to-reorder tasks
- Due date field with overdue highlight
- Tag / label system
- Export to plain text or markdown
- Optional sync via a simple backend (e.g. PocketBase)
