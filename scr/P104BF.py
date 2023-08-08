import math

# function to check if a number is pandigital
def is_pandigital(n):
    digits = [str(i) for i in range(1, 10)]
    return sorted(str(n)) == digits

# we only need to calculate Fibonacci numbers modulo 10^9, since we only care about the last 9 digits
mod = 10**9

# starting values for Fibonacci sequence
f1, f2 = 1, 1

# starting values for log base 10 of Fibonacci numbers
log_f1, log_f2 = 0, math.log10(f1)

# variable to store the index of the current Fibonacci number
idx = 2

# loop until we find a Fibonacci number that is both front and back pandigital
while True:
    # calculate the next Fibonacci number modulo 10^9
    f1, f2 = f2, (f1 + f2) % mod

    # calculate the log base 10 of the next Fibonacci number
    log_f1, log_f2 = log_f2, log_f2 + log_f1 - int(log_f1)
    
    idx += 1
    # if the last 9 digits are pandigital
    if is_pandigital(f2):
        # calculate the first 9 digits
        first_9_digits = int(pow(10, log_f2 - int(log_f2) + 8))
        # if the first 9 digits are pandigital
        if is_pandigital(first_9_digits):
            break

idx
