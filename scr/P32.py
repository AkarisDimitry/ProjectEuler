from functions import *
import time
from decimal import *

@timer
def P32(N=200, v=False): 
	'''
	We shall say that an n-digit number is pandigital if it makes use 
	of all the digits 1 to n exactly once; for example, the 5-digit number, 
	15234, is 1 through 5 pandigital.

	The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
	containing multiplicand, multiplier, and product is 1 through 9 pandigital.

	Find the sum of all products whose multiplicand/multiplier/product 
	identity can be written as a 1 through 9 pandigital.

	HINT: Some products can be obtained in more than one way so be sure 
	to only include it once in your sum.
	'''
	def can_be(N):
		vec = np.array([str(N).count(str(n)) for n in range(10)])>1
		return not vec.any()

	def is_pandigital19(N):
		vec = np.array([str(N).count(str(n)) for n in range(1,10)])==1
		return vec.all()

	N = np.linspace(1000, 9999, 9999-999, dtype=np.int64)
	suma = 0

	pandigitals = []
	for n in N:
		if can_be(n):
			fbn = factorize_big_number(n)
			for n1 in range(1, fbn.shape[0]):
				for n2 in itertools.combinations( factorize_big_number(n), n1):
					
					if is_pandigital19( str(np.prod(n2))+str(int(n/np.prod(n2)))+str(n) ):
						suma+=n
						pandigitals.append( n )
						print( f'{int(n/np.prod(n2))}*{np.prod(n2)}={n}' )
						break
						
	return np.sum( list(set(pandigitals)) )

P32( N=200 )