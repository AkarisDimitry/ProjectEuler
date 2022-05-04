import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P13(N, BN=None, v=False):
	'''
	Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
	'''
	f = open('problem13.txt')
	suma = 0
	for n in f:	suma += int(n[:-1]) 
	return suma