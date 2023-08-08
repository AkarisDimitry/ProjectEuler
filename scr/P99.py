
import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P99(file='/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem99.txt'):
	'''
	Comparing two numbers written in index form like 211 and 37 is not difficult,
	 as any calculator would confirm that 2 11 = 2048 < 3 7 = 2187.

	However, confirming that 632382 518061 > 519432 525806 would be much more difficult, 
	as both numbers contain over three million digits.

	Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
	containing one thousand lines with a base/exponent pair on each line, determine
	which line number has the greatest numerical value.

	NOTE: The first two lines in the file represent the numbers in the example given 
	above.
	'''
	
	f = open(file, 'r')
	data = [ [ int(m) for m in n.split(',')] for n in f]
	max_index, max_base, max_exp,  = 0,data[0][0],data[0][1]

	for i, n in enumerate(data[1:]):

		print(max_index, max_base, max_exp)
		print(i, n[0], n[1] )
		print( np.log(n[0])/np.log(max_base) * max_exp )
		print( np.log(n[0])/np.log(max_base) * max_exp > n[1] )

		if (np.log(n[0])/np.log(max_base) * n[1]) > max_exp:
			max_index, max_base, max_exp = i+1, n[0], n[1]
	f.close()


	return max_index

P99()