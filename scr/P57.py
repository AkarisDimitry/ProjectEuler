from functions import *
import time, copy
from decimal import *
from fractions import Fraction
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P57(N=1000000, v=False): 
	'''
	It is possible to show that the square root of two 
	can be expressed as an infinite continued fraction.

	By expanding this for the first four iterations, we get:

	The next three expansions are
	,
	, and
	, but the eighth expansion,

	, is the first example where the number of digits in the 
	numerator exceeds the number of digits in the denominator.

	In the first one-thousand expansions, how many fractions 
	contain a numerator with more digits than the denominator?
	1/2 		
	2/5 		1
	5/12 		2
	12/29 	5
	29/70 	2
	70/169 	29
	169/408 	
	408/985 	
	'''
	# DENISE solution - puaj #

	list_decimales = [1,2]
	for n in range(2,N):
		list_decimales.append( list_decimales[n-1]*2 + list_decimales[n-2] )

	list_decimales = np.array(list_decimales)
	ans = np.sum([len(str(list_decimales[n]+list_decimales[n+1]))>len(str(list_decimales[n+1])) for n in range(N-1) ] )

	return ans

P57( N=1000 )  