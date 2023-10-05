from sympy import prime
import time, math
import numpy as np
from itertools import product
from decimal import Decimal
from multiprocessing import Pool, cpu_count
from numba import njit, jit

# A timer decorator to measure the execution time of functions.
def timer(func):
	def wrapper(*args, **kwargs):
		before = time.time()
		r = func(*args, **kwargs)
		name = str(func).split(' ')[1]
		print(f'Result of {name} : {r} (execution time {time.time()-before}s)') 
		return r
	return wrapper

@timer
@jit
def P710(N=int(0),div:int=int(1_000_000) )-> int:
	''' 
	<h4>On Sunday 5 April 2020 the Project Euler membership first exceeded one million members. 
	We would like to present this problem to celebrate that milestone. Thank you to everyone for
	 being a part of Project Euler.</h4>

	<p>The number 6 can be written as a palindromic sum in exactly eight different ways:</p>
	$$(1, 1, 1, 1, 1, 1), (1, 1, 2, 1, 1), (1, 2, 2, 1), (1, 4, 1), (2, 1, 1, 2), (2, 2, 2), (3, 3),
	 (6)$$

	<p>We shall define a <dfn>twopal</dfn> to be a palindromic tuple having at least one element
	 with a value of 2. It should also be noted that elements are not restricted to single digits. 
	 For example, $(3, 2, 13, 6, 13, 2, 3)$ is a valid twopal.</p>

	<p>If we let $t(n)$ be the number of twopals whose elements sum to $n$, then it can be seen 
	that $t(6) = 4$:</p>
	$$(1, 1, 2, 1, 1), (1, 2, 2, 1), (2, 1, 1, 2), (2, 2, 2)$$

	<p>Similarly, $t(20) = 824$.</p>

	<p>In searching for the answer to the ultimate question of life, the universe, and everything,
	 it can be verified that $t(42) = 1999923$, which happens to be the first value of $t(n)$ that 
	 exceeds one million.</p>

	<p>However, your challenge to the "ultimatest" question of life, the universe, and everything
	 is to find the least value of $n \gt 42$ such that $t(n)$ is divisible by one million.</p>
	'''
	def pow_mod(base, exponent, mod):
	    result = 1
	    base %= mod
	    
	    while exponent > 0:
	        if exponent % 2 == 1:  # Si el exponente es impar
	            result = (result * base) % mod
	        base = (base * base) % mod  # Duplicar la base
	        exponent //= 2  # Dividir el exponente a la mitad

	    return result % mod

	pal_odd = 0
	pal_odd_0b2 = 2
	pal_odd_0b4 = 1

	twopal_odd = 0
	twopal_odd_0b2 = 1
	twopal_odd_0b4 = 0

	twopal = 0

	suma_odd = 0
	suma_even = 0

	n = 2
	mod = 10**6
	while twopal%div != 0 or n<42 :
		# === Counter === #
		n += 2 

		# === pal_odd === #
		pal_odd = pow_mod(2, int(n/2) - 1, mod) #(2**(int(n/2)-1))%mod

		# === twopal_odd === #
		twopal_odd = (suma_odd - twopal_odd_0b4 + pal_odd_0b4)%mod

		# === twopal === #
		twopal = (twopal_odd + suma_even - twopal_odd_0b2 + pal_odd_0b2)%mod

		# === cumulative sum === #
		suma_odd += twopal_odd
		suma_even += twopal_odd

		# === Reoreder === #
		pal_odd_0b2, pal_odd_0b4 = pal_odd, pal_odd_0b2
		twopal_odd_0b2, twopal_odd_0b4 = twopal_odd, twopal_odd_0b2

	return n

P710(N=42)

