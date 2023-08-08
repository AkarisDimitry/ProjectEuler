import numpy as np
import networkx as nx
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P108() -> int: 
    '''
    In the following equation , , and  are positive integers.

    For  there are exactly three distinct solutions:
     
     
    What is the least value of  for which the number of distinct
     solutions exceeds one-thousand?

    NOTE: This problem is an easier version of Problem 110; it is 
    strongly advised that you solve this one first.
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
            if w > 1000:
                nmin = num
        count = next(count, cmax)

    return (nmin)

P108()