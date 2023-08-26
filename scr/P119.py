import time 

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        r = func(*args, **kwargs)
        name = str(func).split(' ')[1]
        print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' ) 
        return r

    return wrapper


@timer
def P119(N:int=30) -> int: 
    # Optimized approach
    numbers_with_property = []

    def sum_of_digits(n):
        """Return the sum of the digits of n."""
        return sum(int(digit) for digit in str(n))

    # Consider sums from 2 (smallest 2-digit number is 10) to 9*7 (largest 7-digit number is 9999999)
    for digit_sum in range(2, 300 + 1):
        i = 1

        while True:
            num = digit_sum ** i
            if sum_of_digits(num) == digit_sum and num > 10:
                numbers_with_property.append(num)
            # If number of digits in num > digit_sum, break the loop
            if len(str(num)) > digit_sum:
                break
            i += 1

    # Sort the numbers and get the 30th number
    numbers_with_property = sorted(numbers_with_property)
    return  numbers_with_property[:30]

P119() #  248155780267521
