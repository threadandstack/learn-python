"""
Module 01 — Variables, Types & the REPL

Fill in each TODO. You only need arithmetic operators, type(), f-strings,
and multiple assignment for these — nothing from later modules.

Run `pytest` from this folder to check your work.
"""


def fahrenheit_from_celsius(celsius):
    """
    Convert a Celsius temperature to Fahrenheit.

    Formula: F = C * 9/5 + 32

    >>> fahrenheit_from_celsius(0)
    32.0
    """
    # TODO: implement and return the conversion
    pass


def average_of_three(a, b, c):
    """
    Return the average (mean) of three numbers.

    >>> average_of_three(1, 2, 3)
    2.0
    """
    # TODO: implement and return the average
    pass


def is_even(n):
    """
    Return True if n is even, False otherwise.

    Use the modulo operator (%) — don't use if/else, you don't need it.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    # TODO: implement using %
    pass


def describe(value):
    """
    Return a string describing the value and its type, in this exact
    format: "<value> is a <type name>"

    Use type(value).__name__ to get the type's name as a plain string,
    and an f-string to build the result.

    >>> describe(42)
    '42 is a int'
    >>> describe("hi")
    'hi is a str'
    """
    # TODO: implement and return the description string
    pass


def swap(a, b):
    """
    Return a tuple of (b, a) — i.e. the two values swapped.

    Do this using multiple assignment (a, b = b, a), then return the
    result — not by just writing `return b, a` directly. The point of this
    exercise is practicing the assignment pattern.

    >>> swap(1, 2)
    (2, 1)
    """
    # TODO: swap a and b using multiple assignment, then return them
    pass
