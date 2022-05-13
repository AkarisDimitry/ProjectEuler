from functions import *
import time, copy
from decimal import *
from fractions import Fraction
import itertools

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P59(N=5, v=False): 
	'''
	The primes 3, 7, 109, and 673, are quite remarkable. By taking 
	any two primes and concatenating them in any order the result 
	will always be prime. For example, taking 7 and 109, both 7109 
	and 1097 are prime. The sum of these four primes, 792, represents
	 the lowest sum for a set of four primes with this property.

	Find the lowest sum for a set of five primes for which any two 
	primes concatenate to produce another prime.
	'''
	def check_num(N):
		Nsqrt = N**0.5
		for n in primes:
			if N%n == 0:		return False
			elif n>Nsqrt:		return True

	def check_prime_family(prime_family):
		print(prime_family)
		for n in	itertools.permutations(prime_family, 2):
			pass

	def check_2prime_family(prime_family):
		if check_num(int(prime_family[0]+prime_family[1])) and check_num(int(prime_family[1]+prime_family[0])):				return True
		else:			return False

	def check_3prime_family(pf):
		if check_2prime_family([pf[1], pf[2]]) and check_2prime_family([pf[0], pf[2]]):			return True
		else:			return False

	def check_4prime_family(pf):
		if check_2prime_family([pf[0], pf[3]]) and check_2prime_family([pf[1], pf[3]]) and check_2prime_family([pf[2], pf[3]]):			return True
		else:			return False
	
	def check_5prime_family(pf):
		if check_2prime_family([pf[0], pf[4]]) and check_2prime_family([pf[1], pf[4]]) and check_2prime_family([pf[2], pf[4]]) and check_2prime_family([pf[3], pf[4]]):			return True
		else:			return False

	def get_set(P, primes):
		Pset = []
		for p in primes:
			if check_2prime_family([P, str(p)]):	Pset.append(p)
		return set(Pset)

	prime_family = np.zeros(N)
	primes = primes_load_upto(10000).astype(dtype=np.int64)
	Prime_solution = [10000000, 0]

	for i1, n1 in enumerate(primes[5:]):
		n1_str = str(n1)
		n1_set = get_set(n1_str, primes[(i1+1):])
		for i2, n2 in enumerate(n1_set):
			n2_str = str(n2)
			n2_set = get_set(n2_str, primes[(i2+1):])
			n1n2_set = n2_set.intersection(n1_set)

			for i3, n3 in enumerate( n1n2_set ):
				n3_str = str(n3)
				n3_set = get_set(n3_str, primes[(i3+1):])
				n1n2n3_set = n1n2_set.intersection(n3_set)

				for i4, n4 in enumerate(n1n2n3_set):
					n4_str = str(n4)
					n4_set = get_set(n4_str, primes[(i4+1):])
					n1n2n3n4_set = n1n2n3_set.intersection(n4_set)

					for i5, n5 in enumerate(n1n2n3n4_set):
						n5_str = str(n5)
						n5_set = get_set(n5_str, primes[(i5+1):])
						n1n2n3n4n5_set = n1n2n3n4_set.intersection(n5_set)									
						#print([n1_str, n2_str, n3_str, n4_str, n5_str])

						if Prime_solution[0] > np.sum([n1, n2, n3, n4, n5]):
							print( np.sum([n1, n2, n3, n4, n5]), [n1_str, n2_str, n3_str, n4_str, n5_str] )
							Prime_solution[0] = np.sum([n1, n2, n3, n4, n5])
							Prime_solution[1] = [n1_str, n2_str, n3_str, n4_str, n5_str]
							break

	return np.sum([n1, n2, n3, n4, n5])

P59( N=5 )  # pass: exp