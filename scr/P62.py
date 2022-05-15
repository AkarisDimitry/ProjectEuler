import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P62(N):
	'''
	The cube, 41063625 (3453), can be permuted to produce two other 
	cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is 
	the smallest cube which has exactly three permutations of its 
	digits which are also cube.

	Find the smallest cube for which exactly five permutations of 
	its digits are cube.
	'''
	N3 = np.arange(1,10000,1, dtype=np.longlong)**3
	N3_sorted = [sorted(str(n)) for n in N3]
	for i, n in enumerate(N3_sorted):
		count = N3_sorted.count(n)
		if count > 4:
			return  N3[i]

P62(1)