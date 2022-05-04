import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P5(N):
	'''
	2520 is the smallest number that can be divided by each of the numbers 
	from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible by all of 
	the numbers from 1 to 20?
	'''
	def Diff(li1, li2):
		unique1, counts1 = np.unique(li1, return_counts=True) # list1
		unique2, counts2 = np.unique(li2, return_counts=True) # n
		dic1 = dict(zip(unique1, counts1))

		diff = []
		for i, n in enumerate(unique2):
			if n in unique1:
				if counts2[i]>dic1[n]:
					diff += [n]*(counts2[i]-dic1[n] ) 
			else:	diff  += [n]*counts2[i] 

		return diff

	list1 = [] # guardo los factores primos
	for n in range(N, 1, -1):
		if not n in list1: 
			list1 += Diff( list1, list(factorize_big_number(n) ) )

	ans = np.prod(list1, dtype=np.float64)
	return ans