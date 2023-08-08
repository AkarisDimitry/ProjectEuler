import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P94(N=10):
	'''
	It is easily proved that no equilateral triangle exists with integral
	 length sides and integral area. However, the almost equilateral triangle 
	 5-5-6 has an area of 12 square units.
	We shall define an almost equilateral triangle to be a triangle for
	 which two sides are equal and the third differs by no more than one unit.
	Find the sum of the perimeters of all almost equilateral triangles with 
	integral side lengths and area and whose perimeters do not exceed one 
	billion (1,000,000,000).
	'''
	@jit('int64(int64)', nopython=True) # , nopython=True, 
	def sover(N):
		N = 10**9
		result = 0
		def gcd(n, d):
			while d != 0:
				t = d
				d = n%d
				n = t
			return n

		n,m = 1,2
		k = N//3+2
		while m*m+1<k:                  # while c<k (for largest m producing c)
			if n>=m: n,m = m%2,m+1      # n reached m, advance m, reset n
			c = m*m+n*n                 # compute c 
			if c >= k: n=m;continue     # skip remaining n when c >= k
			if gcd(n,m) == 1:           # trigger on coprimes
				a, b, c = m*m-n*n,2*m*n,c
				if abs(2*a-c)==1:               # (c,c,2*a) almost equilateral triangle
					result += 2*a+2*c
				if abs(2*b-c)==1:               # (c,c,2*b) almost equilateral triangle
					result += 2*b+2*c
			n += 2                      # advance n, odd with evens

		return result

	result = sover(N)

	return result

@timer
def P94B(N=10):
	'''
	It is easily proved that no equilateral triangle exists with integral
	 length sides and integral area. However, the almost equilateral triangle 
	 5-5-6 has an area of 12 square units.
	We shall define an almost equilateral triangle to be a triangle for
	 which two sides are equal and the third differs by no more than one unit.
	Find the sum of the perimeters of all almost equilateral triangles with 
	integral side lengths and area and whose perimeters do not exceed one 
	billion (1,000,000,000).
	'''

	@jit('int64(int64)', nopython=True) # , nopython=True, 
	def solver(N):

		suma = 0
		for c in range(2, N//3+2,2):
			cc4 = c*c//4

			for a in (c-1,c+1):
				hh = a*a - cc4
				p = 2*a+c
			
				if p >= N: 
					break	

				h = 1
				while h*h < hh:
					h += 1

				if h*h == hh:	 
					suma += p
					print('1', c, a, suma )

		return suma

	suma = solver(N)

	return suma

P94(N=10**9)