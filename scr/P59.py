from functions import *
import time, copy
from decimal import *
from fractions import Fraction
import itertools

np.set_printoptions(suppress=True,
   formatter={'float_kind':'{:f}'.format})

@timer
def P59(N=1000000, v=False): 
	'''
	Each character on a computer is assigned a unique code and the preferred standard
	 is ASCII (American Standard Code for Information Interchange). For example, uppercase
	  A = 65, asterisk (*) = 42, and lowercase k = 107.

	A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR 
	each byte with a given value, taken from a secret key. The advantage with the XOR function 
	is that using the same encryption key on the cipher text, restores the plain text; for example,
	 65 XOR 42 = 107, then 107 XOR 42 = 65.

	For unbreakable encryption, the key is the same length as the plain text message, and the key is
	 made up of random bytes. The user would keep the encrypted message and the encryption key in different
	  locations, and without both "halves", it is impossible to decrypt the message.

	Unfortunately, this method is impractical for most users, so the modified method is to use a password
	 as a key. If the password is shorter than the message, which is likely, the key is repeated
	  cyclically throughout the message. The balance for this method is using a sufficiently long 
	  password key for security, but short enough to be memorable.

	Your task has been made easy, as the encryption key consists of three lower case characters. 
	Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted
	 ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the
	  message and find the sum of the ASCII values in the original text.
	'''
	def is_word(word):
		if len(word)>2 and word in words:	
			return True

	def could_be_word(word):
		Lword = len(word)
		for n in words:
			if len(n) >= Lword:
				if n[:Lword] == word:
					return True

		return False

	def is_sentence(sentence):
		if len(sentence.split(' ')) == 2: 
			print(sentence.split(' '))


		for word in sentence.split(' ')[:-1]:
			if not is_word(word):
				return False
		if not could_be_word(sentence.split(' ')[-1]):
			return False

		return True

	def cypher_iter(cypher, pos, key, msj):
		if pos < 30:
			for k in range(200):

				L = chr(cypher[pos]^k)
				if L in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
							'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
							'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
							'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:

					#msj_dc = de_crip(key+[k], cypher)

					if L == ' ' and is_word(msj[-1]): 
						cypher_iter(cypher, pos+1, key+[k], msj+[''])

					elif could_be_word(msj[-1]+L):
						print(msj)
						msj1 = copy.copy(msj)
						msj1[-1] += L
						cypher_iter(cypher, pos+1, key+[k], msj1)

	def has_chr(msj, tolerance=15):
		for c in msj:
			if not c in [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
								'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
								'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
								'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
								'.', ',', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
								'[',']','{','}','=','-','+',]:
				tolerance -= 1
				if tolerance == 0:
					return False

		return True

	def cypher_all(cypher):
		for N in range(2, 20):
			for key in itertools.product( list(range(20)), repeat=N):
				msj_dc = de_crip(key, cypher)
				if has_chr(msj_dc): 
					print('123', key)
					if is_sentence(msj_dc):
						print('123', key)

	def cypher_periodic(cypher):
		for N in range(2, 10):
			key = [0 for n in range(N)]
			for p in range(N):

				for k in range(200):
					msj_dc = de_crip( [k], cypher[p::N])
					if has_chr(msj_dc):
						key[p] = chr(k)
						print(f'{p}/{N}')
						print(key)

	def de_crip(key, cypher):
		Rkey = key * int(1+len(cypher)/len(key))
		msj = ''.join([ chr(c^Rkey[i]) for i, c in enumerate(cypher)])
		return msj 

	def msj_sum(msj):
		return np.sum( [ord(n) for n in msj] )

	file = open('../files/problem59.txt')
	cypher = [ int(n) for n in list(file)[0].split(',')]

	file = open('../files/wordlist.10000')
	words = [ n[:-1] for n in file]

	#cypher_periodic(cypher)
	#cypher_iter(cypher, 0, [], [''])

	return msj_sum(de_crip([101, 120, 112], cypher))

P59( N=1000 )  # pass: exp