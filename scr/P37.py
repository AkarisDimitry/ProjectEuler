from functions import *
import time
from decimal import *
import itertools 

@timer
def P37(N=1000000, v=False): 
	'''
	

	The number 3797 has an interesting property. Being prime itself,
	 it is possible to continuously remove digits from left to right, 
	 and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
	 we can work from right to left: 3797, 379, 37, and 3.

	Find the sum of the only eleven primes that are both truncatable 
	from left to right and right to left.

	NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

	'''
	def LRprime(N):
		for n in range(1, len(N)):
			#int(N[:-n])
			#print( int(N[n:]) , int(N[:-n]) )
			if not int(N[n:]) in primes or not int(N[:-n]) in primes:
				return False
		return True

	suma = 0
	primes = primes_load_upto(N=N)
	for n in primes[4:]:

		if LRprime(str(int(n))):
			print(1111111111111, n)
			suma += n
	return suma
	
P37( N=1000000 ) #9000000