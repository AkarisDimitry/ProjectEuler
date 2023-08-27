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
def P116(L:int=50, M:int=3 ) -> int: 
    def add(l, count, mem, m):
        if l in mem: return count+mem[l] 
        else:
            for l0 in range(l-m+1):
                #for ln in range(m, l-l0+1):
                count += 1 

                if l-(m+l0) >= m:
                    count = add(l-(m+l0), count, mem, m)

        return count

    mem2 = {}
    for l in range(0, L+1):
        ans = add(l, 0, mem2, 2)
        mem2[l] = ans
        if ans+1 > 10**20: break

    mem3 = {}
    for l in range(0, L+1):
        ans = add(l, 0, mem3, 3)
        mem3[l] = ans
        if ans+1 > 10**20: break

    mem4 = {}
    for l in range(0, L+1):
        ans = add(l, 0, mem4, 4)
        mem4[l] = ans
        if ans+1 > 10**20: break
    print(mem2)

    return mem2[L] + mem3[L] + mem4[L]
    
P116(L=50, M=2) # Resuldo of P116 : 20492570929 (execution time 0.0018897056579589844s)
