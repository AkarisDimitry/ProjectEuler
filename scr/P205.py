from sympy import prime
import time, math
import numpy as np
from collections import Counter
import itertools

# A timer decorator to measure the execution time of functions.
def timer(func):
	def wrapper(*args, **kwargs):
		before = time.time()
		r = func(*args, **kwargs)
		name = str(func).split(' ')[1]
		print(f'Result of {name} : {r} (execution time {time.time()-before}s)') 
		return r
	return wrapper

@timer
def P205(N )-> int:
	''' 
	<p>Peter has nine four-sided (pyramidal) dice, each with faces numbered $1, 2, 3, 4$.<br>
	Colin has six six-sided (cubic) dice, each with faces numbered $1, 2, 3, 4, 5, 6$.</p>

	<p>Peter and Colin roll their dice and compare totals: the highest total wins. The result 
	is a draw if the totals are equal.</p>

	<p>What is the probability that Pyramidal Peter beats Cubic Colin? Give your answer rounded
	 to seven decimal places in the form 0.abcdefg.</p>
	'''
	# Function to calculate the probability distribution of dice rolls
	def calculate_probability_distribution(num_dice, sides):
	    # Generate all possible combinations of dice rolls
	    outcomes = list(itertools.product(range(1, sides + 1), repeat=num_dice))
	    # Sum the outcomes
	    sums = [sum(outcome) for outcome in outcomes]
	    # Count the frequency of each sum
	    frequency = Counter(sums)
	    # Total number of outcomes
	    total_outcomes = len(outcomes)
	    # Calculate probabilities
	    probability_distribution = {sum_: freq / total_outcomes for sum_, freq in frequency.items()}
	    return probability_distribution

	# Calculate probability distribution for Peter (9 four-sided dice)
	peter_distribution = calculate_probability_distribution(9, 4)

	# Calculate probability distribution for Colin (6 six-sided dice)
	colin_distribution = calculate_probability_distribution(6, 6)

	peter_distribution, colin_distribution

	# Calculate the probability that Peter's sum is greater than Colin's
	peter_beats_colin_probability = 0.0

	for peter_sum, peter_prob in peter_distribution.items():
	    # Sum the probabilities of Colin rolling less than Peter's sum
	    colin_prob_sum = sum(colin_prob for colin_sum, colin_prob in colin_distribution.items() if colin_sum < peter_sum)
	    # Add to the total probability
	    peter_beats_colin_probability += peter_prob * colin_prob_sum

	peter_beats_colin_probability, round(peter_beats_colin_probability, 7)

	return round(peter_beats_colin_probability, 7)


P205(N=1000)

