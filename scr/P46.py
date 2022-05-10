from functions import *
import time
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P46(N=1000000, v=False): 
	'''
	It was proposed by Christian Goldbach that every odd composite 
	number can be written as the sum of a prime and twice a square.

	9 = 7 + 2×12
	15 = 7 + 2×22
	21 = 3 + 2×32
	25 = 7 + 2×32
	27 = 19 + 2×22
	33 = 31 + 2×12

	It turns out that the conjecture was false.

	What is the smallest odd composite that cannot be written as the sum 
	of a prime and twice a square?
	'''
	primes = primes_load_upto(N=10000000)

	Odd_c = np.arange(1,N,2, dtype=np.int64)
	Odd_c = Odd_c[np.logical_not(np.isin(Odd_c, primes))]

	n1 = np.arange(1,N,1, dtype=np.int64)
	n2 = np.arange(1,100,1, dtype=np.int64)
	n1, n2 = np.meshgrid(n1, n2, indexing='xy')

	CGnumber = primes[n1] + 2*n2*n2
	notCGnumber = Odd_c[np.logical_not(np.isin(Odd_c, CGnumber)) ]

	return notCGnumber  

P46( N=6000 ) 