from functions import *
import time
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P49(N=1000000, v=False): 
	'''
	The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
	increases by 3330, is unusual in two ways: (i) each of the three terms
	 are prime, and, (ii) each of the 4-digit numbers are permutations of 
	 one another.

	There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
	 primes, exhibiting this property, but there is one other 4-digit 
	 increasing sequence.

	What 12-digit number do you form by concatenating the three terms in 
	this sequence?
	'''

	primes = primes_load_upto(10000)
	primes = primes[primes>1000]
	for n1 in primes:
		if n1+3330 in primes and n1+3330*2 in primes and is_permutation(n1, n1+3330) and is_permutation(n1, n1+3330*2):
			ans = int(n1)

	return str(ans)+str(ans+3330)+str(ans+3330*2)

P49( N=200000 ) 

