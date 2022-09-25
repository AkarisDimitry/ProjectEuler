import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P86(N=20): 
	'''
	A spider, S, sits in one corner of a cuboid room, measuring 
	6 by 5 by 3, and a fly, F, sits in the opposite corner. By 
	travelling on the surfaces of the room the shortest "straight 
	line" distance from S to F is 10 and the path is shown on the diagram.

	However, there are up to three "shortest" path candidates for
	 any given cuboid and the shortest route doesn't always have 
	 integer length.

	It can be shown that there are exactly 2060 distinct cuboids, 
	ignoring rotations, with integer dimensions, up to a maximum
	 size of M by M by M, for which the shortest route has integer 
	 length when M = 100. This is the least value of M for which the 
	 number of solutions first exceeds two thousand; the number of 
	 solutions when M = 99 is 1975.

	Find the least value of M such that the number of solutions first 
	exceeds one million.
	'''		
	
	def solver(M):
		solutions = np.zeros(M, dtype=np.int64)
		for m in range(1, M):
			count = 0
			Lx = m
			for l1 in range(1, Lx+1):
				for l2 in range(1, l1+1):
					for l3 in range(1, l2+1):
						d = (l1**2 + (l2+l3)**2)**0.5
						if int(d) == float(d):
							count += 1
			solutions[m] = count
		return solutions
	
	@jit('int64[:](int64, int64)', nopython=True, )#, parallel=True) # fastmath=True
	def CUDAsolver(M, Mmin):
		solutions = np.zeros(M, dtype=np.int64)
		for m in range(Mmin, M):
			for l1 in range(1, m+1):
				for l2 in range(1, l1+1):
					for l3 in range(1, l2+1):
						d = (l1**2 + (l2+l3)**2)**0.5
						if int(d) == float(d):
							solutions[m] += 1
		return solutions

	return CUDAsolver( 1819, 1817)[-2:] 

P86(N = 400)