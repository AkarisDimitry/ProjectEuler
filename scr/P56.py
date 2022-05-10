from functions import *
import time, copy
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P56(N=1000000, v=False): 
	'''
	A googol (10100) is a massive number: one followed 
	by one-hundred zeros; 100100 is almost unimaginably
	 large: one followed by two-hundred zeros. Despite 
	 their size, the sum of the digits in each number 
	 is only 1.

	Considering natural numbers of the form, ab, where
	 a, b < 100, what is the maximum digital sum?
	'''

	suma_max = 0
	amax, bmax = 0, 0
	for a in range(100):
		for b in range(100):
			suma = np.sum([int(n) for n in str(a**b)])
			if suma > suma_max:
				suma_max = suma
				amax, bmax = a, b 

	return suma_max

P56( N=10000 )  