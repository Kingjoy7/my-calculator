import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root


# --- Addition Tests ---
def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2


# --- Subtraction Tests ---
def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
    assert subtract(-1, -1) == 0


# --- Multiplication Tests ---
def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_with_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, 2) == -6


# --- Division Tests ---
def test_divide_positive_numbers():
    assert divide(10, 2) == 5


def test_divide_negative_numbers():
    assert divide(-9, 3) == -3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


# --- Power Tests ---
def test_power_positive():
    assert power(2, 3) == 8


def test_power_negative():
    assert power(2, -1) == 0.5


# --- Square Root Tests ---
def test_square_root_positive():
    assert square_root(16) == 4


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-9)
