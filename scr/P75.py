import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer

def P75(N=20): 
	'''
	It turns out that 12 cm is the smallest length of wire that can be bent to 
	form an integer sided right angle triangle in exactly one way, but there are
	 many more examples.

	12 cm: (3,4,5)
	24 cm: (6,8,10)
	30 cm: (5,12,13)
	36 cm: (9,12,15)
	40 cm: (8,15,17)
	48 cm: (12,16,20)

	In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
	sided right angle triangle, and other lengths allow more than one solution to be 
	found; for example, using 120 cm it is possible to form exactly three different
	 integer sided right angle triangles.

	120 cm: (30,40,50), (20,48,52), (24,45,51)

	Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly 
	one integer sided right angle triangle be formed?
	'''	
	@jit('int64[:](int64[:])', nopython=True)#, fastmath=True, parallel=True) #, 
	def check(M):
		count = np.zeros(1500001, dtype=np.int64)
		for m in M:
			for n in range(1, m):
				if gcd(m, n) == 1 and (m+n)%2==1:
					A = 2*n*m
					B = m*m - n*n
					C = m*m + n*n
					L = A+B+C
					Lk = L
					while  Lk <= 1500000:
						count[Lk] += 1
						Lk += L
		return count
 
	count = check(np.arange(0, 1000, dtype=np.int64) )
	return count[count==1].shape

P75(N=1500000)
