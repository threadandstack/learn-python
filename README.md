# LEARN_PYTHON

A trainee-dev curriculum: Python, from zero, taught by Claude Code.

## Why this exists

The goal isn't "know enough Python trivia to pass a quiz." It's to get you to the
point where you can read code in your other projects (PROJECT_XERO_WORKER,
PROJECT_IRIS_WORKER, the Thread & Stack site, etc.) and actually understand what
it's doing, write real working code yourself, and be comfortable driving a
terminal to do it. Treat this like onboarding as a junior engineer, not like a
syntax reference.

## How each module works

Every module folder (`modules/NN_topic_name/`) contains:

- **`LESSON.md`** — a short concept explanation, a **reading exercise** (a
  real-ish snippet of code with questions about what it does and why), and
  a **"check your understanding"** question at the end — answer it in your
  own words before moving on. Read the lesson first, don't skip it — the
  writing exercise builds on it.
- **`exercise.py`** — a stub file with `TODO`s. This is the **writing
  exercise**. You edit this file.
- **`test_NN.py`** (e.g. `test_01.py`) — a `pytest` suite. Run it from the
  terminal; it fails until your `exercise.py` is correct. This is your
  feedback loop — no need to ask "is this right?", the tests tell you.
  It's numbered per module rather than sharing one name across modules so
  that running `pytest` from the project root (not just from inside a
  single module) never collides between modules.
- **`hints.md`** — if you're stuck, this has 2-3 progressive nudges before
  the full solution. Asking for a hint isn't giving up; it's normal.
- **`solutions/solution.py`** — a reference solution. It's there on purpose,
  not hidden — but try to get the tests passing yourself first before
  peeking. Compare your approach to it afterwards either way; that
  comparison is often where the real learning happens.

### The teaching shape: told → try → compounds

Every module is built the same way: **you're told** the concept plainly (not
left to infer it), **you're given a chance to try it** with a worked example
shown first so you're not guessing cold, and then **it compounds forward**
— from Module 02 onward, each module's exercises deliberately reuse at
least one thing from the module right before it, not just its own new
material in isolation. The Phase-ending review modules (05, 10, 15) are the
periodic version of this; the compounding itself is meant to happen every
module, not just every four or five.

### The loop, every module

1. Read `LESSON.md`.
2. Open `exercise.py`, fill in the `TODO`s.
3. In the terminal, `cd` into the module folder and run `pytest`.
4. Stuck for more than ~10-15 minutes on one thing? Open `hints.md` — that's
   what it's for.
5. Fix things until it's all green.
6. Answer the "check your understanding" question at the bottom of
   `LESSON.md`, then peek at `solutions/solution.py` and compare notes.
7. Move to the next module.

You run everything yourself in the terminal. That's deliberate — terminal
fluency is part of the curriculum, not incidental to it. If a terminal
command or shortcut doesn't make sense, [`TERMINAL_CHEATSHEET.md`](TERMINAL_CHEATSHEET.md)
has the basics. If an error message is confusing, check
[`COMMON_ERRORS.md`](COMMON_ERRORS.md) before assuming something's badly
broken — most beginner errors are on that list.

There's a `conftest.py` at the project root that adds a friendly banner
around `pytest`'s own output (still shows the real pytest output — that's
part of learning to read errors, not something to hide). It's louder in
early modules and quiets down as the module number climbs, so it should
feel less like hand-holding as you get more comfortable.

**Using outside help — Google, asking Claude, whatever — in the middle of an
exercise is completely normal and not cheating.** Real developers do this
constantly. The tests exist so you always know objectively whether it
works, regardless of how you got there.

## Setup

Start at [`modules/00_setup_and_orientation/`](modules/00_setup_and_orientation/LESSON.md).
It'll walk you through the terminal basics, a Python virtual environment, and
installing `pytest`, before any real Python content.

The short version, for when you've done it before: this project targets
Python 3.12 (see `.python-version`), and `requirements.txt` pins exact
versions so everyone gets the same install.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Resuming a session

Once Module 00 is done, you don't need to remember which module you were on
or re-type setup steps. From the `LEARN_PYTHON` folder, run:

```bash
./start.sh
```

It activates the virtual environment, shows your progress across all
modules, and tells you exactly which module to open and what to run next.

## Syllabus

Roughly in order. Later modules will be built out as you get to them — this
list is the map, not all of it exists yet. Each phase ends with a **review
module** that mixes concepts from that phase together instead of testing
them in isolation — that's deliberate, it's the difference between
"I followed along" and "I actually retained it."

**Phase 1 — Foundations**
- `00` Setup & Orientation — terminal navigation, venv, installing pytest, running your first script
- `01` Variables, Types & the REPL — ints, floats, strings, bools, `type()`
- `02` Strings & Terminal I/O — string methods, f-strings, `input()`/`print()`
- `03` Control Flow — `if`/`elif`/`else`, booleans, comparisons
- `04` Loops & Iteration — `for`, `while`, `range`, `break`/`continue`
- `05` Review: Foundations — a small exercise mixing 01-04 together

**Phase 2 — Building blocks**
- `06` Data Structures I — lists, tuples
- `07` Data Structures II — dicts, sets
- `08` Functions — `def`, parameters, `return`, scope, default args
- `09` Errors & Debugging — reading tracebacks, `try`/`except`, print-debugging
- `10` Review: Building Blocks — mixing 06-09 together

**Phase 3 — Working with the real world**
- `11` Files & the Filesystem — `open()`, `pathlib`, working with paths
- `12` Modules, Packages & Virtual Envs (deep dive) — `import`, `pip`, `requirements.txt`
- `13` Working with External Data — JSON, CSV, a first look at `requests`/APIs
- `14` Classes & Objects — basic OOP, since it'll show up in real codebases
- `15` Review: Real World — mixing 11-14 together

**Phase 4 — Acting like a trainee dev**
- `16` Testing with pytest, properly — writing tests, not just passing them
- `17` Git & Version Control Basics — since your other projects already use it
- `18` Capstone — read and extend a simplified real script inspired by your
  own projects

## Progress

- [ ] 00 — Setup & Orientation
- [ ] 01 — Variables, Types & the REPL
- [ ] 02 — Strings & Terminal I/O
- [ ] 03 — Control Flow
- [ ] 04 — Loops & Iteration
- [ ] 05 — Review: Foundations
- [ ] 06 — Data Structures I
- [ ] 07 — Data Structures II
- [ ] 08 — Functions
- [ ] 09 — Errors & Debugging
- [ ] 10 — Review: Building Blocks
- [ ] 11 — Files & the Filesystem
- [ ] 12 — Modules, Packages & Virtual Envs
- [ ] 13 — Working with External Data
- [ ] 14 — Classes & Objects
- [ ] 15 — Review: Real World
- [ ] 16 — Testing with pytest, properly
- [ ] 17 — Git & Version Control Basics
- [ ] 18 — Capstone
