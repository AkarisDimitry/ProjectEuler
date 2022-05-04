from functions import *
import time
from decimal import *
import itertools 

@timer
def P43(N=1000000, v=False): 
	'''
	The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
	each of the digits 0 to 9 in some order, but it also has a rather interesting 
	sub-string divisibility property.

	Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
	the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

	Find the sum of all 0 to 9 pandigital numbers with this property
	'''

	def couldbe_pandigital09(N):
		vec = np.array([str(N).count(str(n)) for n in range(0,10)])<=1
		return vec.all()

	divisors = [2,3,5,7,11,13,17]
	d3_dict = { d: {} for d in divisors }

	for d in divisors:
		for n in np.arange(d,1000,d, dtype=np.int64):
			lab = ('0'*(3-len(str(n))) + str(n))[:2]
			if lab in d3_dict[d]:	d3_dict[d][lab].append(str(n)[-1])
			else:					d3_dict[d][lab] = [str(n)[-1]]


	suma = 0
	for d234 in np.arange(12,986,2, dtype=np.int64):
		d234str = ('0'*(3-len(str(d234))) + str(d234))

		if d234str[-2:] in d3_dict[3] and couldbe_pandigital09(d234str):
			for d5 in d3_dict[3][d234str[-2:]]:
				d2345str = d234str + d5

				if d2345str[-2:] in d3_dict[5] and couldbe_pandigital09(d2345str):
					for d6 in d3_dict[5][d2345str[-2:]]:
						d23456str = d2345str + d6

						if d23456str[-2:] in d3_dict[7] and couldbe_pandigital09(d23456str):
							for d7 in d3_dict[7][d23456str[-2:]]:
								d234567str = d23456str + d7

								if d234567str[-2:] in d3_dict[11] and couldbe_pandigital09(d234567str):
									for d8 in d3_dict[11][d234567str[-2:]]:
										d2345678str = d234567str + d8

										if d2345678str[-2:] in d3_dict[13] and couldbe_pandigital09(d2345678str):
											for d9 in d3_dict[13][d2345678str[-2:]]:
												d23456789str = d2345678str + d9

												if d23456789str[-2:] in d3_dict[17] and couldbe_pandigital09(d23456789str):
													for d10 in d3_dict[17][d23456789str[-2:]]:
														d2345678910str = d23456789str + d10

														for d1 in range(1,10):
															d1str = str(d1)
															d12345678910str = d1str + d2345678910str 
															if not d1str in d2345678910str and is_pandigital09(d12345678910str):
																print(str(d1)+d2345678910str)
																suma += int(str(d1)+d2345678910str)

	return suma
P43( N=10000000 ) 