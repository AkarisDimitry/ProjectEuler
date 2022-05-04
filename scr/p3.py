import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P3(N):
	'''
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	'''
	ans = factorize_big_number(N)[-1]
	return ans
