from exercise import (
    average_of_three,
    describe,
    fahrenheit_from_celsius,
    is_even,
    swap,
)


def test_fahrenheit_from_celsius_freezing():
    assert fahrenheit_from_celsius(0) == 32.0


def test_fahrenheit_from_celsius_boiling():
    assert fahrenheit_from_celsius(100) == 212.0


def test_fahrenheit_from_celsius_negative():
    assert fahrenheit_from_celsius(-40) == -40.0


def test_average_of_three_basic():
    assert average_of_three(1, 2, 3) == 2.0


def test_average_of_three_all_same():
    assert average_of_three(5, 5, 5) == 5.0


def test_is_even_true_for_even():
    assert is_even(4) is True


def test_is_even_false_for_odd():
    assert is_even(7) is False


def test_is_even_zero_counts_as_even():
    assert is_even(0) is True


def test_describe_int():
    assert describe(42) == "42 is a int"


def test_describe_str():
    assert describe("hi") == "hi is a str"


def test_describe_bool():
    assert describe(True) == "True is a bool"


def test_swap_basic():
    assert swap(1, 2) == (2, 1)


def test_swap_strings():
    assert swap("first", "second") == ("second", "first")
