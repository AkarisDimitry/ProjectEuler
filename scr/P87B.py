import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P87(N=20): 
	'''
	The smallest number expressible as the sum of a prime square, prime cube, 
	and prime fourth power is 28. In fact, there are exactly four numbers below
	 fifty that can be expressed in such a way:

	28 = 22 + 23 + 24
	33 = 32 + 23 + 24
	49 = 52 + 23 + 24
	47 = 22 + 33 + 24

	How many numbers below fifty million can be expressed as the sum of a prime
	 square, prime cube, and prime fourth power?
	'''		
	s = time.time()
	d = {}
	p2 = np.array(primes_load_upto(int(50000000**(1./2.)) + 1), dtype=np.int64)
	p3 = np.array(primes_load_upto(int(50000000**(1./3.)) + 1), dtype=np.int64)
	p4 = np.array(primes_load_upto(int(50000000**(1./4.)) + 1), dtype=np.int64)

	for x in p4:
	   a = x**4
	   for y in p3:
	      b = y**3
	      if (a + b >= 50000000):
	         break
	      for z in p2:
	         c = z**2
	         if (a + b + c >= 50000000):
	            break
	         d[a+b+c] = 1

	print(len(d))
	print(time.time() - s)

	return 	len(d)

P87(N = 400000)