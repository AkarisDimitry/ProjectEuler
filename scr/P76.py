import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P76(N=20): 
	'''
	Let p(n) represent the number of different ways in which n coins can be 
	separated into piles. For example, five coins can be separated into piles 
	in exactly seven different ways, so p(5)=7.
	OOOOO
	OOOO   O
	OOO   OO
	OOO   O   O
	OO   OO   O
	OO   O   O   O
	O   O   O   O   O

	Find the least value of n for which p(n) is divisible by one million.
	'''	
	data = { 1:{m:1 for m in range(1, N+1)} }
	for n in range(2, N+1):
		data[n] = {}
		for m in range(1, N+1):
			data[n][m] = np.sum([data[n-1][m-k*n] for k in range(int(m/n) )])
			data[n][m] += data[n-1][m%n] if m%n > 0 else 1


	return int(data[N-1][N])

P76(N=3000)
