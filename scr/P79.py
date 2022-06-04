import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P79(N=20): 
	'''
	A common security method used for online banking is to ask the user for three 
	random characters from a passcode. For example, if the passcode was 531278, 
	they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
	
	The text file, keylog.txt, contains fifty successful login attempts.
	
	Given that the three characters are always asked for in order, analyse the 
	file so as to determine the shortest possible secret passcode of unknown length.
	'''	
	def takeSecond(elem):
		return elem[1]

	file = open('../files/problem79.txt')
	vec = [ str(line[:-1]) for line in file ]

	num, count = np.zeros(10), np.ones(10) 
	for n in vec:
		for i, m in enumerate(n):
			num[int(m)] += i+1
			count[int(m)] += 1

	prob = num/count
	order = np.argsort(prob[prob>0])
	ans = np.arange(0,10,1)[prob>0][order]

	return ans

P79(N= 56000)
