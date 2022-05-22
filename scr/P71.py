import numpy as np
import matplotlib as plt
from functions import *
import math

import time 
from functools import reduce

@timer
@jit('int64(int64)', nopython=True)
def P71(N=20): 
	'''
	Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is 
	called a reduced proper fraction.

	If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

	1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

	It can be seen that 2/5 is the fraction immediately to the left of 3/7.

	By listing the set of reduced proper fractions dfor d ≤ 1,000,000 in ascending order of size, find 
	the numerator of the fraction immediately to the left of 3/7.
	'''	
	fract_max = 0
	nmax, dmax = 0, 0
	for d in range(1,N):
		n = int(3/7 * d)
		fract = float(n)/d
		if fract > fract_max and fract<3/7:
			fract_max = fract
			nmax, dmax = int(n), int(d)

	return nmax
P71(N=1000000) # 428570
