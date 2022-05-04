import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P4(N):
	'''
	A palindromic number reads the same both ways. 
	The largest palindrome made from the product of two 2-digit numbers 
	is 9009 = 91 × 99.

	Find the largest palindrome made from the product of two 3-digit numbers.
	'''
	#N = [n for n in str(N)]
	biggest = 0

	for n1 in range(999, 100, -1):
		for n2 in range(n1, 100, -1):
			if n1*n2>biggest:
				if is_palindromic( [n for n in str(n1*n2)] ):
					biggest = n1*n2
			else: break
		
	ans = biggest
	return ans