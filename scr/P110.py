import numpy as np
import networkx as nx
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P110() -> int: 
    '''
    In the following equation , , and  are positive integers.

    It can be verified that when  there are  distinct solutions and this is the least value 
    of  for which the total number of distinct solutions exceeds one hundred.

    What is the least value of  for which the number of distinct solutions exceeds four million?

    NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond
     the limitations of a brute force approach it requires a clever implementation.
   ''' 

    def next(count, maxcount):
        i = 0
        while i < len(count) and count[i] == maxcount:
            i += 1
        if i < len(count):
            n = count[i]
            while i >= 0:
                count[i] = n + 1
                i -= 1
        else:
            return None
        return count

    def getn(primes, count):
        num = 1
        for i in range(len(count)):
            num *= pow(primes[i], count[i])
        return num

    def ways(cfacts):
        i = 1
        for c in cfacts:
            i *= 2 * c + 1
        return (i + 1) / 2

    cmax = 3
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    count = [0] * len(primes)

    nmin = 10**100
    while count:
        num = getn(primes, count)
        if num < nmin:
            w = ways(count)
            if w > 4000000:
                nmin = num
        count = next(count, cmax)

    return (nmin)

P110()