from functions import *
import time
from decimal import *
from fractions import Fraction

@timer
def P33(N=200, v=False): 
	'''
	The fraction 49/98 is a curious fraction, 
	as an inexperienced mathematician in attempting 
	to simplify it may incorrectly believe that 
	49/98 = 4/8, which is correct, is obtained by 
	cancelling the 9s.

	We shall consider fractions like, 30/50 = 3/5, 
	to be trivial examples.

	There are exactly four non-trivial examples of 
	this type of fraction, less than one in value, 
	and containing two digits in the numerator and 
	denominator.

	If the product of these four fractions is given 
	in its lowest common terms, find the value of 
	the denominator.
	'''
	
	'''

	for n in np.linspace(0,999,1000, dtype=np.int64):
		n_str = str(n)
		for m in range(10):
			if n_str[1]!='0' and float(n_str[0])/float(n_str[1])<1 and float(n_str[0])/float(n_str[1]) ==  float(n_str[0]+str(m))/float(str(m)+n_str[1]):
				print(float(n_str[0]),'/',float(n_str[1]),  float(n_str[0]+str(m)),'/',float(str(m)+n_str[1]) )
	'''		
	fraction_prod = [1,1]
	for n1 in range(10):
		for n2 in range(10):
			for n3 in range(10):
				if n1>0 and n2>0 and float(n1)/float(n2) < 1 and float(n1)/float(n2) == float(n1*10+n3)/float(n3*10+n2):	
					fraction_prod[0] *= float(n1)
					fraction_prod[1] *= float(n2)

	numerator_factors = factorize_big_number(fraction_prod[0])
	denominator_factors = list(factorize_big_number(fraction_prod[1]))
	for n in numerator_factors:
		if n in denominator_factors:
			denominator_factors.remove(n)

	return np.prod(denominator_factors)

	# == en una linea == #
	return Fraction(np.prod(list(filter(lambda s: s > 0,[float(str(n)[0])/float(str(n)[1]) if int(str(n)[0])>0 and int(str(n)[1])>0 and float(str(n)[0])/float(str(n)[1])<1 and float(str(n)[0])/float(str(n)[1]) == float(str(n)[0]+str(n)[2])/float(str(n)[2]+str(n)[1])  else 0 for n in np.linspace(100,999,1000, dtype=np.int64) ])))).limit_denominator().denominator 

P33( N=50000 ) #9000000