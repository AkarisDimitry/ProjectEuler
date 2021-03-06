import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P2(N):
	'''
	Each new term in the Fibonacci sequence is generated by adding the 
	previous two terms. By starting with 1 and 2, the first 10 terms will be:
		
		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
		
		By considering the terms in the Fibonacci sequence whose values do not 
		exceed four million, find the sum of the even-valued terms.
		'''
	sec = Fibonacci(N=4000000, Fmax=N)
	ans = np.sum(sec[sec%2==0])
	return ans
