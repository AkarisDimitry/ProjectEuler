import sympy 
import time
import numpy as np
from itertools import combinations

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        r = func(*args, **kwargs)
        name = str(func).split(' ')[1]
        print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' ) 
        return r

    return wrapper


@timer
def P111(N:int=10) -> int:
    ''' 
    Considering 4-digit primes containing repeated digits it is clear that 
    they cannot all be the same: 1111 is  divisible by 11 ,  is 2222 divisible 
    by 22, and so on. But there are nine 4-digit primes containing three ones:
    1117,1151,1171,1181,1511,1811,2111,4111,8111
    We shall say that  M(n,d)represents the maximum number of repeated digits 
    for an n-digit prime where d  is the repeated digit, N(n,d)  represents the
     number of such primes, and S(n,d)  represents the sum of these primes.

    So M(4,1)=3  is the maximum number of repeated digits for a 4-digit prime
     where one is the repeated digit, there are  N(4,1)=9 such primes, and the 
     sum of these primes is S(4,1)=22275 . It turns out that for d=0 , it is
    only possible to have M(4,0)=2  repeated digits, but there are  N(4,0)=13 
    such cases.

    In the same way we obtain the following results for 4-digit primes.

    Digit, d    M(4, d) N(4, d) S(4, d)
    0   2   13  67061
    1   3   9   22275
    2   3   1   2221
    3   3   12  46214
    4   3   2   8888
    5   3   1   5557
    6   3   1   6661
    7   3   9   57863
    8   3   1   8887
    9   3   7   48073
    For d=0  to 9 , the sum of all  S(4,d) is 273700.

    Find the sum of all S(10, d).
    '''

    def generate_numbers(N, n, m):
        # Generate combinations of positions for 'n' in the number
        for comb in combinations(range(N), m):
            for i in range(10**(N-m)):  # Generate other digits of the number
                str_num = str(i).zfill(N-m)
                
                # Construct the number based on the combination and the other digits
                num_list = []
                idx = 0
                for j in range(N):
                    if j in comb:
                        num_list.append(str(n))
                    else:
                        num_list.append(str_num[idx])
                        idx += 1
                
                yield int(''.join(num_list))

    suma = 0
    N = N
    for n in range(10):
        counter = 0
        for m in np.arange(1,N)[::-1]:
            for p in generate_numbers(N, n, m):
                if p>10**(N-1) and sympy.isprime(p):
                    counter += 1    
                    suma += p

            if counter > 0: break

        print( counter, suma )

    return suma
    
P111(N=10) 

