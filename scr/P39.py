from functions import *
import time
from decimal import *
import itertools 

@timer
def P39(N=1000000, v=False): 
	'''
	If p is the perimeter of a right angle triangle with integral 
	length sides, {a,b,c}, there are exactly three solutions for 
	p = 120.

	{20,48,52}, {24,45,51}, {30,40,50}

	For which value of p ≤ 1000, is the number of solutions maximised?
	'''
	al = { (n*n):n for n in range(1000) }
	solutions = np.zeros(1000)

	for c in range(1, 1000):
		c2 = c*c
		for b in range(1, c):
			b2 = b*b
			a2 = c2-b2
			a = a2**0.5
			if int(a) == a and a+b+c < 1000:
				solutions[int(a+b+c)] += 1

	return np.argmax(solutions)
	
P39( N=1000000 ) #9000000