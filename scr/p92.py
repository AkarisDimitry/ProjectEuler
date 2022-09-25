import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P92(N=20): 
	'''
	Square digit chains
	Problem 92

	A number chain is created by continuously adding the square of the digits 
	in a number to form a new number until it has been seen before.
	For example,

	44 → 32 → 13 → 10 → 1 → 1
	85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

	Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
	loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

	How many starting numbers below ten million will arrive at 89?
	'''	
	#@jit('int64(int64)', nopython=True, fastmath=True, )#, parallel=True) # fastmath=True
	def evaluate(N):
		list89 = np.arange(0, N, 1, dtype=np.int64)
		for n in np.arange(1, N, 1, dtype=np.int64):
			num = n
			while num != 89 and num != 1:
				dig = []
				for i in range(1, 20):
					dig.append( num%10 )
					num = int(num/10)
					if num < 10: dig.append(num); break
				num = np.sum( np.array(dig)*np.array(dig) )
			if num == 89: 	list89[n] = 1
			else: 			list89[n] = 0
		return list89

	@jit('int64(int64, int64[:])', nopython=True, fastmath=True)#, parallel=True) # fastmath=True
	def evaluate_list(N, list89):
		count = 0
		for n in np.arange(1, N, 1, dtype=np.int64):
			dig = np.zeros(8, dtype=np.int64)
			num = n
			for i in range(1, 20):
				if num < 10: dig[i] = num; break
				dig[i] = num%10
				num = int(num/10)

			count += list89[np.sum( dig*dig )]
		return count

	first1000 = evaluate(1000)
	
	return evaluate_list(N, first1000)

P92(N=10**7)

# 73162890     
