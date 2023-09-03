import time
from math import trunc, log
from numba import jit
import numpy as np

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        r = func(*args, **kwargs)
        name = str(func).split(' ')[1]
        print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' ) 
        return r

    return wrapper


@timer
def P122(M:int=50) -> int: 

    '''
    ans = sorted (list(getDivs(M)))
    print( ans )
    print( min( ans[1:] ) )

    a = M
    n = min( ans[1:] )
    print(  a - (n * trunc(a/n)) )
    


    Dmin = min( ans[1:] )
    N = str(bin(Dmin)[2:])
    Omin = len(N)-1 + ( sum([ int(n) for n in N]) -1 )

    Dmin = 13
    OOmin = [ int(n)*i for i, n in enumerate(str(bin(Dmin)[2:])[::-1]) ] 
    print( 'OOmin', OOmin, sum(OOmin)+int(str(bin(Dmin)[2:])[-1]) )

    print( bin(Dmin)[2:], int(log(Dmin,2))+ sum([ int(n) for n in bin(Dmin)[2:] ]) - 1 )


    print('Omin', Omin, 'Log', log(M,min(ans[1:])), M%min( ans[1:] ) )
    print( int(log(M,min(ans[1:])))+1 + Omin )

    2 4 8 16 32 64 128
    '''
    @jit(nopython=True, fastmath=True, parallel=True)
    def sum_chain(L:list, N:int, suma_actual:int,lenth_min:int, length_actual:int):

        for l in L[::-1]:
            suma_actual_l = suma_actual + l

            if suma_actual_l > N:
                continue

            elif suma_actual_l == N and length_actual < lenth_min:
                lenth_min = length_actual

            elif suma_actual_l < N and length_actual < lenth_min:
                lenth_min = sum_chain(L if suma_actual_l in L else L+[suma_actual_l] , N, suma_actual_l, lenth_min, length_actual+1)

        return lenth_min

    return sum([ sum_chain(L=[1], N=n, suma_actual=0, lenth_min=9999, length_actual=0) for n in range(1, M+1)])

P122(M=200)

