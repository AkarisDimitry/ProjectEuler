
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
def P114(L:int=101) -> int: 
    def add(l, count, mem, m):
        if l in mem: return count+mem[l] 
        else:
            for l0 in range(l-m+1):
                for ln in range(m, l-l0+1):
                    count += 1 

                    if l-(ln+l0+1) >= m:
                        count = add(l-(ln+l0+1), count, mem, 3)

        return count

    mem = {}
    for l in range(4, L+1):
        ans = add(l, 0, mem, 3)
        mem[l] = ans

    return mem[L]+1
    
P114(L=50) # Resuldo of P114 : 16475640049 (execution time 0.000102133178710938s)
