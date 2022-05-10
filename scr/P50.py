from functions import *
import time
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P50(N=1000000, v=False): 
	'''
	The prime 41, can be written as the sum of six consecutive 
	primes:
	41 = 2 + 3 + 5 + 7 + 11 + 13

	This is the longest sum of consecutive primes that adds to a prime 
	below one-hundred.

	The longest sum of consecutive primes below one-thousand that adds 
	to a prime, contains 21 terms, and is equal to 953.

	Which prime, below one-million, can be written as the sum of the most
	 consecutive primes?

	'''
	consec_max = 0
	prime_max = 0
	primes = primes_load_upto(N)

	for n1 in range(1000):
		for n2 in range(1000):

			suma  = np.sum(primes[n1:n2])
			if suma in primes and n2-n1 > consec_max:
				consec_max = n2-n1
				prime_max = suma
				print(suma, n1, n2)
			elif suma > N:
				break

	return int(suma)

P50( N=1000000 )  

