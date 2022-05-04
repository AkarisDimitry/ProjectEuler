import matplotlib.pyplot as plt
import numpy as np 
from functions import *
import time 
from functools import reduce
import itertools
from decimal import *

@timer
def P27(N=10, v=False): 
	'''
	Euler discovered the remarkable quadratic formula:

	It turns out that the formula will produce 40 primes for the 
	consecutive integer values . However, when is divisible by 41, 
	and certainly when	is clearly divisible by 41.

	The incredible formula	was discovered, which produces 80 primes
	 for the consecutive values. The product of the coefficients, 
	 -79 and 1601, is −126479.

	Considering quadratics of the form:	, where and

	where is the modulus/absolute value of 	e.g. and

	Find the product of the coefficients,   and , for the quadratic 
	expression that produces the maximum number of primes for consecutive 
	values of , starting with .
	'''
	def p(a, b, n):
		# p = n**2 + a*n + b
		return n**2 + a*n + b 
	
	#np.zeros(2000, 2000, 80)
	# p = n**2 + a*n + b > 0
	#     n**2 + a*n + b > 0
    # b > 0  
    # n=40   1600 + b = -40 * a
    # n=40   -40 = a

	A = [a for a in np.linspace(-100, 0, num=100, endpoint=False, dtype=np.int64)]
	B = [b for b in np.linspace(2, 1000, num=998, endpoint=True, dtype=np.int64)]
	n = np.linspace(1, N, N)-1

	prime_list = primes_load_upto(50000)
	ABmax = [0,0]
	list_1 = []
	list_2 = []
	for a in A:
		for b in B:
			pol = p(a,b,n)
			for i, num in enumerate(pol):
				if num<1 or not num in prime_list:
				 	break

			if ABmax[0] < i:
				ABmax[0] = i
				ABmax[1] = a*b
				#print(f'a:{a}, b:{b}, primes:{i+1}' )

	return ABmax[1]


P27(N=100)

