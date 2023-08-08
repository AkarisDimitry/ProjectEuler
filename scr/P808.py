import numpy as np
import matplotlib as plt
from functions import *

import time 
from functools import reduce

@timer
#@jit('int64(int64[:])', nopython=True) # , nopython=True, 
def P808(primes):
    '''
    Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

    We call a number a reversible prime square if:

        It is not a palindrome, and
        It is the square of a prime, and
        Its reverse is also the square of a prime.

    169 and 961 are not palindromes, so both are reversible prime squares.

    Find the sum of the first 50 reversible prime squares.
    '''

    # First, generate a list of prime numbers
    #primes = [2, 3, 5, 7, 11, 13, 17, 19, ...]  # you can use a prime number generator to get this list
    # Next, square each of those prime numbers and check if their reverse is also a square of a prime number
    reversible_prime_squares = []
    sum_of_reversible_prime_squares = 0
    for p in primes:
      square = int(p*p)

      reverse_square = int(str(square)[::-1])  # reverse the number
      sqr_rev = reverse_square**0.5
      if sqr_rev.is_integer() and int(sqr_rev) in primes and not reverse_square==square:
        reversible_prime_squares.append(square)
        sum_of_reversible_prime_squares += square

      if len(reversible_prime_squares) == 50: break

    # Finally, print the result
    return sum_of_reversible_prime_squares

primes = primes_load_upto(40000000)
primes = primes.astype(int)
P808(primes)
