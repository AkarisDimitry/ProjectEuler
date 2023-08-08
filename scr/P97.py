import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P97(max_decimal=10):
	'''
	The first known prime found to exceed one million digits was discovered in 1999, and 
	is a Mersenne prime of the form 2**6972593−1; it contains exactly 2,098,960 digits. Subsequently 
	other Mersenne primes, of the form 2p−1, have been found which contain more digits.

	However, in 2004 there was found a massive non-Mersenne prime which contains 
	2,357,207 digits: 28433×2**7830457+1.

	Find the last ten digits of this prime number.

	'''
	num = 1
	max_n = 10**max_decimal 
	for m in range(7830457):
		num *= 2 
		if num > max_n: num -= max_n

	return str(num*28433+1)[-max_decimal:]

P97(max_decimal = 10)