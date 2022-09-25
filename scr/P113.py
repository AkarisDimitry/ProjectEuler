import numpy as np
import matplotlib as plt
from functions import *
import math, copy, itertools

import time 
from functools import reduce

@timer
def P113(N=20): 
	'''
	Working from left-to-right if no digit is exceeded by the digit to its left it is called
	 an increasing number; for example, 134468.

	Similarly if no digit is exceeded by the digit to its right it is called a decreasing 
	number; for example, 66420.

	We shall call a positive integer that is neither increasing nor decreasing a "bouncy" 
	number; for example, 155349.

	As n increases, the proportion of bouncy numbers below n increases such that there are 
	only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy
	 numbers below 1010.

	How many numbers below a googol (10100) are not bouncy?
	'''		
 
	# ==== method 0 ==== # 
	def binomial(N:int, M:int) -> int:
		assert 0 <= M <= N
		return np.math.factorial(N-1) // (np.math.factorial(N-1-M) * np.math.factorial(M))

	N = 100
	ans = N*9 # flatt #
	for N in range(1, 101):
		for M in range(1, min([N, 9]) ):
			#print('creciente', N, M, clc(10, M+1), clc(N, M))
			ans += binomial(10, M+1) * binomial(N, M)

	for N in range(1, 101):
		for M in range(1, min([N, 10]) ):	
			#print('de-creciente', N, M, clc(11, M+1) , clc(N, M))
			ans += binomial(11, M+1) * binomial(N, M)

	# ==== method 1 ==== # 
	N = 100
	increasing = binomial(N + 10, 9) - 1
	decreasing = binomial(N + 11, 10) - (N + 1)
	flat = N * 9
	ans = increasing + decreasing - flat

	return ans

P113(N = 99)