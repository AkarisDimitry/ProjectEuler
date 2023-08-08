from time import perf_counter
from sympy import fibonacci
from sys import set_int_max_str_digits
from itertools import count

set_int_max_str_digits(5_000_000)

def Fibgen():
    fib1,fib2,fib3 = 0,0,1
    while True:
        yield fib3
        fib1,fib2 = fib2, fib3
        fib3 = fib1+fib2

def main():
    fibgen = Fibgen()
    min_i = 2740
    for i in count(1):
        a = (next(fibgen)) % 10**9
        if i < min_i: continue
        if sorted(str(a)) == sorted("123456789"):
           if sorted(str(fibonacci(i))[:9]) == sorted("123456789"):
                return i

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(round((perf_counter() - start), 3), "sec")