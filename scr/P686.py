import math
from numba import jit
import time
'''
Here, we are importing necessary libraries:

math for mathematical operations.
numba and its jit decorator to optimize Python functions to run as native machine code using industry-standard C compilers.
time for measuring time intervals.
'''

def timeit(func):
    '''
    This is a decorator function timeit which, when applied to another 
    function, measures the time that function takes to run and prints it.
     The decorator also prints the output of the function.
    '''

    """Decorator to measure the execution time of a function and show its output."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function and get its result
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"{func.__name__} took {elapsed_time:.5f} seconds to run.")
        print(f"Output: {result}")
        return result
    return wrapper 

@jit('int64(int64,int64)', nopython=True)
def leading_digits_of_power_of_two(j, num_digits):
    '''
    The leading_digits_of_power_of_two function calculates the first few digits of 2**j.
     It uses properties of logarithms to do this efficiently:

    j * math.log10(2) calculates the logarithm (base 10) of 2**j.
    
    The fractional part of the logarithm gives information about the leading digits of 2**j.
    By raising 10 to the power of this fractional part, we get the leading digits.
    '''

    """Get the leading digits of 2^j."""
    log_val = j * math.log10(2)  # Calculate the log base 10 of 2^j
    fractional_part = log_val - int(log_val)  # Extract the fractional part of the log value
    leading_value = 10 ** fractional_part  # Get the leading digits by raising 10 to the fractional part
    return int(leading_value * 10**(num_digits - 1))  # Scale the leading digits to the desired number of digits

@jit('int64(int64,int64)', nopython=True)
def p(L, n):
    '''
    The function p finds the n-th smallest power of 2 that starts with the digits L. It does this by iterating through powers of 2 and checking their leading digits. This function has a time complexity of ()
    O(n) and a space complexity of O(1) (excluding the storage required for the function's code and the Python interpreter).
    '''

    """Find the nth-smallest value of j such that the base 10 representation of 2^j starts with L."""
    j = 1  # Start with the smallest power of 2
    count = 0  # Counter for how many times we've seen the desired leading digits
    num_digits = len(str(L))  # Number of digits in L
    
    while True:
        if leading_digits_of_power_of_two(j, num_digits) == L:  # Check if 2^j starts with L
            count += 1  # If so, increment the count
            if count == n:  # If we've found the nth occurrence
                return j  # Return the current j value
        j += 1  # Move to the next power of 2
    
    return j

@timeit
def P686(L, n):
    '''
    <p>$2^7=128$ is the first power of two whose leading digits are "12".<br />
    The next power of two whose leading digits are "12" is $2^{80}$.</p>

    <p>Define $p(L, n)$ to be the $n$th-smallest value of $j$ such that the base 10 representation of $2^j$ begins with the digits of $L$.<br />
    So $p(12, 1) = 7$ and $p(12, 2) = 80$.</p>

    <p>You are also given that $p(123, 45) = 12710$.</p>

    <p>Find $p(123, 678910)$.</p>
    '''
    return p(L, n)  # Call the above-defined function)

# Find p(123, 678910)
P686(L=123, n=678910) # 193060223 


