import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P15(N=20): 
	line = [1]
	[line.append( int(line[k] * (N-k) / (k+1))) for k in range(N)]
	return np.sum(np.array(line)**2)

def P15B(N=15):
	'''
	Starting in the top left corner of a 2×2 grid, and only being 
	able to move to the right and down, there are exactly 6 routes 
	to the bottom right corner.

	How many such routes are there through a 20×20 grid?
	'''
	end = np.array([N, N])
	move_down = np.array([0,1])
	move_right = np.array([1,0])

	def move(punto, counter):
		if punto[0] < N:		counter = move( punto + move_right, counter )
		if punto[1] < N:		counter = move( punto + move_down, counter )
		if (punto==end).all():	return counter+1
		return counter
	move( np.array([0,0]), 0 )

