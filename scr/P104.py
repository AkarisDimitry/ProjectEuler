
import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P104():
	'''
	The Fibonacci sequence is defined by the recurrence relation:

	, where  and .
	It turns out that , which contains  digits, is the first Fibonacci number for which 
	the last nine digits are - pandigital (contain all the digits  to , but not necessarily
	 in order). And , which contains  digits, is the first Fibonacci number for which the 
	 first nine digits are - pandigital.

	Given that  is the first Fibonacci number for which the first nine digits AND the last 
	nine digits are - pandigital, find .
	'''
	f1, f2 = 1, 1
	f1_m9, f1_M9, f2_m9, f2_M9 = 1,1,1,1
	idx = 2
	while True:
		#f1, f2 = f2, f1+f2

		f1_m9, f2_m9 = f2_m9, f1_m9+f2_m9
		if len(str(f1_m9)) < len(str(f2_m9)):	f1_m9, f2_m9 = int(str(f1_m9)[:20]), int(str(f2_m9)[:21])
		else:									f1_m9, f2_m9 = int(str(f1_m9)[:20]), int(str(f2_m9)[:20])

		f1_M9, f2_M9 = f2_M9, f1_M9+f2_M9
		f1_M9, f2_M9 = int(str(f1_M9)[-9:]), int(str(f2_M9)[-9:])

		idx += 1
		if is_pandigital(f2_M9):
			if is_pandigital(int(str(f2_m9)[:9])):
				print(idx, f2_m9, f2_M9)
				break
	return True

P104()