
import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P16(N=20): 
	'''
	If the numbers 1 to 5 are written out in words: 
	one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
	letters used in total.

	If all the numbers from 1 to 1000 (one thousand) 
	inclusive were written out in words, how many 
	letters would be used?

	NOTE: Do not count spaces or hyphens. For example, 
	342 (three hundred and forty-two) contains 23 letters 
	and 115 (one hundred and fifteen) contains 20 letters. 
	The use of "and" when writing out numbers is in 
	compliance with British usage.
	'''
				  # 1 2 3 4 5 6 7 8 9
	return ((	np.sum([3,3,5,4,4,3,5,5,4]) * 9 	+
				  # 10 11 12 13 14 15 16 17 18 19
			np.sum([3, 6, 6, 8, 8, 7, 7, 9, 8, 8]) 		+
			 	  # 20 30 40 50 60 70 80 90
			np.sum([6, 6, 5, 5, 5, 7, 6, 6]) * 10 )*10 +
				  # 100
			np.sum([7 ]) *100*9+
				  # and
			np.sum([3 ]) *99*9+
				  # 1 2 3 4 5 6 7 8 9 
			np.sum([3,3,5,4,4,3,5,5,4]) * 100 + 11)

print(P16())