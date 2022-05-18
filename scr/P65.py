import numpy as np
import matplotlib as plt
from functions import *
import time, decimal
from functools import reduce

@timer
def P65(N):
	'''
	https://projecteuler.net/problem=65

	The square root of 2 can be written as an infinite continued fraction.

	The infinite continued fraction can be written, , indicates that 2 
	repeats ad infinitum. In a similar way,.

	It turns out that the sequence of partial values of continued fractions 
	for square roots provide the best rational approximations. Let us consider 
	the convergents for.

	Hence the sequence of the first ten convergents for

	are:

	What is most surprising is that the important mathematical constant,.

	The first ten terms in the sequence of convergents for e are:

	The sum of digits in the numerator of the 10th convergent is.

	Find the sum of digits in the numerator of the 100th convergent of the
	 continued fraction for.
	'''
	def euler_secuence(N):
		es = [2,1]
		for n in range(1, int(N/3 + 1)): es += [2*n,1,1]
		return es[:N]
	
	def series2fraction(series):
		numerator = 1
		denominator = series[-1]
		for e in series[::-1][1:]:
			numerator += e*denominator
			denominator, numerator = numerator, denominator
			print(f'{numerator}/{denominator}')

		return numerator, denominator

	_, numerator =  series2fraction(euler_secuence(N))

	return np.sum([ int(n) for n in str(numerator)])

P65(100)	