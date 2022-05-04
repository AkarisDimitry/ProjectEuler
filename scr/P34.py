from functions import *
import time
from decimal import *

@timer
def P34(N=200, v=False): 
	'''
	145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

	Find the sum of all numbers which are equal to the sum 
	of the factorial of their digits.

	Note: As 1! = 1 and 2! = 2 are not sums they are not 
	included.
	'''
	def digit_factorials(N):	
		return np.sum([ dict_f[int(n)] for n in str(N) ])
		
	dict_f = {n:np.math.factorial(n) for n in range(10) }
	return np.sum([ n if n == digit_factorials(n) else 0 for n in np.linspace(10, N, N-9, dtype=np.int64)])

P34( N=50000 ) #9000000