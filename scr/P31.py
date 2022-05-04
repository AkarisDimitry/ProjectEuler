from functions import *
import time
from decimal import *

@timer
def P31(N=200, v=False): 
	'''
	In the United Kingdom the currency is made up of 
	pound (£) and pence (p). There are eight coins in
	general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

	It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

	How many different ways can £2 be made using any 
	number of coins?	
	'''

	def iter(money, total, counts, index):
		for i, n in enumerate(M[index:]):
			money[i+index] += 1
			total += n

			if total < N:
				counts = iter(money, total, counts, i+index)
				total -= n
				money[i+index] -= 1

			elif total > N:
				total -= n
				money[i+index] -= 1
				break

			elif total == N:
				counts += 1
				total -= n
				money[i+index] -= 1
				break
			else:
				total -= n
				money[i+index] -= 1
				break 

		return counts

	M = [1,2,5,10,20,50,100,200]
	return iter([0,0,0,0,0,0,0,0], 0, 0, 0)

P31( N=200 )