import numpy as np
import matplotlib.pyplot as plt
import time 
from functools import reduce
import itertools

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

def primes_load_upto(N):
	prime = np.loadtxt('../files/primes/primes1.txt')
	return prime[prime<N]

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

def is_palindromic(self, N): return N == N[::-1]

@timer
def pascal_triangle(N):
	#C(n,k+1) = C(n,k) * (n-k) / (k+1)
	line = [1]
	for k in range(n):
		line.append(line[k] * (n-k) / (k+1))
	return line

@timer
def divisors_sum(N):
	divisors = np.zeros(N, dtype=np.int64)
	for n in range(N):
		factors = factorize_big_number(n)
		a = set()
		for m in range(factors.shape[0]):
			a = a | set(itertools.combinations(factors, m))

		divisors[n] = int(np.sum( [ np.prod(n) for n in a ] ))

	return divisors[n]

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

def is_pandigital(N):
	vec = np.array([str(N).count(str(n)) for n in range(1,10)])==1
	return vec.all()

def is_pandigitalN(N):
	vec = np.array([str(N).count(str(n)) for n in range(1,len(str(N))+1)])==1
	return vec.all()

def is_pandigital09(N):
	vec = np.array([str(N).count(str(n)) for n in range(0,10)])==1
	return vec.all()