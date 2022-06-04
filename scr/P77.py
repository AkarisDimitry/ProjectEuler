import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer

def P77(N=20): 
	'''
	It is possible to write ten as the sum of primes in exactly five different ways:

	7 + 3
	5 + 5
	5 + 3 + 2
	3 + 3 + 2 + 2
	2 + 2 + 2 + 2 + 2

	What is the first value which can be written as the sum of primes in over five thousand different ways?
	'''	
	primes = primes_load_upto(1000)
	data = { 0:{n:0 if n%2==1 else 1 for n in range(N+1)} }
	for i, n in enumerate(primes[1:N]):
		# n suma total
		data[i+1] = {}
		for m in range(1, N+1):
			# usando m primeros primos
			data[i+1][m] = np.sum([data[i][m-k*n] for k in range(int(m/n) )])
			data[i+1][m] += data[i][m%n] if m%n > 0 else 1

	for item, value in data[N-1].items():
		if value > 5000: break

	return item 

P77(N=100)
