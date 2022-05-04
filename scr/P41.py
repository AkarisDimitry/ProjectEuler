from functions import *
import time
from decimal import *
import itertools 

@timer
def P41(N=1000000, v=False): 
	'''
	We shall say that an n-digit number is pandigital if 
	it makes use of all the digits 1 to n exactly once. 
	For example, 2143 is a 4-digit pandigital and is also prime.

	What is the largest n-digit pandigital prime that exists?
	'''
	for prime in primes_load_upto(N=N)[::-1]:
		if is_pandigitalN(int(prime)):	break
	return int(prime)

P41( N=10000000 ) 