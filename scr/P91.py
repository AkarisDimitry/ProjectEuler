import numpy as np
import matplotlib as plt
from functions import *

import time 
from functools import reduce

@timer
#@jit('int64(int64[:])', nopython=True) # , nopython=True, 
def P91(Nmax=50):
    '''
    The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), 
    to form ΔOPQ.

    There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate 
    lies between 0 and 2 inclusive; that is,
    0 ≤ x1, y1, x2, y2 ≤ 2.

    Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
    '''
    def minimal_fraction(numerator, denominator):
      def gcd(a, b):
          if b == 0:
              return a
          return gcd(b, a % b)

      divisor = gcd(numerator, denominator)
      return numerator // divisor, denominator // divisor

    return sum([ min( [int((Nmax-y1)/minimal_fraction(x1, y1)[0]), int(x1/minimal_fraction(x1, y1)[1])] ) + min( [int((Nmax-x1)/minimal_fraction(x1, y1)[1]), int(y1/minimal_fraction(x1, y1)[0])] ) if y1 > 0 and x1 > 0 else Nmax if y1>0 or x1>0 else Nmax*Nmax  for x1 in range(0, Nmax+1) for  y1 in range(0, Nmax+1) ])

P91()
