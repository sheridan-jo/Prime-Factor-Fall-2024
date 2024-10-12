"""
Python Development II
Assignment 3 - Prime Factors
John O.
October 12, 2024

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

    #  Checks for divisibility by 2
    #  Executes until 'number' is no longer divisible by 2
    while number % 2 == 0:
        prime_factors.append(2)  # Adds 2 to 'prime_factors' list while the loop condition is True
        number //= 2  # Divides 'number' by 2 and assigns it a new value

    return prime_factors  # List of prime factors for 'number' parameter is returned
