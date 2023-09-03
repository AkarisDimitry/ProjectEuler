import time

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
def P125(N=int(50)) -> int:
    '''
    <p>The palindromic number $595$ is interesting because it can be written as 
    the sum of consecutive squares: $6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2$.
    </p>
    <p>There are exactly eleven palindromes below one-thousand that can be written 
    as consecutive square sums, and the sum of these palindromes is $4164$. Note 
    that $1 = 0^2 + 1^2$ has not been included as this problem is concerned with 
    the squares of positive integers.</p>
    <p>Find the sum of all the numbers less than $10^8$ that are both palindromic 
    and can be written as the sum of consecutive squares.</p>

    ''' 
    # Create a list of the squares of the first 10000 numbers.
    squared = [n**2 for n in range(10000)]
    # Create a list of string representations of digits from 0 to 9.
    digits_str = [str(n) for n in range(0, 10)]
    
    # This function computes all possible sums of consecutive squares up to N.
    # It adds each sum to a set.
    def squared_sum(N):
        squared_sum_numbers = set()
        for n in range(1, int((N/2)**0.5+2)):
            suma = 0
            i = n
            while suma < N:
                suma += i**2
                i += 1
                if i > n+1: 
                    squared_sum_numbers.add(suma)
                
        return squared_sum_numbers
    
    # Complexity: O(N*sqrt(N)) in time as for each number up to sqrt(N), we're 
    # potentially adding up to N numbers. O(N) in space due to the set.
    
    # The find_sum function checks if a given number N can be expressed as a 
    # sum of consecutive squares.
    def find_sum(N):
        for n in range(int((N/2)**0.5+2)):
            suma = 0
            i = n
            while suma < N:
                suma += i**2
                i += 1
                if suma == N and i > n+1:
                    return True
        return False
    
    # Complexity: O(sqrt(N)*N) in time as for each number up to sqrt(N), we're 
    # potentially adding up to N numbers. O(1) in space.
    
    # This function generates all palindromic numbers up to a given limit.
    def generate_palindromes(limit):
        def add_digit(N):
            palindromes = []
            for n in N:
                for m in digits_str:
                    palindromes.append(m+n+m)
            return palindromes

        palindromes_filtered = []
        palindromes = ['']
        for n in digits_str:
            palindromes.append(n)
        for p in palindromes[1:]:
            if p[0] != '0' and int(p) != 0 and int(p) <= limit:
                palindromes_filtered.append(int(p))
        for n in range(int(len(str(limit))/2)):
            palindromes = add_digit(palindromes)
            for p in palindromes:
                if p[0] != '0' and int(p) != 0 and int(p) <= limit:
                    palindromes_filtered.append(int(p))
        return palindromes_filtered
    
    # Complexity: O(N) in time as it generates roughly N palindromes.
    # O(N) in space for storing the palindromes.
    
    # Generate all possible sums of consecutive squares up to N.
    squared_sums = squared_sum(N)
    
    # Check each palindrome number if it's in the set of sums of consecutive squares.
    # Return the total of such numbers.
    return sum([n if n in squared_sums else 0 for n in generate_palindromes(N)])

# Calling the function with N = 10^8
P125(N=10**7)
