
import numpy as np
import matplotlib as plt
from functions import *
import time, copy, math
from functools import reduce

@timer
def P88(K=1):
    '''
    A natural number, N, that can be written as the sum and product of a given set of at least 
    two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

    For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

    For a given set of size, k, we shall call the smallest N with this property a minimal 
    product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, 
    and 6 are as follows.

    k=2: 4 = 2 × 2 = 2 + 2
    k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
    k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
    k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
    k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

    Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note
     that 8 is only counted once in the sum.

    In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12,
     15, 16}, the sum is 61.

    What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

    '''
    @jit('int64(int64, int64[:], int64)', nopython=True) 
    def solver(K, vec, ans):
        #print(K, vec, np.sum(vec), np.prod(vec))
        if ans != 0: return ans
        for kmax in range(1,K):
            vec_p = vec + np.array([1 if n<kmax else 0 for n in range(K)])

            suma = np.sum(vec_p)
            product = np.prod(vec_p)

            if product <= suma:
                continue
            else:
                kmax -= 1
                break

        vec[:kmax] += np.ones(kmax, dtype=np.int64)
        for n in range(kmax-1,-1, -1):
            suma = np.sum(vec)
            product = np.prod(vec)
        
            if product == suma: return suma
            if kmax > 1: 
                ans = solver(K, vec, 0)
                if ans != 0: return ans

            vec[n] -= 1
         
        return ans

    @jit('int64(int64, int64, int64[:], int64, int64, int64)', nopython=True) 
    def solver2(K, k, vec, partial_suma, partial_prod, suma_min):
        #print(k, vec, partial_suma, partial_prod)
        for n in range(2, K):
            #print('111111111111111',k, n, vec)
            vec[k] = n

            suma = partial_suma + n
            prod = partial_prod * n

            if prod > suma:
                break

            elif k+1 < K and prod < suma:
                suma_min = solver2(K, k+1, np.copy(vec), suma-vec[k+1], prod/vec[k+1], suma_min)

            else:
                if suma < suma_min:
                    suma_min = suma
                    return suma_min

        return suma_min


    #@jit('int64(int64)', nopython=True) 
    def solver3(n):
         answers = [0]*(n+1)
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

         for x in range(4,2*n+1):
             factors = factorizations[x]
             for p in factors:
                 t = 0
                 for y in p:
                     t+=y
                 if(len(p)>1 and t<=x):
                     i = len(p)+x-t
                     if(i<=n):
                         v = answers[i]
                         if(v==0):
                             answers[i] = x
         found = []
         total = 0
         for x in answers:
             if x not in found:
                 total+=x
                 found.append(x)
         return total

    return solver3(K)

P88(K=12000) # 7587457