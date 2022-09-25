import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P87(N=20): 
	'''
	The smallest number expressible as the sum of a prime square, prime cube, 
	and prime fourth power is 28. In fact, there are exactly four numbers below
	 fifty that can be expressed in such a way:

	28 = 22 + 23 + 24
	33 = 32 + 23 + 24
	49 = 52 + 23 + 24
	47 = 22 + 33 + 24

	How many numbers below fifty million can be expressed as the sum of a prime
	 square, prime cube, and prime fourth power?
	'''		
	primes = np.array(primes_load_upto(50000000**0.5), dtype=np.int64)
	primes2 = primes**2
	primes3 = primes**3
	primes4 = primes**4

	@jit('int64(int64[:], int64[:], int64[:])', nopython=True) # , nopython=True, 
	def solver_indexsearch(primes2, primes3, primes4):
		Vmax = 50000000
		ppt_list = np.zeros( (500000, 100), dtype=np.int64)
		counters = np.zeros(100, dtype=np.int64)
		count = 0
		for c1 in primes2:
			
			
			if c1 > Vmax:	break
			else:
				for c2 in primes3:
					
					if c1+c2 > Vmax:	break
					else:
						for c3 in primes4:
							ppt = c1+c2+c3
							index = int(ppt/500000)

							if ppt > Vmax: break
							elif not ppt in ppt_list[:counters[index], index]:
								ppt_list[counters[index], index] = ppt
								counters[index] += 1
								count += 1 
		return count


	@jit('int64(int64[:], int64[:], int64[:])', nopython=True) # , nopython=True, 
	def solver_dict(primes2, primes3, primes4):
		Vmax = 50000000
		d = {}
		for c1 in primes2:
			if c1 > Vmax:	break
			else:
				for c2 in primes3:
					
					if c1+c2 > Vmax:	break
					else:
						for c3 in primes4:
							ppt = c1+c2+c3
							index = int(ppt/500000)

							if ppt > Vmax: break
							d[ppt] = 0
		return len(d)


	count = solver_dict(primes2, primes3, primes4)

	return 	count

P87(N = 400000)