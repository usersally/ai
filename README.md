# 📓 Scratchpad

> *jot it down, cross it off*

A minimal, delightful todo app styled like a spiral notebook — ruled lines, a red margin stripe, and handwritten fonts that make task management feel tactile and personal.

---
## Features

- **Add tasks** — type and hit Enter or click `+`
- **Priority levels** — 🔴 high, 🟡 medium, 🟢 low
- **Toggle done** — click the checkbox to cross things off
- **Inline edit** — double-click any task text to rename it
- **Filter views** — All / Active / Done
- **Clear done** — sweep completed tasks off the page
- **Persistent storage** — tasks saved to `localStorage`, survive page refresh
- **Zero dependencies** — single HTML file, no build step
---
## Usage

Just open `index.html` in any modern browser. No server, no npm, no config.
```bash
open index.html
# or
npx serve .
```
---
## Design

The aesthetic is a ruled notebook page — cream paper, a left red margin line, spiral holes, and [`Caveat`](https://fonts.google.com/specimen/Caveat) (handwriting) paired with [`Libre Baskerville`](https://fonts.google.com/specimen/Libre+Baskerville) (serif) for a human, analog feel. Strike-throughs are styled in red to look like pen marks.

---
## Project Structure

```
todo-app/
├── index.html     # Everything — markup, styles, and logic
└── README.md
```
---
## Browser Support

Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

---

*Built as a single-file app. No frameworks, no bundlers — just the essentials.*
