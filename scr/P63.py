import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P63(N):
	'''
	The 5-digit number, 16807=75, is also a fifth power. 
	Similarly, the 9-digit number, 134217728=89, is a ninth power.

	How many n-digit positive integers exist which are 
	also an nth power?
	'''
	count = 0
	for n in range(1, 22):
		for m in range(1,10):
			if n == len(str(m**n)): 
				#print(f'{m}**{n}={m**n}')
				count += 1

	return count

P63(1)