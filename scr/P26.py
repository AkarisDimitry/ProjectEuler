import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce
import itertools
from decimal import *

@timer
def P26(N=1000, v=False): 
	'''
	Euler discovered the remarkable quadratic formula:
	It turns out that the formula will produce 40 primes 
	for the consecutive integer values . However, when  
	is divisible by 41, and certainly when  is clearly 
	divisible by 41.

	The incredible formula  was discovered, which produces 
	80 primes for the consecutive values . The product of 
	the coefficients, −79 and 1601, is −126479.

	Considering quadratics of the form:smith 

	, where  and 

	where  is the modulus/absolute value of 
	e.g.  and 
	Find the product of the coefficients,  and , for the 
	quadratic expression that produces the maximum number 
	of primes for consecutive values of , starting with .
	'''
	
	return np.argmax( [getPeriod(n) for n in range(1,N)] )


P26()


