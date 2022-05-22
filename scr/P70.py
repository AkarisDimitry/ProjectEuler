
import numpy as np
import matplotlib as plt
from functions import *

import time 
from functools import reduce

@timer
def P70(N=20): 
	'''
	Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the 
	number of positive numbers less than or equal to n which are relatively prime to n. For 
	example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
	
	The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

	Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

	Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) 
	produces a minimum.
	'''

	primes = primes_load_upto(N)
	primes = primes[primes<5000]
	primes = primes[primes>2000]

	vec, vec1, xvec1 = [], [], []
	nphi_max = 10
	nmax = 0
	for i1, n1 in enumerate(primes):
		for i2, n2 in enumerate(primes):
			p = n1*n2
			phi = phi_2primes(n1, n2, p)
			nphi = p/phi
			if p<10000000 and nphi < nphi_max and is_permutation(int(p), int(phi) ):
				nmax = p
				nphi_max = nphi
				print(nmax, nphi_max)

	return nmax

P70(N=10000000)
