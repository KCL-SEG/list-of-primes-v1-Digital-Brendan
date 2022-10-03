"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from sympy import prime

def primes(number_of_primes):
    list = []

    for i in range(1, number_of_primes+1):
        list.append(prime(i))

    return list
