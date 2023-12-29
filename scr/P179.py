
'''
 <p>Find the number of integers $1 \lt n \lt 10^7$, for which $n$ and $n + 1$ have
   the same number of positive divisors. For example,
 $14$ has the positive divisors $1, 2, 7, 14$ while $15$ has $1, 3, 5, 15$.</p>
'''

def optimized_count_divisors(limit):
    """Optimized function to count divisors for all numbers up to 'limit'."""
    divisors = [0] * (limit + 1)

    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            divisors[j] += 1

    return divisors

def find_matching_divisors_optimized(limit):
    """Find numbers less than 'limit' where n and n+1 have the same number of divisors, using an optimized approach."""
    divisor_counts = optimized_count_divisors(limit)
    count = 0

    for n in range(2, limit):
        if divisor_counts[n] == divisor_counts[n + 1]:
            count += 1

    return count

# Calculate for the range 1 to 10^7 with the optimized approach
optimized_result = find_matching_divisors_optimized(10**7)
optimized_result
print(optimized_result )



