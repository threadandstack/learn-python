# Hints — Module 01

Stuck on one of the five functions for more than ~10-15 minutes? That's
normal, not a sign you're behind. Work through the hints for that specific
function in order — each one gives away a bit more. Try to stop as soon as
the hint unblocks you rather than reading all three every time.

If your editor/viewer supports it, the sections below are collapsible
(click to expand). If not, just read them in order — level 1 first.

## `fahrenheit_from_celsius`

<details><summary>Hint 1</summary>

The formula is given to you in the docstring: `F = C * 9/5 + 32`. You just
need to write that as a Python expression using the `celsius` parameter,
and `return` it.
</details>

<details><summary>Hint 2</summary>

Remember `return` is required — a function that just *calculates* a value
without `return`ing it gives back `None`, which is why the tests show
`assert None == 32.0` when this isn't implemented yet.
</details>

<details><summary>Hint 3 (near-solution)</summary>

```python
def fahrenheit_from_celsius(celsius):
    return celsius * 9 / 5 + 32
```
</details>

## `average_of_three`

<details><summary>Hint 1</summary>

"Average" means: add them all up, then divide by how many there are.
</details>

<details><summary>Hint 2</summary>

You have exactly three parameters (`a`, `b`, `c`) — no need for anything
fancier than `+` and `/`.
</details>

<details><summary>Hint 3 (near-solution)</summary>

```python
def average_of_three(a, b, c):
    return (a + b + c) / 3
```
</details>

## `is_even`

<details><summary>Hint 1</summary>

Re-read the modulo (`%`) explanation in `LESSON.md`. What does `n % 2` give
you when `n` is even? When it's odd?
</details>

<details><summary>Hint 2</summary>

You don't need `if`/`else` here — a comparison like `x == y` already
produces a `True`/`False` value directly, which you can `return` as-is.
</details>

<details><summary>Hint 3 (near-solution)</summary>

```python
def is_even(n):
    return n % 2 == 0
```
</details>

## `describe`

<details><summary>Hint 1</summary>

You need two pieces: the value's type name (`type(value).__name__`) and an
f-string to combine it with the value itself.
</details>

<details><summary>Hint 2</summary>

An f-string can embed more than one thing: `f"{a} and {b}"`. You need
`value` and `type(value).__name__` both inside one f-string, in the exact
format `"<value> is a <type name>"`.
</details>

<details><summary>Hint 3 (near-solution)</summary>

```python
def describe(value):
    return f"{value} is a {type(value).__name__}"
```
</details>

## `swap`

<details><summary>Hint 1</summary>

Re-read the "Multiple assignment" section of `LESSON.md`. The pattern
`a, b = b, a` does the swap in one line — the whole right-hand side gets
evaluated before either assignment happens.
</details>

<details><summary>Hint 2</summary>

The docstring is explicit: do the swap using `a, b = b, a` *inside* the
function, then `return` the (now swapped) `a` and `b`. Returning two values
separated by a comma (`return a, b`) automatically gives you a tuple back.
</details>

<details><summary>Hint 3 (near-solution)</summary>

```python
def swap(a, b):
    a, b = b, a
    return a, b
```
</details>
