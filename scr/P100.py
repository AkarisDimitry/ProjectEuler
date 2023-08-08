import numpy as np
import matplotlib as plt
from functions import *

import time 
from functools import reduce

@timer
#@jit('int64(int64)', nopython=True) # , nopython=True, 
def P100(N=100):
    '''
    If a box contains twenty-one coloured discs, composed of fifteen blue 
    discs and six red discs, and two discs were taken at random, it can be
     seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

    The next such arrangement, for which there is exactly 50% chance of 
    taking two blue discs at random, is a box containing eighty-five blue 
    discs and thirty-five red discs.

    By finding the first arrangement to contain over 1012 = 1,000,000,000,000 
    discs in total, determine the number of blue discs that the box would contain.
    '''

    #for n in range(10**12, 10**12+10**3):
    n=35+85
    sqrt2 = 1.0 / sqrt(2)
    while True:

      #b = int(sqrt2 * n) + 1
      b = int(0.5*(sqrt(2*n**2 - 2*n + 1) + 1))
      if b*(b-1)*2 == n*(n-1):
        print(n, b, b/n * (b-1)/(n-1) )  
        if n > 10**12: break
        n = int(5.8284 * n)

      n+=1
    # Finally, print the result

    return 1

from math import sqrt

def P100b(N=100):
  n = 35+85
  sqrt2 = 1.0 / sqrt(2)
  while 1:
      print(n)
      x = int(sqrt2 * n) + 1
      #x = 0.5*(sqrt(2*n**2 - 2*n + 1) + 1)

      if 2*x*(x-1) == n*(n-1):
          print("yay",x,"\tn =",n)
          if n > 10**12: 
              print( "done.")
              break
          n = int(5.8284 * n)
      n += 1


P100(1)
'''
x = 1/2 (sqrt(2 n^2 - 2 n + 1) + 1)

http://www.research.att.com/projects/OEIS?Anum=A029549
patron :
a(n) = 6*a(n-1) - a(n-2) - 2 with a(0) = 1, a(1) = 3. 
1, 3, 15, 85, 493, 2871, 16731, 97513, 568345, 3312555, 19306983, 112529341, 655869061, 3822685023, 22280241075, 129858761425, 756872327473, 4411375203411, 25711378892991, 149856898154533, 873430010034205, 5090723162050695, 29670908962269963
Diophantine pairs
Solucion : 756872327473
'''

