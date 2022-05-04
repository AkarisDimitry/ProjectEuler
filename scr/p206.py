import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P206(self, N):
	'''
	Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
	where each “_” is a single digit.

	1_2_3_4_5_6_7_8_900

	1_2_3_4_5_6_7_8_9
	'''
	Nmin = 10203040506070809**0.5
	Nmax = 19293949596979899**0.5
	for n in range( 101010101, 138902662, 1):
		n2 = n*n
		if 	str(n*n)[0] == '1' and 	str(n*n)[2] == '2' and 	str(n*n)[4] == '3' and 	str(n*n)[6] == '4' and 	str(n*n)[8] == '5' and 	str(n*n)[10] == '6'  and str(n*n)[12] == '7' and 	str(n*n)[14] == '8' and 	str(n*n)[16] == '9':
			ans = n*10

	return ans