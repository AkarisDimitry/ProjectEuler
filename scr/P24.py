import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce
import itertools

@timer
def P24(N=30000, v=False): 
	'''
	A permutation is an ordered arrangement of objects. For 
	example, 3124 is one possible permutation of the digits 
	1, 2, 3 and 4. If all of the permutations are listed 
	numerically or alphabetically, we call it lexicographic 
	order. The lexicographic permutations of 0, 1 and 2 are:

	012   021   102   120   201   210

	What is the millionth lexicographic permutation of the 
	digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
	'''
	
	for i, n in enumerate(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 10)):
		if i+1 == 1000000 and i < 1000100:
			ans = ''.join(list([str(n) for n in n] )) 
			break

	return ans


P24()
