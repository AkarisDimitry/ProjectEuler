import matplotlib.pyplot as plt
import numpy as np 
from functions import *
import time 
from functools import reduce
import itertools
from decimal import *

@timer
def P28(N=1001, v=False): 
	'''
	Starting with the number 1 and moving to the right in a clockwise 
	direction a 5 by 5 spiral is formed as follows:

	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13

	It can be verified that the sum of the numbers on the diagonals is 101.

	What is the sum of the numbers on the diagonals in a 1001 by 1001 
	spiral formed in the same way?
	'''

	n37 = np.linspace( 1, N+0, N*2-1, dtype=np.float64 )-1
	vec37 =  4*n37**2 + 2*n37 + 1 
	# [  1.   3.   7.  13.  21.  31.  43.  57.  73.  91. 111. 133. 157. 183. 211.]
	
	n9 = np.linspace( 1, N+0, N, dtype=np.float64 )[1:]-1
	vec9 = 4*n9**2 + 4*n9 + 1 
	# [  1.   9.  25.  49.  81. 121. 169. 225. 289. 361. 441. 529. 625. 729.  841.]
	
	n5 = np.linspace( 1.5, N+0.5, N, dtype=np.float64 )-1
	vec5 = 4*n5**2 + 4*n5 + 2 
	# [  5.  17.  37.  65. 101. 145. 197. 257. 325. 401. 485. 577. 677. 785. 901.]

	vec = np.concatenate( (vec37, vec9, vec5) )
	return np.sum( vec[vec<=(N*N)] , dtype=np.int64) 

#P28( N=1001 )

