import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P78(N=20): 
	'''
	It is possible to write five as a sum in exactly six different 
	ways:

	4 + 1
	3 + 2
	3 + 1 + 1
	2 + 2 + 1
	2 + 1 + 1 + 1
	1 + 1 + 1 + 1 + 1

	How many different ways can one hundred be written as a sum of at 
	least two positive integers?
	'''	
	#@jit('int64(int64)', nopython=True) 
	def P(N):
		data = { 1:{m:1 for m in range(1, N+1)} }
		for n in range(2, N+1):
			data[n] = {}
			for m in range(1, N+1):
				data[n][m] = np.sum([data[n-1][m-k*n] for k in range(int(m/n) )])
				data[n][m] += data[n-1][m%n] if m%n > 0 else 1

	@njit('uint32(uint32)', nopython=True) # fastmath=True
	def P(N):
		vec1 = np.ones(N+1, dtype=np.int32)
		for n in range(2, N+1):
			vec2 = np.zeros(N+1, dtype=np.int32)
			for m in range(1, N+1):

				for k in range(int(m/n) ):
					vec2[m] += vec1[m-k*n]
					while vec2[m] > 1000000:
						vec2[m] -= 1000000

				if m%n > 0:		vec2[m] += vec1[m%n]
				else:			vec2[m] += 1

				while vec2[m] > 10000000:
					vec2[m] -= 10000000
			
			#print(n, vec2[n])
			if vec2[n] % 1000000 == 0:
				return n
	
			vec1 = vec2 

		return 1
	
	print( P(N) )

	return True

P78(N= 56000)

# 73162890     
