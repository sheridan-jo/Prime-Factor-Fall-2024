"""
Python Development II
Assignment 3 - Prime Factors
Test Suite for prime.py module
John O.
October 12, 2024

This test suite ensures that the function, generate_prime_factors() in the module, prime.py, works correctly. It
verifies that the function can handle any integer entered, including numbers less than two. It also verifies that it
can handle errors resulting from non-integer input.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import pytest
import prime

#  Verify that ValueError is raised when generate_prime_factors() is called with non-integer argument
def test_non_integer():
    with pytest.raises(ValueError):
        prime.generate_prime_factors(3.14)

#  Verify that an empty list is returned when generate_prime_factors() is called with 1
def test_number_is_1():
    assert prime.generate_prime_factors(1) == []

# Verify that list [2] is returned when generate_prime_factors() is called with 2
def test_number_is_2():
    assert prime.generate_prime_factors(2) == [2]

# Verify that list [3] is returned when generate_prime_factors() is called with 3
def test_number_is_3():
    assert prime.generate_prime_factors(3) == [3]

# Verify that list [4] is returned when generate_prime_factors() is called with 4
def test_number_is_4():
    assert prime.generate_prime_factors(4) == [2,2]

# Verify that list [2,3] is returned when generate_prime_factors() is called with 6
def test_number_is_6():
    assert prime.generate_prime_factors(6) == [2,3]

# Verify that list [2,2,2] is returned when generate_prime_factors() is called with
def test_number_is_8():
    assert prime.generate_prime_factors(8) == [2,2,2]
