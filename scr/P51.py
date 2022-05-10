from functions import *
import time, copy
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P51(N=1000000, v=False): 
	'''
	By replacing the 1st digit of the 2-digit number *3, it turns 
	out that six of the nine possible values: 13, 23, 43, 53, 73, 
	and 83, are all prime.

	By replacing the 3rd and 4th digits of 56**3 with the same digit, 
	this 5-digit number is the first example having seven primes among 
	the ten generated numbers, yielding the family: 56003, 56113, 56333,
	 56443, 56663, 56773, and 56993. Consequently 56003, being the first
	  member of this family, is the smallest prime with this property.

	Find the smallest prime which, by replacing part of the number 
	(not necessarily adjacent digits) with the same digit, is part of
	 an eight prime value family.
	'''

	primes = primes_load_upto(1000000)[9000:]
	for p in primes[1000:]:
		p_str = str(int(p))
		p_list = [int(n) for n in p_str]
		p_dic = {d:[] for d in set(p_list)}
		for i, n in enumerate(p_str): 
			if i<len(p_list)-1:
				p_dic[int(n)].append(i)

		for digits in set(p_list):
			for Nsust in range(1, len(p_dic[digits])+1):
				for Ps in itertools.combinations( np.arange(0,len(p_dic[digits]),1), Nsust):
					p2_list = copy.copy(p_list)
					count = 0
					small8 = 0
					for dig in range(10):
						for ns in Ps:
							p2_list[p_dic[digits][ns]] = dig
						num = int(''.join(map(str,p2_list)))

						if int(num) in primes:
							if small8 == 0:	small8 = num
							count += 1
					
					if count > 7:
						return small8

	# 44 min solution #
	for digits in range(5, 8):
		for Nsust in range(1, digits-1):
			Nnfix = digits-Nsust
			# 111**
			for Ps in itertools.permutations( np.arange(0,digits,1), Nsust):
				for Pf in itertools.product( [0,1,2,3,4,5,6,7,8,9], repeat=Nnfix):

					count_primes = 0
					small8 = 0

					for Drep in range(10):
						num = [0 for n in range(digits) ]
						count = 0
						for dig in range(digits):
							if dig in Ps:
								num[dig] = Drep
							else:
								num[dig] = Pf[count]
								count += 1

						#print(Ps, Pf, Drep,''.join( [str(n) for n in num]))
						if int(''.join( [str(n) for n in num])) in primes:
							count_primes += 1
							if small8 == 0:
								small8 = num

					# * - - - - -  9999 - 0000
					if count_primes > 7:
						print(Pf, Ps, small8, count_primes)


	return 

P51( N=10000000 )  
