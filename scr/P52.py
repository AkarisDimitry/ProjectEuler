from functions import *
import time, copy
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P52(N=1000000, v=False): 
	'''
	It can be seen that the number, 125874, and its double, 251748, 
	contain exactly the same digits, but in a different order.

	Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
	and 6x, contain the same digits.
	'''
	N = np.arange(10**2, 10**8, 1, dtype=np.int64)

	for n in N:
		if is_permutation(n, n*2) and is_permutation(n, n*3) and is_permutation(n, n*4) and is_permutation(n, n*5) and is_permutation(n, n*6):
			break

	return n

P52( N=10000000 )  
