import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce
import itertools

@timer
def P22(N=10000, v=False): 
	'''
	Using names.txt (right click and 'Save Link/Target As...'), 
	a 46K text file containing over five-thousand first names, 
	begin by sorting it into alphabetical order. Then working out 
	the alphabetical value for each name, multiply this value by 
	its alphabetical position in the list to obtain a name score.

	For example, when the list is sorted into alphabetical order, 
	COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
	name in the list. So, COLIN would obtain a score of 
	938 × 53 = 49714.

	What is the total of all the name scores in the file?
	'''

	# === 1 line solution === #
	return sum([ sum([{ n:i+1 for i, n in enumerate(['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',] ) }[n1] for n1 in n[1:-1]])*(i+1) for i, n in enumerate( sorted(list(open('/home/akaris/Documents/code/Math/problems/ProyectEuler/files/problem22.txt'))[0].split(',')) ) ]) 

	'''
	#=== 3 lines solution ===#
	let2num = { n:i+1 for i, n in enumerate( 
								[	'A', 'B', 'C', 'D', 'E', 
								'F', 'G', 'H', 'I', 'J', 
								'K', 'L', 'M', 'N', 'O', 
								'P', 'Q', 'R', 'S', 'T', 
								'U', 'V', 'W', 'X', 'Y', 
								'Z',] ) }

	f = open('/home/akaris/Documents/code/Math/problems/ProyectEuler/files/problem22.txt')
	return sum([ sum([let2num[n1] for n1 in n[1:-1]])*(i+1) for i, n in enumerate( sorted(list(f)[0].split(',')) ) ]) 
	'''
P22()
