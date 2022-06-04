import numpy as np
import matplotlib as plt
from functions import *
import math

import time 
from functools import reduce

@timer
def P74(N=20): 
	'''
	The number 145 is well known for the property that the sum of the factorial 
	of its digits is equal to 145:

	1! + 4! + 5! = 1 + 24 + 120 = 145

	Perhaps less well known is 169, in that it produces the longest chain of
	 numbers that link back to 169; it turns out that there are only three such 
	 loops that exist:

	169 → 363601 → 1454 → 169
	871 → 45361 → 871
	872 → 45362 → 872

	It is not difficult to prove that EVERY starting number will eventually get 
	stuck in a loop. For example,

	69 → 363600 → 1454 → 169 → 363601 (→ 1454)
	78 → 45360 → 871 → 45361 (→ 871)
	540 → 145 (→ 145)

	Starting with 69 produces a chain of five non-repeating terms, but the longest 
	non-repeating chain with a starting number below one million is sixty terms.

	How many chains, with a starting number below one million, contain exactly sixty 
	non-repeating terms?
	'''	
	#print([(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10)), -1, -1)][bool(math.log(n,10)%1):])


	asd
	
	ans = 0
	for N in range(10, 1000000):
		if N%10000==0: print(N)

		suma = N
		store = np.zeros(61, dtype=np.int64)
		store[0] = N

		for n in range(1, 61):
			suma = sum([ [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][int(s)] for s in str(suma)])
			if suma in store[:n]:

				if n == 60:
					ans += 1
					print(ans, N)
				break
			else:
				store[n] = suma
	return ans

P74(N=8)
