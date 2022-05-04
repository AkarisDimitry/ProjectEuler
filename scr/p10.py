import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P10(N):
	'''
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
	'''
	prime = primes_load_upto(N)
	return np.sum(prime)