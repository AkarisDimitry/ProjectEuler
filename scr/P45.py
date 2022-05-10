from functions import *
import time
from decimal import *
import itertools 

@timer
def P45(N=1000000, v=False): 
	'''
	Triangle, pentagonal, and hexagonal numbers are generated 
	by the following formulae:
	Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
	Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
	Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

	It can be verified that T285 = P165 = H143 = 40755.

	Find the next triangle number that is also pentagonal and 
	hexagonal.
	'''
	

	n3 = np.arange(284,N,1, dtype=np.int64)
	P3 = n3*(n3+1)/2
	
	n5 = np.arange(143,N,1, dtype=np.int64)
	P5 = n5*(3*n5-1)/2
	P5f = P5[np.isin(P5, P3)]

	n6 = np.arange(143,N,1, dtype=np.int64)
	P6 = n6*(2*n6-1)
	P6f = P6[np.isin(P6, P3)]

	P = P5[np.isin(P5, P6)]
	print( P6[-1] )
	return P  

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

P45( N=150500 ) 