import numpy as np
import matplotlib as plt
from functions import *
import math, copy, itertools

import time 
from functools import reduce

@timer
def P89(N=20): 
	'''
	For a number written in Roman numerals to be considered valid there are basic rules which must 
	be followed. Even though the rules allow some numbers to be expressed in more than one way there 
	is always a "best" way of writing a particular number.

	For example, it would appear that there are at least six ways of writing the number sixteen:

	IIIIIIIIIIIIIIII
	VIIIIIIIIIII
	VVIIIIII
	XIIIIII
	VVVI
	XVI

	However, according to the rules only XIIIIII and XVI are valid, and the last example is
	 considered to be the most efficient, as it uses the least number of numerals.

	The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand 
	numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman 
	Numerals for the definitive rules for this problem.

	Find the number of characters saved by writing each of these in their minimal form.

	Note: You can assume that all the Roman numerals in the file contain no more than four consecutive 
	identical units.
	'''	
	def dec2roman(num:int=None) -> str:
		rules = {	1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M',}
		rules_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000,1000]
		rom = ''
		while num > 0:
			for i, m in enumerate(rules_list):
				if num < m:
					break
			num -= rules_list[i-1]
			rom += rules[rules_list[i-1]]

		return rom
		
	numbers = np.array([  str(line[:-1]) for line in open('/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem89.txt')] )
	valid = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, }
	numbers2 = [ [valid[d] for d in n] for n in numbers] 

	gain = 0
	for i, n in enumerate(numbers2):
		num = n[-1]
		for d in range(len(n)-1):
			num += n[d] if n[d] >= n[d+1] else -n[d]
		print(f'ref:{numbers[i]} - dec: {num} - new:{dec2roman(num)}')
		gain += len(numbers[i]) - len(dec2roman(num))

	return 	gain

P89(N = 0)