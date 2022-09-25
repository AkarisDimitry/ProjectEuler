import numpy as np
import matplotlib as plt
from functions import *
import math, copy

import time 
from functools import reduce

@timer
def P84(N=20): 
	'''


	In the game, Monopoly, the standard board is set up in the following way:
	p084_monopoly_board.png

	A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares 
	they advance in a clockwise direction. Without any further rules we would expect to visit each square with 
	equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes 
	this distribution.

	In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a 
	player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed
	 directly to jail.

	At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a 
	card from the top of the respective pile and, after following the instructions, it is returned to the bottom 
	of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned
	 with cards that order a movement; any instruction not concerned with movement will be ignored and the player
	  will remain on the CC/CH square.

	    Community Chest (2/16 cards):
	        Advance to GO
	        Go to JAIL
	    Chance (10/16 cards):
	        Advance to GO
	        Go to JAIL
	        Go to C1
	        Go to E3
	        Go to H2
	        Go to R1
	        Go to next R (railway company)
	        Go to next R
	        Go to next U (utility company)
	        Go back 3 squares.

	The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability 
	of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J 
	for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 
	5/8 request a movement to another square, and it is the final square that the player finishes at on each roll 
	that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we 
	shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out 
	on their next turn.

	By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit 
	numbers to produce strings that correspond with sets of squares.

	Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 
	10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed 
	with the six-digit modal string: 102400.

	If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

	'''	
	@jit('int64[:](int64[:], int64[:])', nopython=True )#, parallel=True) # fastmath=True
	def move(moves, freq):

		pos = 0
		ch = 0 
		cc = 0
		for mov in moves:	
			pos += mov
			if 	 pos in [2, 17, 33]:  # CC
				if 		cc == 0:	pos = 0  # Advance to GO
				elif 	cc == 1:	pos = 10 # Go to JAIL
				cc += 1
				if cc>=16: cc=0

			elif pos in [7, 22, 36]:  # CHG
				if   ch == 0:	pos = 0   # Advance to GO
				elif ch == 1:	pos = 10  # Go to JAIL
				elif ch == 2:	pos = 11  # Go to C1
				elif ch == 3:	pos = 24  # Go to E3
				elif ch == 4:	pos = 39  # Go to H2
				elif ch == 5:	pos = 5  # Go to R1
				elif ch == 6:	pos = int((pos+5)/10)*10+5  # Go to next R (railway company)
				elif ch == 7:	pos = int((pos+5)/10)*10+5   # Go to next R 
				elif ch == 8:	
					if pos < 10:	 pos = 12 # Go to next U (utility company) 12 28
					else:			 pos = 28 # Go to next U (utility company) 12 28
				elif ch == 9:	pos -= 3  # Go back 3 squares.
				ch += 1
				if ch>=16: ch=0

			elif pos == 30: pos = 10

			if pos >= 40:	pos -= 40

			freq[pos] += 1

		return freq
	
	counter = np.zeros(40, dtype=np.int64)

	for n in range(1000):
		freq = np.zeros(40, dtype=np.int64)
		Nrand = np.random.randint(1, 5, size=N, dtype=np.int64) + np.random.randint(1, 5, size=N, dtype=np.int64)
		freq = move( Nrand , freq )

		ind = np.argpartition(freq, -4)[-4:]
		top4 = freq[ind]

		for m in ind:	counter[m] += 1

	ind = np.argpartition(counter, -3)[-3:]
	top3 = counter[ind]

	return ind, top3*100

P84(N= 150)