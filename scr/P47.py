from functions import *
import time
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P47(N=1000000, v=False): 
	'''
	The first two consecutive numbers to have two distinct 
	prime factors are:

	14 = 2 × 7
	15 = 3 × 5

	The first three consecutive numbers to have three distinct
	 prime factors are:

	644 = 2² × 7 × 23
	645 = 3 × 5 × 43
	646 = 2 × 17 × 19.

	Find the first four consecutive integers to have four 
	distinct prime factors each. What is the first of these 
	numbers?
	'''
	primes = primes_load_upto(N=10000000)

	consecutive_primes = 0
	for i, n in enumerate(primes):
		if primes[i+1] - primes[i] >= 4:
			for m in range(int(primes[i])+1, int(primes[i+1])):

				#if i%1000==0: 
				#	print( consecutive_primes, primes[i+1] - primes[i], primes[i+1], primes[i], m)
				
				if len( list(set(factorize_big_number(m)))) == 4:
						consecutive_primes += 1
						if consecutive_primes == 4:
							print(m)
							break
				else: 
					if int(primes[i+1]) - m < 4: 
						consecutive_primes = 0
						break
					else:
						consecutive_primes = 0
						#break

	return n-3  

P47( N=200000 ) 