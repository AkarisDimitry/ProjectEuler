import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P6(N):
	'''
	The sum of the squares of the first ten natural numbers is,
	The square of the sum of the first ten natural numbers is,
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is.
	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	'''
	ans = np.sum( np.arange(1,N+1,1) )**2 - np.sum( np.arange(1,N+1,1)**2 )
	return ans