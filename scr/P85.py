import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P85(N=20): 
	'''
	By counting carefully it can be seen that a rectangular grid measuring 3 by 
	2 contains eighteen rectangles:

	Although there exists no rectangular grid that contains exactly two million 
	rectangles, find the area of the grid with the nearest solution.
	'''	
	def solver(Nx, Ny):
		Nxmin, Nymin, area, solutions = np.inf,np.inf,np.inf,np.inf
		for nx in range(1, N):
			for ny in range(1, N):
				s = np.sum(np.outer(np.arange(1,nx+1,1), np.arange(1,ny+1,1)))

				if abs(2000000-s) <  solutions:
					Nxmin, Nymin, area, solutions = nx, ny, nx*ny, abs(2000000-s)

				elif s > 2000000:
					break
		return Nxmin, Nymin, area, solutions

	return solver(N, N)[2]

P85(N= 80)