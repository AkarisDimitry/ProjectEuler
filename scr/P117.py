'''
### Problem Description
Given a row of \( L \) units in length, we can fill it with gray square tiles of size 1 unit, and oblong tiles: red of 2 units, green of 3 units, and blue of 4 units. We want to count the number of ways we can tile the row without any gaps or overlaps.

### Real World Application
This type of problem can be related to combinatorial designs in interior decoration, architecture, or even certain manufacturing processes where different sized parts need to be fit together in a particular space without any gaps.

### Code Explanation

1. `timer` function:
   This is a decorator function which, when added before any function (as `@timer`), will measure the execution time of that function.
'''
import time 

def timer(func):
    # The wrapper function is a common pattern in decorators.
    # It 'wraps' the functionality of the original function.
    def wrapper(*args, **kwargs):
        before = time.time()  # Capture start time
        r = func(*args, **kwargs)  # Execute the original function
        name = str(func).split(' ')[1]  
        print(f'Resuldo of {name} : {r} (execution time {time.time()-before}s)') 
        return r

    return wrapper  # Return the wrapper function
'''
2. `P117` function:
   This is the main function that solves the tiling problem.
'''
@timer  # This will measure the execution time of P117
def P117(L:int=50, M:int=3 ) -> int: 
    # This nested function 'add' is a recursive function to calculate the number of ways 
    # to tile the remaining space of length 'l'
    def add(l, count, mem, m):
        # If the value is in memoization, return it
        if l in mem: return count+mem[l] 
        else:
            # For each possible start position of the oblong tile
            for l0 in range(l-m+1):
                # For each possible length of the oblong tile
                for ln in range(m, min([5, l-l0+1])):
                    count += 1 
                    # If there's remaining space, recursively count for that space
                    if l-(ln+l0) >= m:
                        count = add(l-(ln+l0), count, mem, m)
        return count

    mem = {}  # Dictionary for memoization to improve time complexity
    for l in range(0, L+1):
        ans = add(l, 0, mem, 2)  # Count ways for each length 'l'
        mem[l] = ans  # Store the result for reusability
        # A condition to break out early if the number of ways exceeds a large number
        if ans+1 > 10**20: break

    return mem[L] + 1  # Return the number of ways for length 'L'
'''
### Time Complexity:
The time complexity is difficult to pin down precisely due to the recursive nature of the function and the memoization (which reduces the number of redundant calculations). However, without memoization, the complexity would be exponential. With memoization, it reduces considerably, but still retains a polynomial component due to the nested loops.

### Space Complexity:
The space complexity is \( O(L) \) due to the memoization dictionary `mem` which stores a value for each possible length up to \( L \).
'''

P117(L=50) # Resuldo of P117 : 100808458960497 (execution time 0.0008766651153564453s)
