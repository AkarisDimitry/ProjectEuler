from functions import *
import time
from decimal import *
import itertools 

@timer
def P35(N=1000000, v=False): 
	'''
	The number, 197, is called a circular prime because 
	all rotations of the digits: 197, 971, and 719, are 
	themselves prime.
	There are thirteen such primes below 100: 2, 3, 5, 7, 
	11, 13, 17, 31, 37, 71, 73, 79, and 97.
	How many circular primes are there below one million?
	'''
	def if_circular(N):
		return np.array([ len(factorize_big_number(n)) == 1 for n in list(set([ int(''.join(m)) for m in list(itertools.permutations(str(N)))]))]).all()
	
	def if_circular(N):
		Nstr = str(int(N))
		for n in range(len(Nstr)):
			if not int(Nstr[n:]+Nstr[:n]) in primes:
				return False
		return True

	circular_primes = []
	primes = primes_load_upto(N=N)
	for n in primes:
		nstr = str(int(n))
		if not n in circular_primes and not '2' in nstr and not '5' in nstr  and not '0' in nstr and not '4' in nstr and not '6'  in nstr and not '8' in nstr and if_circular( int(n) ):
			circular_primes += list([int(nstr[n:]+nstr[:n]) for n in range(len(nstr))])

	return len( list(set(circular_primes))) + 2
	
P35( N=1000000 ) #9000000