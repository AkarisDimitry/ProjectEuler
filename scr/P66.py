import numpy as np
import matplotlib as plt
from functions import *
import time, decimal
from functools import reduce

@timer
def P66(N):
	'''
	https://projecteuler.net/problem=66
	https://www.youtube.com/watch?v=ZA5FC9ONO3A
	Pell’s equation (sometimes the Pell-Fermat equation) 

	Consider quadratic Diophantine equations of the form:
	
	x2 – Dy2 = 1

	For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

	It can be assumed that there are no solutions in positive integers when D is square.

	By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

	32 – 2×22 = 1
	22 – 3×12 = 1
	92 – 5×42 = 1
	52 – 6×22 = 1
	82 – 7×32 = 1

	Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained
	 when D=5.

	Find the value of D ≤ 1000 in minimal solutions of x for which the largest value 
	of x is obtained.

	D = D*1 + 0
	0 = D + -1 D

	chakravala method

	'''
	def diophantine(x, y, D):	return x*x - D*y*y

	def find_minX(D, x_max=10):
		for x in range(2, x_max):
			x2_1D = 1 + x*x*D 
			
			print( x2_1D, 2*x*D)
			
			if is_square_prec( int(x2_1D) ):
				print(x2_1D**0.5)
				return x

	def find_xy(D, ):
		cfl = continued_fraction(D)*5
		#print( cfl, series2fraction( cfl ))
		for i, n in enumerate(cfl):
			if i>0:
				y, x = series2fraction( cfl[-i+1:] )
				
				print(x,y, x*x - D*(y*y) )
				#if x*x - D*y*y == 1 or x*x - D*y*y == -1:
					#return x, y

	#print(diophantine(1766319049, 226153980, 61)) 
	find_xy( 2  )
	asdf
	maxminX = 0
	for n in range(1,N+1):

		if n**0.5 != int(n**0.5):

			num = find_minX(n)
			if num is None:
				pass
			elif num > maxminX:
				maxminX = num
			print(n, num)

	return maxminX

P66(1000)	