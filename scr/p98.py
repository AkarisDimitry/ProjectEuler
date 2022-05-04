import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P98(self, N, BN=None, v=False):
	'''
	By replacing each of the letters in the word CARE with 1, 2, 9, and 6 
	respectively, we form a square number: 1296 = 362. What is remarkable 
	is that, by using the same digital substitutions, the anagram, RACE, 
	also forms a square number: 9216 = 962. We shall call CARE (and RACE) 
	a square anagram word pair and specify further that leading zeroes are 
	not permitted, neither may a different letter have the same digital 
	value as another letter.

	Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
	file containing nearly two-thousand common English words, find all the 
	square anagram word pairs (a palindromic word is NOT considered to be 
	an anagram of itself).

	What is the largest square number formed by any member of such a pair?
	NOTE: All anagrams formed must be contained in the given text file.
	'''
	import itertools

	def num2hash(num, dic=dicNH):
		return ''.join([dic[n] for n in num ])

	# open file
	f = open('p098_words.txt')
	for n in f:
		W = n.split(',') 
	W = [ w[1:-1] for w in W] 

	# max word length
	Wmax = max([ len(w) for w in W]) 

	# Perfect squared number proc
	dicNH = {	'9':'A', '8':'B', '7':'C',
				'6':'D', '5':'E', '4':'F',
				'3':'G', '2':'H', '1':'I', '0':'J'}
	Aps = [ int(n*n) for n in range( int( (10**Wmax)**0.5)+1 ) ]
	Aps_tree = [ [] for n in range(Wmax) ] 
	for a in Aps:	Aps_tree[len(str(a))-1].append( a )

	print( len(Aps_tree[13]) )
	asdasd

	# classification tree by word length
	Wtree = [[] for n in range(Wmax) ] 
	for w in W:	Wtree[len(w)-1].append( w )

	# classification tree by word length and ordered alphabetically
	Wstree = [ [''.join(sorted( [w1 for w1  in w])) for w in b] for b in Wtree ] 

	for k, b in enumerate(Wstree):
		for i, n1 in enumerate(b):
			for j, n2 in enumerate(b[(i+1):]):

				if n1 == n2:
					if k == 5:
						print(i, n1, j, n2)
	
	asdf
	for n in W:
		for n2 in itertools.permutations(n, len(n)):
			print(n, n2)
			if n2 in W:
				print(n, n2)

	return w