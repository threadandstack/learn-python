# 01 — Variables, Types & the REPL

## Concepts

**A variable is a name bound to a value.** `x = 5` doesn't declare a box
called `x` that holds `5` forever — it points the name `x` at the value `5`,
right now. You can point it somewhere else later: `x = "hello"` is completely
legal, even though `x` used to mean a number. Python doesn't make you declare
what *type* of thing a variable will hold up front (unlike languages like
Java or C) — this is called **dynamic typing**.

**Built-in types you'll use constantly:**

| Type | Example | Meaning |
|---|---|---|
| `int` | `42` | whole number |
| `float` | `3.14` | decimal number |
| `str` | `"hello"` | text, in quotes |
| `bool` | `True` / `False` | boolean, capitalized |
| `NoneType` | `None` | "nothing" / absence of a value |

You can check what type something is with the built-in `type()` function:
`type(42)` gives you `<class 'int'>`.

**Arithmetic operators:** `+` `-` `*` `/` all do what you'd expect, but note:
- `/` always gives you a `float` back, even `4 / 2` gives `2.0`, not `2`.
- `//` is **floor division** — `7 // 2` is `3` (division, then round down).
- `%` is **modulo** — the *remainder* after division. `7 % 2` is `1`.
  Modulo is how you test "is this number divisible by that one" — a number
  is even exactly when `n % 2 == 0`.
- `**` is exponent — `2 ** 3` is `8`.

**f-strings** let you embed variables directly inside a string:
`f"{name} is {age} years old"`. The `f` before the opening quote is what
turns on this behavior — without it, `{name}` would just be literal text.
We'll cover strings properly in Module 02; for now just recognize the
pattern.

**Multiple assignment:** Python lets you assign several variables in one
line: `a, b = 1, 2`. This also lets you swap two variables without a
temporary variable: `a, b = b, a` — the right-hand side is fully evaluated
*before* any assignment happens, so this genuinely swaps them rather than
overwriting `a` before `b` gets a chance to read it.

**The REPL.** Run `python3` with no arguments in your terminal and you get
an interactive prompt (`>>>`) where you can type expressions and see results
immediately — no file needed. It's the fastest way to check "wait, what does
this actually do?" Try it now: type `python3`, then try `2 ** 10`, then
`type("hi")`, then `exit()` to leave.

## Reading exercise

Try to work out what each `print` outputs before running it — using the
"Concepts" section above, not guessing blind. If you're not sure, a guess
is still worth writing down; you'll check it against the real output in a
second either way, so there's no way to get this "wrong" in any way that
matters.

```python
a = 7
b = 2
c = a / b
d = a // b
e = a % b
f = (a == 7)
g = "a is " + str(a)
a, b = b, a

print(c, type(c))
print(d, type(d))
print(e)
print(f, type(f))
print(g)
print(a, b)
```

### Worked example

**Q: What do you predict `c` and `d` are, and why are they different
despite both starting from `a / b`-style division?**

Reasoning: the Concepts section above says `/` always returns a `float`,
even when the numbers divide evenly, and `//` is floor division — divide,
then round down. `a` is `7`, `b` is `2`. `7 / 2` is `3.5` exactly, so
`/` just gives that back as a float: `3.5`. `7 // 2` divides the same way
(`3.5`) but then rounds down to the nearest whole number: `3` — and
because `//` is specifically the "give me a whole number" operator, that
`3` comes back as an `int`, not a float.

**A: `c` is `3.5` (a `float`). `d` is `3` (an `int`).**

### Now try these the same way

1. What does line `g = "a is " + str(a)` need the `str(a)` for? What
   happens if you write `g = "a is " + a` instead (try it — read the error
   message it gives you)?
2. After the `a, b = b, a` line, what are `a` and `b`? Walk through *why*,
   not just what.

Then actually run the code (paste it into the REPL, or save as a scratch
file and `python3` it) and check your reasoning against the real output.

## Writing exercise

Open `exercise.py`. There are five functions with `TODO`s — no control flow
(`if`, loops) needed for any of them, just what's covered above:
arithmetic, `type()`, f-strings, and multiple assignment.

Run `pytest` from this folder once you've filled them in. Stuck on any one
of them for a while? `hints.md` has progressive nudges per function — that's
what it's there for, not a last resort. When it's all green, compare your
solutions to `solutions/solution.py`.

## Check your understanding

Before moving on, answer in your own words (no need to write it down,
just make sure you actually *could*):

> Why does `4 / 2` give you `2.0` instead of `2` in Python? And what's the
> difference between `/` and `//` — when would you actually want `//`?

If that's fuzzy, go back and try a few examples in the `python3` REPL
before moving to Module 02 — this distinction (float division vs. floor
division) comes up constantly and is worth being solid on now.
