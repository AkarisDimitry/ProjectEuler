from functions import *
import time
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P48(N=1000, v=False): 
	'''
	The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
	by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii)
	 each of the 4-digit numbers are permutations of one another.

	There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
	exhibiting this property, but there is one other 4-digit increasing sequence.

	What 12-digit number do you form by concatenating the three terms in this 
	sequence?
	'''
	return str(np.sum([ int(str(n**n)) for n in range(1, N+1) ]))[-10:]

P48( N=1000 ) 