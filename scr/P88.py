import numpy as np
import matplotlib as plt
from functions import *
import math, copy, itertools

import time 
from functools import reduce

@timer
def P88(N=20): 
	'''
	https://projecteuler.net/problem=88

	A natural number, N, that can be written as the sum and product of a given 
	set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum 
	number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

	For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

	For a given set of size, k, we shall call the smallest N with this property a 
	minimal product-sum number. The minimal product-sum numbers for sets of size, 
	k = 2, 3, 4, 5, and 6 are as follows.

	k=2: 4 = 2 × 2 = 2 + 2
	k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
	k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
	k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
	k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

	Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; 
	note that 8 is only counted once in the sum.

	In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 
	12, 15, 16}, the sum is 61.

	What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

	'''		

	def solver( vec ):
		S = np.sum(vec)
		P = np.prod(vec)

		p_vec = [ np.prod(vec[:i])*np.prod(vec[i+1:]) for i, n in enumerate(vec) ]

		if S > P:
			for i, p in enumerate(p_vec):
				for n in range(int(P/p)):
					vec1 = np.array(vec)
					vec1[i] += 1
					solver( vec1 )

		elif P > S:
			return False
		else:	
			print(vec, S, P)

	def S(N, M, P):
		#   N-2 + 2*M + T3 =  2**M * T3
		T3 = (N-M-1 + P*M) / (P**M-1)
		return T3 * P**M 

	@jit('int64(int64)', nopython=True,  )#, parallel=True) # fastmath=True
	def solve(N1):
		ans = np.zeros(N1+1)
		for N in range(2, N1+1):
			if N%1000==1:print(N)
			Vmin = 999999

			for M in np.arange(1, 70, dtype=np.float64):
				for P in np.arange(2,100, dtype=np.float64):
					V = (N-M-1.0 + P*M) / (P**M-1.0) * P**M
					if V < Vmin and int(V) == float(V):
						#print(N, V) 
						Vmin = V
			#vec = np.array([ (N-M-1 + P*M) / (P**M-1) * P**M  for M in range(1, 30) for P in range(2,80) ])
			#print( N, np.min(vec[F]) )
			ans[N] = Vmin

		return np.sum(np.unique(ans))

	#for n in itertools.product( np.arange(2,12000), repeat=2):
	#	if n[0]%1000==1:
	#		print(n)

	#asdproduct
	return 	solve(N)
50213
# 63048742
# 65228478
# 69111923
# 282417926
P88(N = 12000)