import numpy as np
import matplotlib as plt
from functions import *

import time 
from functools import reduce

@timer
#@jit('int64(int64)', nopython=True) # , nopython=True, 
def P804(N=10):
    

    n = N
    counter = 2*int(np.sqrt(n))
    for i in range(1, n+1): 
        if(4*n-163*i*i<0): 
            break
        upper = (-i+int(np.sqrt(i*i+4*n-164*i*i))//2)
        lower = -i-upper
        counter+=(upper-lower+1)*2

    return counter



P804(N=10**16)
