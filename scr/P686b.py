import decimal
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

@timeit
def pe686(target):
    upper_limit = decimal.Decimal(1.24).log10()
    lower_limit = decimal.Decimal(1.23).log10()

    n = decimal.Decimal(2**196).log10()
    m = decimal.Decimal(2**93).log10() # 289 - 196
    x = decimal.Decimal(2**12710).log10()
    i = 12710
    nth = 45
    while nth < target:
        x += n
        i += 196
        d = x % 1

        if d > lower_limit and d < upper_limit:
            nth += 1
            continue
        x += m
        i += 93
        d = x % 1
        if d > lower_limit and d < upper_limit:
            nth += 1
    return i

pe686(678910)
