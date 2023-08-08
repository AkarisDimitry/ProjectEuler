import numpy as np
from scipy.spatial.distance import cdist
from scipy.spatial import KDTree

import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P816(N=14):
	'''
	We create an array of points in a two dimensional plane using the following random number generator:

	Let be the shortest distance of any two (distinct) points among .
	E.g. Find . Give your answer rounded to 9 places after the decimal point. 
	'''
	@jit('int64[:,:](int64)', nopython=True) # , nopython=True, 
	def generator(N) -> np.ndarray:

		def sn1(sn):
			return (sn*sn) % 50515093

		Nlist = np.zeros(N*2, dtype=np.int64)
		Nlist[0] = 290797

		for n in range(1, N*2):
			Nlist[n] = sn1(Nlist[n-1])

		Npoints = np.zeros((N, 2), dtype=np.int64)
		for n in range(0, N):
			Npoints[n,:] = np.array([Nlist[2*n], Nlist[2*n+1]])

		return Npoints

	@jit('float64(int64[:,:], int64)', nopython=True) # , nopython=True, 	
	def Dmin(Npoints, N):
		min_dist = 10**6
		for n1 in range(N):
			for n2 in range(n1+1,N):
				V = Npoints[n1,:] - Npoints[n2,:]
				if V[0] < min_dist and V[1] < min_dist:
					d2 = (V[0]**2 + V[1]**2)**0.5
					if min_dist > d2: min_dist = d2

		return min_dist

	Npoints = generator(N)
	print(Npoints)


	# slow #
	#min_dist = Dmin(Npoints, N)

	# To much ram #
	#min_dist = np.min(cdist(Npoints,Npoints))
	
	tree = KDTree(Npoints)
	min_dist, min_index = tree.query(Npoints, k=2)
	min_dist = np.min(min_dist[:,1])

	min_dist

	return min_dist

P816(N=20)