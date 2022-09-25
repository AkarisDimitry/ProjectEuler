import numpy as np
import matplotlib as plt
from functions import *
import math, copy
from decimal import *

import time 
from functools import reduce
getcontext().prec = 110

@timer
def P80(N=20): 
	'''
	It is well known that if the square root of a natural number is not
	 an integer, then it is irrational. The decimal expansion of such square
	 roots is infinite without any repeating pattern at all.

	The square root of two is 1.41421356237309504880..., and the digital sum 
	of the first one hundred decimal digits is 475.

	For the first one hundred natural numbers, find the total of the digital 
	sums of the first one hundred decimal digits for all the irrational square roots.
	'''	
	return np.sum([int(str(Decimal(n).sqrt())[0]) + np.sum([int(m) for m in str(Decimal(n).sqrt())[2:101] ]) if not int(n**0.5) == n**0.5 else 0  for n in range(N)])

P80(N= 100)
