"""
Python Development II
Assignment 3 - Prime Factors
Test Suite for prime.py module
John O.
October 12, 2024

This test suite ensures that the function, generate_prime_factors()
in the module, prime.py, works correctly. It verifies that the
function can handle any integer entered, including numbers less
than two. It also verifies that it can handle errors resulting
from non-integer input.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import pytest
import prime

def test_non_integer():
    """Test that a ValueError is raised when a non-integer is passed."""
    with pytest.raises(ValueError):
        prime.generate_prime_factors(3.14)

def test_number_is_1():
    """Test that an empty list is returned when 1 is passed."""
    assert prime.generate_prime_factors(1) == []


def test_number_is_2():
    """Test that [2] is returned when 2 is passed."""
    assert prime.generate_prime_factors(2) == [2]


def test_number_is_3():
    """Test that [3] is returned when 3 is passed."""
    assert prime.generate_prime_factors(3) == [3]

def test_number_is_4():
    """Test that [2, 2] is returned when 4 is passed."""
    assert prime.generate_prime_factors(4) == [2,2]

def test_number_is_6():
    """Test that [2, 3] is returned when 6 is passed."""
    assert prime.generate_prime_factors(6) == [2,3]

def test_number_is_8():
    """Test that [2, 2, 2] is returned when 8 is passed."""
    assert prime.generate_prime_factors(8) == [2,2,2]

def test_number_is_9():
    """Test that [3, 3] is returned when 9 is passed."""
    assert prime.generate_prime_factors(9) == [3,3]

def test_number_is_10():
    """Test that [2, 5] is returned when 10 is passed."""
    assert prime.generate_prime_factors(10) == [2, 5]
