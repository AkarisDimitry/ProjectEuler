from functions import *
import time
from decimal import *
import itertools 

@timer
def P36(N=1000000, v=False): 
	'''
	The decimal number, 585 = 1001001001 (binary), is palindromic 
	in both bases.

	Find the sum of all numbers, less than one million, which are 
	palindromic in base 10 and base 2.

	(Please note that the palindromic number, in either base, may 
	not include leading zeros.)
	'''
	suma = 0
	for n in range(1, N+1):
		if str(bin(n))[2:] == str(bin(n))[2:][::-1] and str(n) == str(n)[::-1]:
			print( n,  str(bin(n))[2:] )
			suma += n

	return suma
	
P36( N=1000000 ) #9000000