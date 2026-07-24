# Common Errors

Python's error messages (tracebacks) look alarming at first — a wall of red
text. In practice, the last line almost always tells you exactly what went
wrong, and most errors you'll hit as a beginner are on this list. When you
hit something new, read the **last line first**, then work upward.

This list will grow as the curriculum does — if you hit something confusing
that isn't here, ask, and it'll get added.

---

### `NameError: name 'x' is not defined`

You used a variable or function name that Python doesn't know about yet.
Usually a typo, or you're using something before you've assigned it.

```python
print(totl)  # meant "total" — NameError: name 'totl' is not defined
```

**Check:** spelling, and that the assignment (`x = ...`) actually ran
*before* the line that uses `x`.

---

### `IndentationError: expected an indented block` (or `unexpected indent`)

Python uses indentation (spaces at the start of a line) to know what's
"inside" a function, loop, or `if` block — it's not just style, it's
syntax. This error means your indentation doesn't line up with what Python
expects.

```python
def greet(name):
print(f"hi {name}")  # IndentationError — this line needs to be indented
```

**Check:** is the line after a `:` (like `def`, `if`, `for`) indented? Are
you mixing tabs and spaces? Most editors handle this for you once you save
with consistent settings — if in doubt, use 4 spaces, never tabs.

---

### `SyntaxError: ...`

Python couldn't parse your code at all — usually a missing colon, missing
closing bracket/quote, or a typo in the structure itself. This happens
*before* your code even runs.

```python
def greet(name)      # SyntaxError — missing colon
    return f"hi {name}"
```

**Check:** the line the error points to, and the line just above it —
often the real problem (an unclosed bracket or quote) is one line earlier
than where Python notices something's wrong.

---

### `TypeError: ...`

You used a value in a way its type doesn't support — e.g. mixing types
that can't combine that way, or calling something with the wrong number of
arguments.

```python
"age: " + 25   # TypeError: can only concatenate str (not "int") to str
```

**Check:** the message usually tells you exactly which types clashed. Fix
here: `"age: " + str(25)`.

---

### `AttributeError: 'X' object has no attribute 'y'`

You tried to use `.y` on something that doesn't have it — often because the
value isn't the type you thought it was.

```python
name = "Brendan"
name.append("!")   # AttributeError — strings don't have .append (lists do)
```

**Check:** what type is the thing actually? (`print(type(name))` in the
REPL is your friend here.)

---

### `ModuleNotFoundError: No module named 'X'`

Python can't find a package you tried to `import`. Almost always one of:
- You forgot to activate your virtual environment (`source .venv/bin/activate`)
- You never `pip install`-ed it in this environment
- A typo in the module name

**Check:** is `(.venv)` showing in your prompt? If not, that's usually it.

---

### `ZeroDivisionError: division by zero`

Exactly what it says — you divided by zero somewhere (`x / 0`). Usually
means a variable you expected to be non-zero ended up being zero; trace
back where it got its value.

---

### `IndexError: list index out of range`

You asked for a position in a list (or string) that doesn't exist —
commonly off-by-one (asking for index `len(x)` instead of `len(x) - 1`, or
looping one step too far).

---

### `KeyError: 'x'`

Same idea as `IndexError`, but for dictionaries — you asked for a key that
isn't in the dict. Check spelling, and whether the key was ever actually
added.

---

### `AssertionError` (from pytest)

This one's different — it's not "your code is broken," it's pytest telling
you "your code ran, but the result didn't match what was expected." This is
the *normal*, expected shape of a failing test in this curriculum. Read the
lines above it:

```
>       assert is_even(4) is True
E       assert None is True
E        +  where None = is_even(4)
```

`E` lines show you the actual value your function returned (`None`, here —
meaning the function didn't `return` anything yet) versus what was
expected (`True`). This is usually the most informative error you'll see —
it's pointing at exactly the gap between what you wrote and what's needed.

---

### General debugging approach when you're lost

1. Read the **last line** of the traceback first — that's the actual error.
2. Find the **file and line number** just above it — that's where it
   happened.
3. If it's inside your own `exercise.py`, that's almost certainly where the
   fix goes.
4. Try printing the value in question (`print(some_variable)`) right before
   the line that fails, rerun, and look at what it actually is versus what
   you assumed it was.
