# 00 — Setup & Orientation

No Python content yet — this module is entirely about getting your terminal
and environment ready, and proving the exercise loop (`pytest`) actually
works before we rely on it for everything else.

## Concepts

A few pieces of vocabulary, since we'll use these words constantly:

- **Terminal** — the window you type commands into (Ghostty, in your case).
- **Shell** — the program *inside* the terminal that reads your commands and
  runs them (probably `zsh` on your Mac). "Terminal" and "shell" get used
  interchangeably in casual speech; the terminal is the window, the shell is
  what's actually interpreting what you type.
- **Working directory** — the folder your shell is currently "standing in".
  Every relative path (like `modules/01_variables_and_types`) is relative to
  this. `pwd` ("print working directory") tells you where you are.
- **`python3`** — the command that runs the Python interpreter, either
  interactively (the **REPL** — Read-Eval-Print Loop) or against a script
  file.
- **Virtual environment (`venv`)** — an isolated, project-specific install of
  Python packages, so installing something for LEARN_PYTHON doesn't affect
  or get affected by your other projects. Almost every real Python project
  uses one.
- **`pip`** — Python's package installer. `pip install X` downloads and
  installs package `X` into whatever environment is currently active.
- **`pytest`** — a testing tool. You point it at a folder, it finds files
  named `test_*.py`, runs the functions inside starting with `test_`, and
  reports pass/fail.

## Reading exercise

**You are not expected to know these answers cold.** The vocabulary above
gives you words, not reasoning — the point of this exercise is to *try*
reasoning with them, not to already have the right answer. Guessing wrong,
or having no guess at all, is a completely normal place to be right now.

Here's a terminal transcript, followed by one question worked through
fully (so you can see what "reasoning through it" actually looks like),
then three more for you to try the same way.

```
$ pwd
/Users/brendanrodgers/T+S_Codebase/threadstack.dev/LEARN_PYTHON
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ cd modules/00_setup_and_orientation
(.venv) $ pytest
```

### Worked example

**Q: Why does the venv get created at the top of `LEARN_PYTHON`, not inside
the `00_setup_and_orientation` folder?**

Reasoning: a venv holds installed packages (like `pytest`) for whatever it
covers. This curriculum has many modules — `00`, `01`, `02`, and so on —
and every one of them needs `pytest` to run its tests. If the venv only
existed inside `00_setup_and_orientation`, only that one folder could use
it; each other module would need its own separate venv and its own
separate `pip install` of the same packages, over and over. Putting it at
the `LEARN_PYTHON` root means every module underneath can share it —
install once, works everywhere.

**A: To be shared by every module, not just this one.**

### Now try these the same way — reason it out, even if you're not sure

1. What does the `(.venv)` that appears in the prompt after `activate`
   tell you? (Look closely at the transcript — compare the lines before
   and after `activate` runs. What's different, and what would explain
   that difference appearing?)
2. `cd` happens *after* `pip install`, not before. Does the working
   directory matter for `pip install -r requirements.txt` the way it will
   matter for `pytest`? Why might that be? (Hint: `requirements.txt` is
   written as a bare filename, not a full path — where does a bare
   filename get looked for?)
3. Nothing was written to disk by `pytest` in this transcript (no file
   editing happened) — so what do you expect its output to be, pass or
   fail, and why? (Hint: this module doesn't ask you to write any Python
   yet — what would there even be to get wrong?)

Come back and tell me your reasoning (even a wrong guess) if you want it
checked, or just move on — either is fine.

## Writing exercise — really just "run it"

There's no code to write in this module. Your task is to actually execute
that transcript for real (adjusted to your own machine), starting from the
`LEARN_PYTHON` folder:

```bash
cd LEARN_PYTHON
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd modules/00_setup_and_orientation
pytest
```

If everything is set up right, you'll see `pytest` report **2 passed**.
Those tests aren't testing your understanding of Python — they're proving
your toolchain works, so every module after this one "just works" the same
way.

If you see an error instead, read it — don't just retry blindly. What line
of the transcript does it correspond to, and what does the error message
say went wrong? (This is the first bit of real trainee-dev skill: reading
error output instead of skimming past it.)

## Before moving on

Once `pytest` reports a pass, you're set up. `.venv` lives at the
`LEARN_PYTHON` root and covers every module — you only create it once. Every
new terminal tab/session needs `source .venv/bin/activate` run again from
the `LEARN_PYTHON` root before `pytest` will work (activation doesn't
persist between terminal sessions), but you won't need to reinstall
anything.

From here on, every module follows the same loop: `cd` into the module
folder, read `LESSON.md`, edit `exercise.py`, run `pytest`.

## Check your understanding

Before moving on, answer this out loud or in a note somewhere — not to me,
just to yourself:

> You open a brand new terminal tab tomorrow and want to work on Module 01.
> What's the very first command you need to run, and why won't `pytest`
> work if you skip it?

If you're not sure, that's a sign to reread the "Before moving on" section
above rather than push forward — this exact thing trips people up
constantly in the first week.

Head to `../01_variables_and_types/LESSON.md` next.
