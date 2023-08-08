
import numpy as np
import matplotlib as plt
from functions import *
import time 
from functools import reduce

@timer
def P98(file='/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem98.txt'):
	'''
	By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we 
	form a square number: 1296 = 362. What is remarkable is that, by using the same digital
	 substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call
	  CARE (and RACE) a square anagram word pair and specify further that leading zeroes are 
	  not permitted, neither may a different letter have the same digital value as another letter.

	Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
	 two-thousand common English words, find all the square anagram word pairs (a palindromic 
	 word is NOT considered to be an anagram of itself).

	What is the largest square number formed by any member of such a pair?

	NOTE: All anagrams formed must be contained in the given text file.
	'''
	def get_anagram_list(word_list):
		anagram_list = []
		for i1, n1 in enumerate(word_list):
			for i2, n2 in enumerate(word_list[i1+1:]):
				if anagram(n1, n2):
					anagram_list.append([n1, n2])	
		return anagram_list

	def get_word_list(file):	
		with open(file, 'r') as f: 	word_list = [ m[1:-1 ] for n in f  for m in n.split(',') ]
		print( 'Total words : ', len(word_list) )
		return word_list

	def int2rep(n):
		rep_dic = {}
		index = 1
		for s in str(n):
			if not s in rep_dic:
				rep_dic[s] = index
				index += 1

		rep = 0
		for i, s in enumerate(str(n)[::-1]):
			rep += rep_dic[s]*10**i

		return rep, rep_dic

	def rep2int(rep_dic, N):
		rep_dic_rev = {}
		for key, item in rep_dic.items():
			rep_dic_rev[str(item)] = key

		rep = 0
		for i, s in enumerate(str(N)[::-1]):
			rep += int(rep_dic_rev[s])*10**i

		return rep

	def str2rep(n1, n2):
		rep_dic = {}
		index = 1
		for s in str(n1):
			if not s in rep_dic:
				rep_dic[s] = index
				index += 1

		rep1 = 0
		for i, s in enumerate(str(n1)[::-1]):
			rep1 += rep_dic[s]*10**i

		rep2 = 0
		for i, s in enumerate(str(n2)[::-1]):
			rep2 += rep_dic[s]*10**i

		#print('Word1', n1, n2, rep1, rep2)
		return rep1, rep2


	word_list    = get_word_list(file)
	anagram_list = get_anagram_list(word_list)

	maxN = 0
	for n1, n2 in anagram_list:
		Srep1a, Srep2a = str2rep(n1, n2)
		N=len(n1)
		if N>3 and N>=len(str(maxN)):
			for n in [n*n for n in range( int(10**((N-1)/2))+1, int(10**(N/2)+1)) ][::-1]: 		
				Nrep, rep_dic = int2rep(n)	

				if Srep1a == Nrep:
					int2 = rep2int(rep_dic, Srep2a)

					if len(str(int2)) == len(str(n)) and is_square(int2):
						print('W1 : ', n1, n)
						print('W2 : ', n2, int2)
						print('----------')	
						if maxN < int2: maxN = int2
						if maxN < n: maxN = n
						break
	
	return maxN

P98()