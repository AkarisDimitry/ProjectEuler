import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce
import itertools

@timer
def P21(N=10000, v=False): 
	'''
	Let d(n) be defined as the sum of proper divisors of n 
	(numbers less than n which divide evenly into n).
	If d(a) = b and d(b) = a, where a ≠ b, then a and b are 
	an amicable pair and each of a and b are called amicable numbers.

	For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
	20, 22, 44, 55 and 110; therefore d(220) = 284. 

	The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

	Evaluate the sum of all the amicable numbers under 10000.
	'''
	divisors = np.zeros(N, dtype=np.int64)
	for n in range(N):
		factors = factorize_big_number(n)
		a = set()
		for m in range(factors.shape[0]):
			a = a | set(itertools.combinations(factors, m))

		divisors[n] = int(np.sum( [ np.prod(n) for n in a ] ))

		if v:
			print('===============================')
			print('numero:',n, )
			print('Factores:',factors, )
			print('numero de factores :',factors.shape[0], )
			print('numero:',divisors[n])
			print('divisores factorizados', a)
			print('divisores',[ np.prod(n) for n in a ] )
	
	suma = 0
	for i, n in enumerate( divisors ):
		try:
			if divisors[divisors[int(i)]] == i and divisors[i] != i:
				suma += i

		except: pass

	return suma
	#divisors[divisors>N] = 0
	#oneline = np.sum( (np.linspace(1, N,N,dtype=np.int64)-1)[np.logical_and( divisors[ [*divisors] ] == np.linspace(1, N,N,dtype=np.int64)-1 , divisors !=  np.linspace(1, N,N,dtype=np.int64)-1)] ) 

