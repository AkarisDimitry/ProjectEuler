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
	u = [0, 0, 1, 0]
	a = [0, 1, 1, 1]

	n = 3
	N = 6
	while True:
	    a.append((a[-1] + a[-2] + a[-4]) % 10**N)
	    a.append((a[-1] + a[-2] + a[-4]) % 10**N)
	    
	    n += 2
	    
	    w = (u[n-2] + u[n-3]) % 10**N
	    v = (w + a[(n-1)//2]) % 10**N
	    
	    u += [v, w]
	    
	    if w == 0 or v == 0:
	        break

	return n-1

P710()


