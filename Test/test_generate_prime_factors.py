"""
Python Development II
Assignment 3 - Prime Factors
Test Suite for prime.py module
John O.
October 8, 2024

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
