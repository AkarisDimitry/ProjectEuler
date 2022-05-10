from functions import *
import time, copy
from decimal import *
import itertools 

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P54(N=1000000, v=False): 
	'''
	In the card game poker, a hand consists of five cards and are ranked, 
	from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

	The cards are valued in the order:
	2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

	If two players have the same ranked hands then the rank made up of the 
	highest value wins; for example, a pair of eights beats a pair of fives 
	(see example 1 below). But if two ranks tie, for example, both players have
	 a pair of queens, then highest cards in each hand are compared (see example 
	 4 below); if the highest cards tie then the next highest cards are compared, and so on.

	Consider the following five hands dealt to two players:
	Hand	 	Player 1	 	Player 2	 	Winner
	1	 	5H 5C 6S 7S KD
	Pair of Fives
		 	2C 3S 8S 8D TD
	Pair of Eights
		 	Player 2
	2	 	5D 8C 9S JS AC
	Highest card Ace
		 	2C 5C 7D 8S QH
	Highest card Queen
		 	Player 1
	3	 	2D 9C AS AH AC
	Three Aces
		 	3D 6D 7D TD QD
	Flush with Diamonds
		 	Player 2
	4	 	4D 6S 9H QH QC
	Pair of Queens
	Highest card Nine
		 	3D 6D 7H QD QS
	Pair of Queens
	Highest card Seven
		 	Player 1
	5	 	2H 2D 4C 4D 4S
	Full House
	With Three Fours
		 	3C 3D 3S 9S 9D
	Full House
	with Three Threes
		 	Player 1

	The file, poker.txt, contains one-thousand random hands dealt to two players. 
	Each line of the file contains ten cards (separated by a single space): 
	the first five are Player 1's cards and the last five are Player 2's cards. You 
	can assume that all hands are valid (no invalid characters or repeated cards), 
	each player's hand is in no specific order, and in each hand there is a clear winner.

	How many hands does Player 1 win?
	'''
	def read_hand():
		hands = []
		file = open('../files/problem54.txt')
		for line in file:
			hand = []
			for card in line[:-1].split(' '):
				hand += [ int(card[0].replace('A', '14').replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13')), card[1]] 
			hands.append(hand)

		return hands

	def High_Card(hand): return True, np.max(hand[0::2]) if not 1 in hand else 14
	
	def One_Pair(hand): 
		Vmax = -1
		for n in set(hand[0::2]):
			if hand[0::2].count(n) == 2:	Vmax = n
		return Vmax>0, Vmax

	def two_Pairs(hand): 
		Vmax = -1
		for n1 in set(hand[0::2]):
			if hand[0::2].count(n1) == 2:

				for n2 in set(hand[0::2]):
					if hand[0::2].count(n2) == 2 and n1!=n2:	Vmax = np.max( [n1, n2] )

		return Vmax>0, Vmax

	def Straight(hand): 
		Vmax = -1
		Nhand = hand[0::2]
		Nhand.sort()
		for i, n in enumerate(Nhand):
			if n-Nhand[0] != i:
				return False, -1
		return True, Nhand[-1]

	def Three_of_a_Kind(hand): 
		Vmax = -1
		for n in set(hand[0::2]):
			if hand[0::2].count(n) == 3:	Vmax = n
		return Vmax>0, Vmax

	def Flush(hand): 
		return len(set(hand[1::2]))==1, High_Card(hand)[1]

	def Full_House(hand): 
		Vmax = -1
		for n1 in set(hand[0::2]):
			if hand[0::2].count(n1) == 3:	

				for n2 in set(hand[0::2]):
					if hand[0::2].count(n2) == 2 and n1!=n2:	Vmax = np.max( [n1, n2] )

		return Vmax>0, Vmax

	def Four_of_a_Kind(hand): 
		Vmax = -1
		for n in set(hand[0::2]):
			if hand[0::2].count(n) == 4:	Vmax = n
		return Vmax>0, Vmax

	def Straight_Flush(hand): 
		return Flush(hand)[0] and Straight(hand)[0], Straight(hand)[1] 

	def Royal_Flush(hand): 
		return Flush(hand)[0] and sorted(hand[0::2])==[10,11,12,13,14], 14 

	hands, wins = read_hand(), [0, 0]
	for ij, hand in enumerate(hands):
		P1, P2   = hand[:10] , hand[10:]
		GP, Gmax = [100, 100], [  0,   0]

		for i, P in enumerate([P1, P2]):
			for j, G in enumerate([ Royal_Flush(P), Straight_Flush(P), Four_of_a_Kind(P), 
											Full_House(P), Flush(P), Straight(P),Three_of_a_Kind(P),  
											two_Pairs(P), One_Pair(P), High_Card(P)]):
				if G[0]:
					GP[i], Gmax[i]  = j, G[1]
					break

		if GP[0] != GP[1]:			wins[np.argmin([GP])] += 1
		else:						
			if Gmax[0] != Gmax[1]:	wins[np.argmax(Gmax)] += 1 
			else:							wins[np.argmax([High_Card(P1)[1], High_Card(P2)[1]])] += 1 

	return wins

P54( N=10000000 )  