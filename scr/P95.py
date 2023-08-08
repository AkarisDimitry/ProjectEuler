
import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P95(N=100):
	'''
	The proper divisors of a number are all the divisors excluding the number 
	itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
	 the sum of these divisors is equal to 28, we call it a perfect number.

	Interestingly the sum of the proper divisors of 220 is 284 and the sum of 
	the proper divisors of 284 is 220, forming a chain of two numbers. For this 
	reason, 220 and 284 are called an amicable pair.

	Perhaps less well known are longer chains. For example, starting with 12496,
	 we form a chain of five numbers:

	12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

	Since this chain returns to its starting point, it is called an amicable chain.

	Find the smallest member of the longest amicable chain with no element
	 exceeding one million.
	'''

	@jit('int64[:](int64[:])', nopython=True)#, parallel=True) # fastmath=True
	def getDivs_sum_list_gpu(nlist):
		'''
		In this example, the sum_divisors function takes an integer as input and returns 
		the sum of its divisors. 
		'''
		div_sum_list = np.zeros_like(nlist)

		for j, n in enumerate(nlist):
			divisors = [1]
			for i in range(2, int(n**0.5)+1):
				if n % i == 0:
					divisors.append(i)
					if i != n // i:
						divisors.append(n // i)

			div_sum_list[j] = sum(divisors) 

		return div_sum_list

	div_dict = {} # dict with divisors
	for n in range(1, N):
		div_dict[n] = getDivs_sum_gpu(n)
	div_dict[1] = 1 
	'''
	num_list = np.arange(1, N, dtype=np.int64)
	div_dict_list = getDivs_sum_list_gpu( num_list )	
	div_dict = {n:div_dict_list[i] for i, n in enumerate(num_list) }
	'''

	min_element_max_cicle = 0
	max_cicle = 0
	div_lenth_list = np.zeros(N) # list with max cicle lenth for each number
	for n in range(1, N):

		div_list = []
		num = n
		div_cicle_lenth = 0
		while True:
			div_list.append(num)
			num = div_dict[num]
			div_cicle_lenth += 1 # cicle lenth

			if num in div_list:
				div_cicle_lenth = div_cicle_lenth - div_list.index(num)
				break	

			if num > N:
				div_cicle_lenth = 0
				break

			if num < n:
				div_cicle_lenth = div_lenth_list[num]
				break		

		if max_cicle < div_cicle_lenth:
			max_cicle = div_cicle_lenth
			min_element_max_cicle = num

		div_lenth_list[n] = div_cicle_lenth 

	return min_element_max_cicle

P95(10**6)