from sympy import prime
import time
from numba import jit

# A timer decorator to measure the execution time of functions.
def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        r = func(*args, **kwargs)
        name = str(func).split(' ')[1]
        print(f'Result of {name} : {r} (execution time {time.time()-before}s)') 
        return r
    return wrapper

@timer
@jit
def P129b(N:int) -> int:
    '''
    <p>A number consisting entirely of ones is called a repunit. We shall
     define $R(k)$ to be a repunit of length $k$; for example, $R(6) = 111111$.</p>
    <p>Given that $n$ is a positive integer and $\gcd(n, 10) = 1$, it can 
    be shown that there always exists a value, $k$, for which $R(k)$ is 
    divisible by $n$, and let $A(n)$ be the least such value of $k$; for 
    example, $A(7) = 6$ and $A(41) = 5$.</p>
    <p>The least value of $n$ for which $A(n)$ first exceeds ten is $17$.</p>
    <p>Find the least value of $n$ for which $A(n)$ first exceeds one-million.</p>
    '''
    k_max = 0
    for n in range(N/10-1000, N):

        if n%2!=0 and n%5!=0:
            k = 2               #R_k = int((10**k-1)/9)
            res = 11            # 13
            res0 = 10           # 10

            while res != 0:
                res0 = int((res0*10)%n)  # 9 (mod13)
                res = (res0+res)%n         # 22

                k += 1
                #R_k = int((10**k-1)/9)
            if k > k_max: k_max = k
            if k > 10**6: break
            #print(n, k)           


    return n

P129b(N=10**7) 





