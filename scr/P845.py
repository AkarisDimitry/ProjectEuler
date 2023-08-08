def count_combinations_up_to_n(n, targets):
    # The numbers we can use to sum to the targets
    numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157]

    results = {}

    for target in targets:
        # Initialize dp array
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = 1  # There is one way to sum to 0 with 0 numbers: use no numbers

        # Fill in dp array
        for num in numbers:
            for i in range(1, n+1):
                for j in range(num, target+1):
                    dp[i][j] += dp[i-1][j-num]
        
        # The number of ways to sum to the target with up to n numbers is the sum of dp[i][target] for all i
        results[target] = sum(dp[i][target] for i in range(n+1))

    return results

n = 2
targets = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157]
# Test the function with the provided targets and n = 17
a = count_combinations_up_to_n(n, targets)
print(a)
asdasd





from sympy import prime
from sympy import isprime

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def solve(N):
	counter = 0
	for P in range(1, N):

		D = sum_digits(P)
		if D in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157]:
			counter += 1
			if counter%10000 == 0:
				print(counter, D, P, D)
			elif counter == 10**16:
				print(counter, D, P, D)
				break
sda
solve(N=10**16)
