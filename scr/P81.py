import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P81(N=20): 
	'''
	In the 5 by 5 matrix below, the minimal path sum from 
	the top left to the bottom right, by only moving to the 
	right and down, is indicated in bold red and is equal to 2427.

	Find the minimal path sum from the top left to the bottom 
	right by only moving right and down in matrix.txt (right 
	click and "Save Link/Target As..."), a 31K text file containing 
	an 80 by 80 matrix.
	'''	
	weith_matrix = np.array([	[131,673,234,103,18 ],
								[201,96 ,342,965,150],
								[630,803,746,422,111],	
								[537,699,497,121,956],
								[805,732,524,37 ,331]])
	weith_matrix = np.array([ [ int(m) for m in line.split(',')] for line in open('/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem81.txt')] )
	wm_h, wm_w = weith_matrix.shape
	distance_matrix = np.zeros_like(weith_matrix)

	def search( wait_list, checked, suma, mov=[[1,0], [-1,0], [0,1], [0,-1]]):						
		Vmin = min(wait_list, key=lambda x: x[2])
		wait_list.remove(Vmin)
		suma += Vmin[2]

		for i, n in enumerate(wait_list):
			wait_list[i][2] -= Vmin[2]

		for x in mov:
			pos = [int(Vmin[0]+x[0]), int(Vmin[1]+x[1])]

			if pos[0] >= 0 and pos[1] >= 0 and pos[0] < wm_h and pos[1] < wm_w and not pos in checked:
				checked.append(pos)
				wait_list.append( [pos[0], pos[1], weith_matrix[pos[0], pos[1]]] )

		return wait_list, checked, suma, Vmin

	def print_checkmatrix(wait_list, elements):
		for nx in range(wm_h):
			text = ''
			for ny in range(wm_w):
				if [nx, ny] in [ [n[0], n[1]] for n in wait_list]:	text += 'O\t'
				elif [nx, ny] in elements:	text += 'X\t'
				else : 						text += ' \t'
			
			print(text)

	wait_list, checked, suma, Vmin = search( [ [0,0,weith_matrix[0,0]] ], [ [0,0] ], 0, mov=[[1,0], [0,1]] )
	while len(wait_list) > 0:
		distance_matrix[Vmin[0], Vmin[1]]  = suma
		wait_list, checked, suma, Vmin = search( wait_list, checked, suma, mov=[[1,0], [0,1]] )

	distance_matrix[Vmin[0], Vmin[1]]  = suma
	print(distance_matrix)

	return distance_matrix

P81(N= 56000)