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
def P115(L:int=50, M:int=3) -> int: 
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
        ans = add(l, 0, mem, M)
        mem[l] = ans
        if ans+1 > 10**6: break

    return l
    
P115(L=200, M=50)
