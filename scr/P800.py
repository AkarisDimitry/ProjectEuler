import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P800(N=20): 
	'''
	Problem 800

	An integer of the form
	with prime numbers is called a hybrid-integer.
	For example,

	is a hybrid-integer.

	We define
	to be the number of hybrid-integers less than or equal to .
	You are given and Find 
	'''	

	@jit('int64(int64[:], float64[:])', nopython=True )#, fastmath=True)#, parallel=True) # fastmath=True
	def count(primes, primes800800):
		L = primes.shape[0]
		count = np.int64(0)
		for i1,(p1, l81) in enumerate(zip(primes[::-1], primes800800[::-1])):
			for i2,(p2, l82) in enumerate(zip( primes[:(L-i1-1)], primes800800[:(L-i1-1)] )):
				if l81*p2 + l82*p1 <= 800800:
					count += 1
				else: break

		return count

	primes = np.array( primes_load_upto(18*10**6), dtype=np.int64)
	primes10 = np.log10(primes)
	primes800800 = primes10/np.log10(800800)
	return count(primes, primes800800)

P800(N= 56000)