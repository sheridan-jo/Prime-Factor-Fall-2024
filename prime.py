"""
Python Development II
Assignment 3 - Prime Factors
John O.
October 9, 2024

This program contains a function that generates the prime factors of the number entered. 

Usage:
Enter an integer as the argument for the generate_prime_factors() function, and it will return
a list containing the set of prime numbers which are multiplied by one another to form the
number entered.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

def generate_prime_factors(number):
    """
        Generates a list of the prime factors for the number that the user inputs.

        Parameters:
        number(int): The number for which prime factors are generated. It must be an integer greater than one.

        Returns:
        list of int: A list of the prime numbers that multiply together to make 'number'.
    """

    #  Raises a ValueError if 'number' is not an integer
    if not isinstance(number, int):
        raise ValueError(f'{number} is not an integer.')

    prime_factors = []  # The list which contains the prime factors for the 'number' parameter

    #  Returns an empty list if 'number' is less than 2, because in that case it cannot be a prime number
    if number < 2:
        return prime_factors