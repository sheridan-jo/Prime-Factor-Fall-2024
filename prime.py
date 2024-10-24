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
        number(int): The number for which prime factors are generated.

        Returns:
        list of int: A list of the prime numbers that multiply together to make 'number'.
    """

    #  Raises a ValueError if 'number' is not an integer
    if not isinstance(number, int):
        raise ValueError(f'{number} is not an integer.')

    prime_factors = []  # The list which contains the prime factors for the 'number' parameter

    #  Returns an empty list if 'number' is less than 2
    if number < 2:
        return prime_factors

    #  Checks for divisibility by 2
    #  Executes until 'number' is no longer divisible by 2
    while number % 2 == 0:
        prime_factors.append(2)  # Adds 2 to 'prime_factors' list while the loop condition is True
        number //= 2  # Divides 'number' by 2 and assigns it a new value

    #  Handling of numbers whose prime factors are larger than 2

    odd_factor = 3  #  Used to check if 'number' is divisible by prime numbers larger than 2

    #  Executes while 'odd_factor' is less than or equal to 'number'
    while odd_factor <= number:

        #  Checks whether 'odd_factor' divides evenly into 'number' on each iteration
        if number % odd_factor == 0:
            prime_factors.append(odd_factor) #  Appends 'odd_factor' to list
            number //= odd_factor  #  Divides 'number' by 'odd_factor' and assigns it a new value
        else:
            odd_factor += 2  #  Increments odd_factor by 2

    #  If 'number' is still greater than 1 it is a prime factor and appended to the list
    if number > 1:
        prime_factors.append(number)

    return prime_factors  # List of prime factors for 'number' parameter is returned
