import matplotlib.pyplot as plt
import numpy as np 
from functions import *
import time 
from functools import reduce
import itertools
from decimal import *

@timer
def P30(N=1000000, v=False): 
	'''
	Surprisingly there are only three numbers that can be written as 
	the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

	As 1 = 14 is not a sum it is not included.	

	The sum of these numbers is 1634 + 8208 + 9474 = 19316.

	Find the sum of all the numbers that can be written as the sum of 
	fifth powers of their digits.
	
	'''
	Nmin = 10
	Nmax = N
	vec = np.linspace(Nmin, Nmax, Nmax-Nmin+1, dtype=np.int64)
	dfp = np.zeros(Nmax-Nmin+1) 
	for i, n in enumerate(vec):
		dfp[i] = np.sum( [int(d)**5 for d in str(n)] )

	return np.sum( vec[vec==dfp]  )

P30( N=194979 )