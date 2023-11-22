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
def P120(N )-> int:
	''' 
	<p>Let $r$ be the remainder when $(a - 1)^n + (a + 1)^n$ is divided by $a^2$.</p>
	<p>For example, if $a = 7$ and $n = 3$, then $r = 42$: $6^3 + 8^3 = 728 \equiv 42
	\mod 49$. And as $n$ varies, so too will $r$, but for $a = 7$ it turns out that
	 $r_{\mathrm{max}} = 42$.</p>
	<p>For $3 \le a \le 1000$, find $\sum r_{\mathrm{max}}$.</p>
	'''
	def max_remainder(a):
	    """Calculate the maximum remainder for a given 'a'."""
	    remainders = set()
	    n = 1
	    max_r = 0

	    while True:
	        r = ((a - 1) ** n + (a + 1) ** n) % (a ** 2)
	        if r in remainders:
	            # Break if the remainder starts repeating
	            break
	        remainders.add(r)
	        max_r = max(max_r, r)
	        n += 2

	    return max_r

	# Sum of the maximum remainders for each a in the range 3 to 1000
	return np.sum([max_remainder(a) for a in range(3, N+1)])


P120(N=1000)

