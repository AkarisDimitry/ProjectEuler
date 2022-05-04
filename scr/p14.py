import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P14(N, v=False):
	'''
	The following iterative sequence is defined for the set of positive integers:
	n → n/2 (n is even)
	n → 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:
	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
	Which starting number, under one million, produces the longest chain?
	NOTE: Once the chain starts the terms are allowed to go above one million.
	'''
	def finder(Ni):
		N0 = Ni
		l = 1
		while Ni != 1:
			Ni = Ni/2 if Ni%2==0 else 3*Ni+1
			if Ni < N0: 
				l += L[int(Ni)]
				break
			else:
				l += 1
		return l

	L = np.zeros(N)
	for n in range(1,N):
		L[n] = finder(n)

	return np.argmax(L), np.max(L)
