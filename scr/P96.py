import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P96(N:int=20) -> int: 
	'''
	Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. 
	Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a 
	similar, and much more difficult, puzzle idea called Latin Squares. The objective of 
	Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such 
	that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an 
	example of a typical starting puzzle grid and its solution grid.
	p096_1.png     p096_2.png

	A well constructed Su Doku puzzle has a unique solution and can be solved by logic, 
	although it may be necessary to employ "guess and test" methods in order to eliminate
	 options (there is much contested opinion over this). The complexity of the search 
	 determines the difficulty of the puzzle; the example above is considered easy because
	  it can be solved by straight forward direct deduction.

	The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty 
	different Su Doku puzzles ranging in difficulty, but all with unique solutions (the
	 first puzzle in the file is the example above).

	By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left 
	corner of each solution grid; for example, 483 is the 3-digit number found in the top
	 left corner of the solution grid above.
	'''	
	def read(file:str):
		f = open(file, 'r')
		sudoku = []
		for line in f:
			if line[:4] == 'Grid': 	sudoku.append([])
			else:					sudoku[-1].append( [ int(n) for n in line[:-1] ])

		return sudoku

	def candidates(nx, ny, matrix):
		mnx, mny = int(nx/3), int(ny/3)
		sm1 = matrix[mnx*3:(mnx+1)*3, mny*3:(mny+1)*3]
		sm2, sm3 = matrix[:,ny], matrix[nx,:]

		return np.array([ False if n in sm1 or n in sm2 or n in sm3 else True for n in range(1,10) ])

	def eval(matrix, i):
		c = [] 
		for nx in range(9):
			for ny in range(9):
				if matrix[nx, ny] == 0:
					candidates_xy = candidates(nx, ny, matrix)
					c.append( [nx, ny, candidates_xy, np.sum(candidates_xy) ] )

		if  len(c) > 0:
			n = sorted(c, key=lambda x: x[3])[0]
			if n[3] == 0:
				return matrix

			for m in np.arange(1,10)[n[2]]:
				matrix[n[0],n[1]] = m
				matrix = eval(matrix, i+1)
				if type(matrix[0]) is str:
					return matrix

			matrix[n[0],n[1]] = 0
		else:
			return ['solved', matrix]

		return matrix

	sudokus = read('/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem96.txt')

	return np.sum( [ eval(np.array(matrix),0)[1][0,:3]*[100,10,1] for matrix in sudokus ] )

P96()