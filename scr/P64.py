import numpy as np
import matplotlib as plt
from functions import *
import time, decimal
from functools import reduce

@timer
def P64(N):
	'''
	https://projecteuler.net/problem=64

	All square roots are periodic when written as continued 
	fractions and can be written in the form:
	For example, let us consider
	If we continue we would get the following expansion:
	The process can be summarised as follows:
	It can be seen that the sequence is repeating. For conciseness,
	 we use the notation
	, to indicate that the block (1,3,1,8) repeats indefinitely.
	The first ten continued fraction representations of (irrational)
	 square roots are:
	, period=Exactly four continued fractions, for
	, have an odd period.
	How many continued fractions for
	have an odd period?
	'''

	odd = 0
	for n in range(2, N):
		if continued_fraction_period_prec(n)%2==1:
			odd+=1

	return odd

P64(10000)	