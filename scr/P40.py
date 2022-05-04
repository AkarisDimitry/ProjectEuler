from functions import *
import time
from decimal import *
import itertools 

@timer
def P40(N=1000000, v=False): 
	'''
	An irrational decimal fraction is created by concatenating the 
	positive integers:

	0.123456789101112131415161718192021...

	It can be seen that the 12th digit of the fractional part is 1.

	If dn represents the nth digit of the fractional part, find the 
	value of the following expression.

	d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
	'''
	D = [1,10,100,1000,10000, 100000, 1000000]
	product, Pn, Dn = 1, 0, 0
	for n in range(1, 400000):
		nstr = str(n)
		Dn += len(nstr)

		if Dn >= D[Pn]:
			product *= int(nstr[ D[Pn]-(Dn-len(nstr))-1 ])
			Pn += 1
			if Pn > len(D)-1:
				break

	return product

P40( N=1000000 ) 