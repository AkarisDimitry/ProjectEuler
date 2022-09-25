import numpy as np
import matplotlib as plt
from functions import *
import math, copy, itertools

import time 
from functools import reduce

@timer
def P112(N=20): 
	'''
	Working from left-to-right if no digit is exceeded by the digit to its left it is 
	called an increasing number; for example, 134468.

	Similarly if no digit is exceeded by the digit to its right it is called a decreasing
	 number; for example, 66420.

	We shall call a positive integer that is neither increasing nor decreasing a "bouncy"
	 number; for example, 155349.

	Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the
	 numbers below one-thousand (525) are bouncy. In fact, the least number for which the 
	 proportion of bouncy numbers first reaches 50% is 538.

	Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 
	the proportion of bouncy numbers is equal to 90%.

	Find the least number for which the proportion of bouncy numbers is exactly 99%.
	'''		

	@jit('int64(int64)', nopython=True ) # , nopython=True, 
	def eval(N):
		count = 0
		n = 99
		porcentage = 0
		while porcentage < N:
			n += 1
			num = n
			digits = np.zeros( 9 )
			pointer = 0
			while num > 0:
				digits[pointer] = num%10
				num = int(num/10)
				pointer += 1
			
			digits = digits[:pointer] 
			decresiente = digits[1:] - digits[:-1] >= 0
			creciente   = digits[1:] - digits[:-1] <= 0

			if   decresiente.all() or creciente.all():	pass
			else:						
				count += 1
				porcentage = count/n * 100
			 
		return n

	n = eval(99)

	return n

P112(N = 99)