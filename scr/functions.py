import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import itertools, decimal, time, math
from math import gcd
from numba import njit, jit

def timer(func):
	def wrapper(*args, **kwargs):
		before = time.time()
		r = func(*args, **kwargs)
		name = str(func).split(' ')[1]
		print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' ) 
		return r

	return wrapper

@timer
def Fibonacci(N, init=[1, 1], Fmax=None, save=True):
	init = init
	Fmax = Fmax if type(Fmax) != type(None) else np.inf
	F = np.zeros(N)
	F[1], F[0] = init[-1], init[-2]

	for n in range(2, N):
		if F[n-1] > Fmax: break
		F[n] = F[n-1] + F[n-2]

	if save: Fibonacci = F[:n-1]
	return F[:n-1]

def phi(n):
	amount = 0        
	for k in range(1, n + 1):
		if gcd(n, k) == 1:
			amount += 1

	return amount

def phi_2primes(p1, p2, n):
	return n * (1-1/p1) * (1-1/p2)

@timer
@jit('int64[:](int64[:])', nopython=True) # , nopython=True, 
def phi_list_jit(N):
	d = np.zeros_like(N, dtype=np.int64)
	for i, n in enumerate(N):
		for k in range(1, n + 1):
			if np.gcd(n, k) == 1:
				d[i] += 1
	return d

#@timer
@jit('int64(int64)', nopython=True) # , nopython=True, 
def phi_jit(N):
	d = 0
	for k in range(1, N + 1):
		if gcd(N, k) == 1:
			d += 1
	return d

def is_coprime(x, y):
    return gcd(x, y) == 1
    
@timer
def primes_calculate(N):
	prime_list = np.zeros(N, dtype=np.int64) 
	prime_list[0] = 2
	p = np.array([1])

	for n in range(3, N, 2):
		for m in range(p[0]):
			if n%prime_list[m]==0: break
		
		if m+1 == p[0]:
			prime_list[p[0]] = n	
			p[0] += 1

	primes_list = prime_list[:p[0]]
	return primes_list

@timer
def primes_first_N(N):
	prime_list = np.zeros(N, dtype=np.int64)
	prime_list[0] = 2
	p = np.array([1])
	n = np.array([3])

	while p[0] < N :

		for m in range(p[0]):
			if n[0]%prime_list[m]==0: break
		
		if m+1 == p[0]:
			prime_list[p[0]] = n[0]	
			p[0] += 1

		n[0] += 2

	primes_list = prime_list[:p[0]]
	return primes_list

@timer
def primes_lower_N(N):
	prime_list = np.zeros(N, dtype=np.int64)
	prime_list[0] = 2
	p = np.array([1])
	n = np.array([3])

	while prime_list[p[0]-1] < N :
		for m in range(p[0]):
			if n[0]%prime_list[m]==0: break
		
		if m+1 == p[0]:
			prime_list[p[0]] = n[0]	
			p[0] += 1

		n[0] += 2

	primes_list = prime_list[:p[0]-1]
	return primes_list

def get_primes_list_max():
	return 			   [ 15485863,  32452843,  49979687,  67867967,  86028121, 
						104395301, 122949823, 141650939, 160481183, 179424673,
						198491317, 217645177, 236887691, 256203161, 275604541, 
						295075147, 314606869, 334214459, 353868013, 373587883,
						393342739, 413158511, 433024223, 452930459, 472882027,
						492876847, 512927357, 533000389, 553105243, 573259391,
						593441843, 613651349, 633910099, 654188383, 674506081,
						694847533, 715225739, 735632791, 756065159, 776531401,
						797003413, 817504243, 838041641, 858599503, 879190747,
						899809343, 920419813, 941083981, 961748927, 982451653, ]

def primes_tree(N):
	prime_tree = {}
	for i, n in enumerate( get_primes_list_max() ):
		print(f'Loading {n}/{N}')
		prime_tree[n] = np.loadtxt(f'../files/primes/primes{i+1}.txt')
		if N<n:	break

	return prime_tree

def primes_list(N): return primes_load_upto(N)

def primes_load_upto(N):
	for i, n in enumerate( get_primes_list_max() ):
		print(f'Loading {n}/{N}')
		prime_list = np.loadtxt(f'../files/primes/primes{i+1}.txt') if i == 0 else np.concatenate( (prime_list, np.loadtxt(f'../files/primes/primes{i+1}.txt')), axis=0 )
		if N<n:	break

	return prime_list[prime_list<=N]

@timer
def factorize(N):
	primes_calculate( int(N**0.5) )
	prime_factors = np.zeros( int(N**0.5), dtype=np.int64)
	index = 0

	for p in primes_list:
		while N%p == 0:
			prime_factors[index] = p
			index += 1
			N /= p
		if p>N: break

	factorize_list = prime_factors[:index]
	print(f'Factores primos de {np.prod(factorize_list, dtype=np.int64)} : {factorize_list}' )
	return factorize_list

def factorize_big_number(N):
	prime_list = np.zeros(100, dtype=np.int64) 
	index = 0

	n = 2
	while N > 1:
		if N%n == 0:	
			N /= n
			prime_list[index] = n
			index += 1
		else: 			n+=1

	primes_list = prime_list[:index]
	return primes_list

@jit('int64[:](int64)', nopython=True) # , nopython=True, 
def factorize_big_number_cuda(N):
	prime_list = np.zeros(100, dtype=np.int64) 
	index = 0

	n = 2
	while N > 1:
		if N%n == 0:	
			N /= n
			prime_list[index] = n
			index += 1
		else: 			n+=1

	primes_list = prime_list[:index]
	return primes_list


@jit('int64[:,:](int64[:])', nopython=True) # , nopython=True, 
def factorize_big_list_cuda(N):
	# upto 2**30 = 1073741824
	prime_list = np.zeros((N.shape[0], 30), dtype=np.int64) 
	
	for i, M in enumerate(N):
		index = 0
		n = 2
		while M > 1:
			if M%n == 0:	
				M /= n
				prime_list[i, index] = n
				index += 1
			else: 			
				n+=1

	return prime_list

def get_all_factorizations(N):
     factorizations = [[],[],[[2]],[[3]],[[2,2],[4]]]
     for c in range(5,2*n+1):
         factors = []
         for x in range(2,int(math.sqrt(c))+1):
             if(c%x==0):
                 a = factorizations[int(c/x)]
                 for p in a:
                     possible = True
                     for z in p:
                         if z<x:
                             possible = False
                             break
                     if possible:
                         t = p[:]
                         t.append(x)
                         factors.append(sorted(t))
         factors.append([c])
         factorizations.append(factors)
     return factorizations
     
def is_prime(N):
	prime_list = np.zeros(100, dtype=np.int64) 
	index = 0

	n = 2
	while N > 1:
		if N%n == 0:	
			N /= n
			prime_list[index] = n
			index += 1
			return 0
		else: 			n+=1

	return 1

def is_palindromic(N): return N == N[::-1]

@timer
def pascal_triangle(N):
	#C(n,k+1) = C(n,k) * (n-k) / (k+1)
	line = [1]
	for k in range(n):
		line.append(line[k] * (n-k) / (k+1))
	return line

def getDivs_sum(N):
	'''
	In this example, the sum_divisors function takes an integer as input and returns 
	the sum of its divisors. 
	'''
	factors = {1}
	maxP  = int(N**0.5)
	p,inc = 2,1
	while p <= maxP:
		while N%p==0:
			factors.update([f*p for f in factors])
			N //= p
			maxP = int(N**0.5)
		p,inc = p+inc,2
	if N>1:
		factors.update([f*N for f in factors])
	return sum(factors) 

@jit('int64(int64)', nopython=True)#, parallel=True) # fastmath=True
def getDivs_sum_gpu(n):
	'''
	In this example, the sum_divisors function takes an integer as input and returns 
	the sum of its divisors. The numba.jit decorator is used to compile the function,
	 which can make it run faster. Note that the numba library does not support recursion or closures.
	'''
	divisors = [1]
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
			if i != n // i:
				divisors.append(n // i)
	return sum(divisors)

@jit('int64[:](int64[:])', nopython=True)#, parallel=True) # fastmath=True
def getDivs_sum_list_gpu(nlist):
	'''
	In this example, the sum_divisors function takes an list of integers as input and returns 
	the list of sum of its divisors. 
	'''
	div_sum_list = np.zeros_like(nlist)

	for j, n in enumerate(nlist):
		divisors = [1]
		for i in range(2, int(n**0.5)+1):
			if n % i == 0:
				divisors.append(i)
				if i != n // i:
					divisors.append(n // i)

		div_sum_list[j] = sum(divisors) 

	return div_sum_list

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def getDivs(N):
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return factors 

def abundant_numbers(N):
	divisors = np.zeros(N, dtype=np.int64)
	for n in range(N):
		factors = factorize_big_number(n)
		a = set()
		for m in range(factors.shape[0]):
			a = a | set(itertools.combinations(factors, m))

		divisors[n] = int(np.sum( [ np.prod(n) for n in a ] ))

	filters = divisors > np.linspace(0,N-1,N, dtype=np.int64)

	return  np.linspace(0,N-1,N, dtype=np.int64)[filters]

def divide(number_one, number_two, decimal_place = 4):
	'''
	This function works on the basis of "Euclid Division Algorithm". 
	This function is very useful if you don't want to import any external
	header files in your project.
	https://stackoverflow.com/questions/117250/how-do-i-get-a-decimal-value-when-using-the-division-operator-in-python
	'''
	dot = False
	quotient_str = ''
	for loop in range(0, decimal_place):	
		zeros_add = 0
		while (number_one * 10**zeros_add) < number_two: zeros_add+=1
		if not dot and zeros_add>0: 
			dot = True
			quotient_str+='.'
			quotient_str+='0'*(zeros_add-1)
		else:
			quotient_str+='0'*(zeros_add-1)

		surplus_quotient = int(number_one * 10**zeros_add / number_two)
		quotient_str += str(surplus_quotient)
		number_one = number_one*10**zeros_add - int(surplus_quotient)*number_two
		if number_one == 0:
			break

	return str(quotient_str)

def period(L):
	period = L[0]

	for l in L[1:]:

		period_repeat = str(period*int(len(L)/len(period)+1))[:len(L)]
		if L == period_repeat:
			return period
		else:
			period += l

	return period

def division_period(number_one, number_two):

	a = divide(number_one, number_two, 100)
	print('divition',number_one, number_two, a)
	print('period', period(a) )
	print(number_two, period(divide(number_one, number_two, 100)))
	return None

def find_period(n, d):
	z = x = n * 9
	k = 1
	c = 0
	while z % d:
		c = z%d
		z = z * 10 + x
		k += 1

	digits = f"{z // d:0{k}}"
	return k, digits
	
def getPeriod( n) :
 
    # Find the (n+1)th remainder after
    # decimal point in value of 1/n
    rem = 1 # Initialize remainder
    for i in range(1, n + 2):
        rem = (10 * rem) % n
 
    # Store (n+1)th remainder
    d = rem
     
    # Count the number of remainders
    # before next occurrence of
    # (n+1)'th remainder 'd'
    count = 0
    rem = (10 * rem) % n
    count += 1
    while rem != d :
        rem = (10 * rem) % n
        count += 1
     
    return count

def continued_fraction(n, max_length=100):  
	mn, dn = 0.0, 1.0
	a0 = int(math.sqrt(n))
	an = int(math.sqrt(n))
	cf_list = [a0]
	period = 0
	if a0 != math.sqrt(n):
		while an != 2*a0 and len(cf_list)<max_length:
			mn = dn*an - mn
			dn = (n - mn**2)/dn
			an = int((a0 + mn)/dn)
			cf_list.append(an)
			period += 1

	return cf_list

def continued_fraction_period_prec(n):
	mn, dn = 0.0, 1.0
	a0 = int(math.sqrt(n))
	an = int(math.sqrt(n))
	period = 0
	if a0 != math.sqrt(n):
		while an != 2*a0:
			mn = dn*an - mn
			dn = (n - mn**2)/dn
			an = int((a0 + mn)/dn)
			period += 1

	return period

def series2fraction(series):
	numerator = 1
	denominator = series[-1]
	for e in series[::-1][1:]:
		numerator += e*denominator
		denominator, numerator = numerator, denominator
		print(f'{numerator}/{denominator}')

	return numerator, denominator

def reducefract(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

@jit('int64(int64)', nopython=True) # , nopython=True, 
def proper_fractions(n):
  distinct_prime_factors = set()   # use set to avoid duplicates
  totient_function = n
  if n == 1:
    totient_function = 0
  else:
    i = 2
    while i*i <= n:
      if n % i == 0:
        distinct_prime_factors.add(i)
        n = n/i
      else:
        i += 1
    if n > 1:
      distinct_prime_factors.add(n)   # picks up prime factors > sqrt(n)
    if len(distinct_prime_factors) == 0:   # empty set means denominator is prime
      totient_function = n - 1
    else:
      for p in distinct_prime_factors:
        totient_function = (totient_function*(p - 1))/p
  return totient_function

@jit('uint32(uint32, uint32)', nopython=True, fastmath=True, parallel=True )#, parallel=True) # fastmath=True
def numberofways(n, m) :
	dp = np.zeros((n + 2, n + 2), dtype=np.uint32) 
	dp[0][n + 1] = 1
	# Filling the table. k is for numbers
	# greater than or equal that are allowed.
	for k in range(n, m - 1, -1) :
		# i is for sum
		for i in range(n + 1) :
			# initializing dp[i][k] to number
			# ways to get sum using numbers
			# greater than or equal k+1
			dp[i][k] = dp[i][k + 1]
 
 			# if i > k
			if (i - k >= 0) :
				dp[i][k] = (dp[i][k] + dp[i - k][k])
	
	return dp[n][m]


def squareRoot(number, precision):
 
    start = 0
    end, ans = number, 1
 
    # For computing integral part
    # of square root of number
    while (start <= end):
        mid = int((start + end) / 2)
 
        if (mid * mid == number):
            ans = mid
            break
 
        # incrementing start if integral
        # part lies on right side of the mid
        if (mid * mid < number):
            start = mid + 1
            ans = mid
 
        # decrementing end if integral part
        # lies on the left side of the mid
        else:
            end = mid - 1
 
    # For computing the fractional part
    # of square root upto given precision
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment
 
        # loop terminates when ans * ans > number
        ans = ans - increment
        increment = increment / 10
 
    return ans

def is_square_prec(apositiveint):
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

def is_pandigital(N):
	vec = np.array([str(N).count(str(n)) for n in range(1,10)])==1
	return vec.all()

def is_pandigitalN(N):
	vec = np.array([str(N).count(str(n)) for n in range(1,len(str(N))+1)])==1
	return vec.all()

def is_pandigital09(N):
	vec = np.array([str(N).count(str(n)) for n in range(0,10)])==1
	return vec.all()

def is_permutation(N1, N2):
	N1 = [n for n in str(N1)]
	N2 = [n for n in str(N2)]
	return all(N1.count(char) == N2.count(char) for char in set(N1) | set(N2))

def anagram(str1:str, str2:str) -> bool:
	return len(str1)==len(str2) and sorted(str1)==sorted(str2)

@jit('int64(int64)', nopython=True) # , nopython=True, 
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def genTriples(k): # primitive pythagorean triangles a,b,c where a<b<c<k
	def gcd(n, d):
		while d != 0:
			t = d
			d = n%d
			n = t
		return n

	n,m = 1,2
	while m*m+1<k:                  # while c<k (for largest m producing c)
		if n>=m: n,m = m%2,m+1      # n reached m, advance m, reset n
		c = m*m+n*n                 # compute c 
		if c >= k: n=m;continue     # skip remaining n when c >= k
		if gcd(n,m) == 1:           # trigger on coprimes
			yield m*m-n*n,2*m*n,c   # return a,b,c triple
		n += 2                      # advance n, odd with evens

@jit('int64[:,:](int64)', nopython=True) # , nopython=True, 
def genTriples_gpu(k): # primitive pythagorean triangles a,b,c where a<b<c<k
	Triples = []
	def gcd(n, d):
		while d != 0:
			t = d
			d = n%d
			n = t
		return n

	n,m = 1,2
	while m*m+1<k:                  # while c<k (for largest m producing c)
		if n>=m: n,m = m%2,m+1      # n reached m, advance m, reset n
		c = m*m+n*n                 # compute c 
		if c >= k: n=m;continue     # skip remaining n when c >= k
		if gcd(n,m) == 1:           # trigger on coprimes
			Triples.append([m*m-n*n,2*m*n,c]) # return a,b,c triple
		n += 2                      # advance n, odd with evens

	return np.array( Triples )

#print( [n for n in genTriples_gpu(100)] )