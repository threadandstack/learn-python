# Terminal Cheat Sheet

Things that are second nature once you know them, invisible until someone
tells you. Keep this open in a tab for the first few modules.

## Moving around

| Command | What it does |
|---|---|
| `pwd` | Print working directory — "where am I?" |
| `ls` | List what's in the current folder |
| `ls -la` | List everything, including hidden files (dotfiles like `.venv`), with details |
| `cd foldername` | Move into `foldername` |
| `cd ..` | Move up one level (to the parent folder) |
| `cd` (no argument) | Jump straight back to your home folder |
| `cd -` | Jump back to whatever folder you were in before your last `cd` |

## Keyboard shortcuts that will save you real time

| Shortcut | What it does |
|---|---|
| **↑ / ↓** | Cycle through your previous commands — don't retype a command you just ran, press ↑ instead |
| **Tab** | Autocomplete a file/folder name or command — start typing `cd mod` then hit Tab, it'll finish it for you (and won't let you typo a path that doesn't exist) |
| **Ctrl+C** | Interrupt/kill whatever's currently running. Stuck in a hung command, an infinite loop, or the REPL? This is your escape hatch |
| **Ctrl+L** | Clear the screen (same as typing `clear`) — doesn't erase your command history, just the visual clutter |
| **Ctrl+A** | Jump to the start of the current line you're typing |
| **Ctrl+E** | Jump to the end of the current line you're typing |
| **Ctrl+D** | Exit the current shell or REPL (equivalent to typing `exit()` in the Python REPL) |

## Running Python

| Command | What it does |
|---|---|
| `python3` | Open the interactive REPL — type expressions, see results immediately |
| `python3 filename.py` | Run a script file |
| `exit()` or Ctrl+D | Leave the REPL |

## Virtual environments (see Module 00 for the full explanation)

| Command | What it does |
|---|---|
| `python3 -m venv .venv` | Create a virtual environment in a folder called `.venv` |
| `source .venv/bin/activate` | Turn it on for the current terminal session — you'll see `(.venv)` appear in your prompt |
| `deactivate` | Turn it off |

**A venv only stays active for the terminal tab/session you activated it in.**
Opened a new tab? You'll need to `source .venv/bin/activate` again from the
`LEARN_PYTHON` folder — this is the single most common "why isn't this
working" moment for beginners, and it's not a bug, it's just how shells work.

## Running the exercises

| Command | What it does |
|---|---|
| `pytest` | Run every test in the current folder |
| `pytest -q` | Same, but quieter/more compact output |
| `pytest -v` | Same, but more verbose — shows every individual test name |

## When something looks broken

Before assuming you've broken something:
1. Run `pwd` — are you actually in the folder you think you're in?
2. Is `(.venv)` showing in your prompt? If not, `activate` it.
3. Check [`COMMON_ERRORS.md`](COMMON_ERRORS.md) — the error you're seeing is
   very likely on that list.
