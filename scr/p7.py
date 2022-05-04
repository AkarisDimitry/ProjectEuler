import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P7(N):
	'''
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10 001st prime number?
	'''
	ans = primes_first_N(N)
	return ans[-1]