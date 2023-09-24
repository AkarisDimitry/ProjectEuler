from sympy import prime
import time, math
import numpy as np
from itertools import product
from decimal import Decimal
from multiprocessing import Pool, cpu_count

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
def P751(N=int(50)) -> int:
    '''
    <p>A non-decreasing sequence of integers $a_n$ can be generated from any positive real value $\theta$
     by the following procedure:
    \begin{align}
    \begin{split}
    b_1 &amp;= \theta \\
    b_n &amp;= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 
    1\right)~~~\forall ~ n \geq 2 \\
    a_n &amp;= \left\lfloor b_{n} \right\rfloor
    \end{split}
    \end{align}
    Where $\left\lfloor \cdot \right\rfloor$ is the floor function.</p>

    <p>For example, $\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 
    34, 55, 89, ...$</p>

    <p>The <i>concatenation</i> of a sequence of positive integers $a_n$ is a real value denoted $\tau$ 
    constructed by concatenating the elements of the sequence after the decimal point, starting at $a_1$: 
    $a_1.a_2a_3a_4...$</p>

    <p>For example, the Fibonacci sequence constructed from $\theta=2.956938891377988...$ yields the 
    concatenation $\tau=2.3581321345589...$ Clearly, $\tau \neq \theta$ for this value of $\theta$.</p>

    <p>Find the only value of $\theta$ for which the generated sequence starts at $a_1=2$ and the concatenation
     of the generated sequence equals the original value: $\tau = \theta$. Give your answer rounded to $24$ 
     places after the decimal point.</p>
    '''
    def gen_next(bn):
        return int(bn)*(bn-int(bn)+1)

    def gen_secuence(seed, decimals=24):
        num = str(int(seed))+'.'

        while len(num)-1 < decimals:
            seed = gen_next(seed)
            num += str(int(seed))

        return num

    seed = 2.2
    while True:
        number = gen_secuence(seed) 
        if Decimal(number) > seed: seed = Decimal(number)
        else: break

    return number

# sigle core version
# Fibonacci sequence constructor
#phi = 2.95693889910377988
P751(N=phi)







