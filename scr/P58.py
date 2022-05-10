from functions import *
import time, copy
from decimal import *
from fractions import Fraction
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P58(N=1000000, v=False): 
	'''
	Starting with 1 and spiralling anticlockwise in the following way, a square 
	spiral with side length 7 is formed.

	37 36 35 34 33 32 31
	38 17 16 15 14 13 30
	39 18  5  4  3 12 29
	40 19  6  1  2 11 28
	41 20  7  8  9 10 27
	42 21 22 23 24 25 26
	43 44 45 46 47 48 49

	It is interesting to note that the odd squares lie along the bottom right 
	diagonal, but what is more interesting is that 8 out of the 13 numbers lying 
	along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

	If one complete new layer is wrapped around the spiral above, a square spiral
	 with side length 9 will be formed. If this process is continued, what is the
	  side length of the square spiral for which the ratio of primes along both 
	  diagonals first falls below 10%?
	'''

	# ================================== #
	# === with prime Elimination 16s === #
	# ================================== #
	Sprimes = primes_load_upto(30000)
	def check_num(N):
		Nsqrt = N**0.5
		for n in Sprimes:
			if N%n == 0:		return False
			elif n>Nsqrt:		return True

	N = 14000
	n37 = np.linspace( 1, N+0, N*2-1, dtype=np.float64 )-1
	vec37 =  np.array(4*n37**2 + 2*n37 + 1 , dtype=np.int64 )
	# [  1.   3.   7.  13.  21.  31.  43.  57.  73.  91. 111. 133. 157. 183. 211.]
	
	# !! never prime !! #
	#n9 = np.linspace( 1, N+0, N, dtype=np.float64 )[1:]-1
	#vec9 = np.array(4*n9**2 + 4*n9 + 1 , dtype=np.int64 )
	#vec9 = [ 0 for n in vec9] 
	# [  1.   9.  25.  49.  81. 121. 169. 225. 289. 361. 441. 529. 625. 729.  841.]
	
	n5 = np.linspace( 1.5, N-0.5, N-1, dtype=np.float64 )-1
	vec5 = np.array(4*n5**2 + 4*n5 + 2, dtype=np.int64 )
	# [  5.  17.  37.  65. 101. 145. 197. 257. 325. 401. 485. 577. 677. 785. 901.]

	numerator = 0
	denominator = 1
	for i in range(1, N ):
		for n in vec37[i*2-1:(i*2+1)]:
			if check_num(n):
				numerator += 1

		for n in vec5[i-1:i]:
			if check_num(n):
				numerator += 1

		denominator += 4
		if i%1000==0:
			print(i, vec5[i-1:i], numerator/denominator)

		if numerator/denominator < 0.1:
			return i*2+1

	# ================================ #
	# === with prime list time:40s === #
	# ================================ #
	def prime_check(N):
		max_list = [ 15485863,  32452843,  49979687,  67867967,  86028121, 
						104395301, 122949823, 141650939, 160481183, 179424673,
						198491317, 217645177, 236887691, 256203161, 275604541, 
						295075147, 314606869, 334214459, 353868013, 373587883,
						393342739, 413158511, 433024223, 452930459, 472882027,
						492876847, 512927357, 533000389, 553105243, 573259391,
						593441843, 613651349, 633910099, 654188383, 674506081,
						694847533, 715225739, 735632791, 756065159, 776531401,
						797003413, 817504243, 838041641, 858599503, 879190747,
						899809343, 920419813, 941083981, 961748927, 982451653, ]
						
		if N > max_list[-1]:
			print(f'Error {N}')
		for i, n in enumerate(max_list):
			if N < n:
				break

		return N in Tprimes[n]

	Tprimes = primes_tree(16000000000)

	N = 14000
	n37 = np.linspace( 1, N+0, N*2-1, dtype=np.float64 )-1
	vec37 =  np.array(4*n37**2 + 2*n37 + 1 , dtype=np.int64 )
	vec37 = [ prime_check(n) for n in vec37]
	# [  1.   3.   7.  13.  21.  31.  43.  57.  73.  91. 111. 133. 157. 183. 211.]
	
	n9 = np.linspace( 1, N+0, N, dtype=np.float64 )[1:]-1
	vec9 = np.array(4*n9**2 + 4*n9 + 1 , dtype=np.int64 )
	vec9 = [ 0 for n in vec9]
	# [  1.   9.  25.  49.  81. 121. 169. 225. 289. 361. 441. 529. 625. 729.  841.]
	
	n5 = np.linspace( 1.5, N-0.5, N-1, dtype=np.float64 )-1
	vec5 = np.array(4*n5**2 + 4*n5 + 2, dtype=np.int64 )
	vec5 = [ prime_check(n) for n in vec5]
	# [  5.  17.  37.  65. 101. 145. 197. 257. 325. 401. 485. 577. 677. 785. 901.]

	for i in range(1, N ):
		vec = np.concatenate( (vec37[:(i*2+1)], vec9[:(i)], vec5[:(i)]) )
		primes_count = np.sum(vec)
		pct = 100*float(primes_count)/vec.shape[0]

		print(i*2+1, pct, float(primes_count), vec.shape[0])
		if pct < 10:
			break

	return i*2+1

P58( N=1000 )  