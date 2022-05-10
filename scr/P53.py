from functions import *
import time, copy
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P53(N=1000000, v=False): 
	'''
	There are exactly ten ways of selecting three from five, 12345:

	123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
	In combinatorics, we use the notation,

	In general,
	, where , , and

	It is not until
	, that a value exceeds one-million:

	How many, not necessarily distinct, values of
	for , are greater than one-million?
	'''
	def combinatorics(n,r):		return np.math.factorial(n) / (np.math.factorial(r)*np.math.factorial(n-r))
	return np.sum([ combinatorics(n,r)>10**6 for n in range(1, 101) for r in range(1, n+1)  ])

P53( N=10000000 )  