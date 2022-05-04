import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P9(N, BN=None, v=False):
	'''
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a2 + b2 = c2

	For example, 32 + 42 = 9 + 16 = 25 = 52.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
	'''
	Ns = int(N/2)
	a = np.linspace(1, Ns, Ns, dtype=np.int32)
	a, b, c = np.meshgrid(a, a, a)
	s = a+b+c
	p = a**2 + b**2 - c**2
	L = np.logical_and(s==N, p==0)
	return a[L] * b[L] * c[L]
