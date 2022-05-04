from functions import *
import time
from decimal import *
import itertools 

@timer
def P42(N=1000000, v=False): 
	'''
	The nth term of the sequence of triangle numbers is given by, tn = 
	½n(n+1); so the first ten triangle numbers are:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	By converting each letter in a word to a number corresponding to its 
	alphabetical position and adding these values we form a word value. 
	For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If 
	the word value is a triangle number then we shall call the word a triangle
	word.
	
	Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
	file containing nearly two-thousand common English words, how many are 
	triangle words?
	'''
	triang_num = [ int(0.5*n*(n+1)) for n in range(1000) ]

	let2num = { n:i+1 for i, n in enumerate(['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',] ) }
	words = [ n[1:-1] for n in list(open('/home/akaris/Documents/code/Math/problems/ProyectEuler/files/problem42.txt'))[0].split(',')]
	num = [ np.sum([let2num[l] for l in w]) for w in words ]
	trian = [ int(n) in triang_num  for n in num ]

	return np.sum(trian)

P42( N=10000000 ) 