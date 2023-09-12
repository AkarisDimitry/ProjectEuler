from sympy import prime
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
def P836(N=int(50)) -> int:
    '''
	<p>Let $A$ be an <b>affine plane</b> over a <b>radically integral local field</b> $F$ with 
	residual characteristic $p$.</p>
	<p>We consider an <b>open oriented line section</b> $U$ of $A$ with normalized Haar measure
	 $m$.</p>
	<p>Define $f(m, p)$ as the maximal possible discriminant of the <b>jacobian</b> associated
	 to the <b>orthogonal kernel embedding</b> of $U$ <span style="white-space:nowrap;">into
	  $A$.</span></p>
	<p>Find $f(20230401, 57)$. Give as your answer the concatenation of the first letters of 
	each bolded word.</p>
    '''
    return 'aprilfoolsjoke'


# Calling the function with N = 10^9
P836(N=0)





