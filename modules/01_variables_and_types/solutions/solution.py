"""
Reference solution for Module 01. Compare against your own exercise.py
after you've got the tests passing yourself — don't copy this in before
you've had a real go.
"""


def fahrenheit_from_celsius(celsius):
    return celsius * 9 / 5 + 32


def average_of_three(a, b, c):
    return (a + b + c) / 3


def is_even(n):
    return n % 2 == 0


def describe(value):
    return f"{value} is a {type(value).__name__}"


def swap(a, b):
    a, b = b, a
    return a, b
