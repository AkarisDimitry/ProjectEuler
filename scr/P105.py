from itertools import combinations
import numpy as np

def P105(filename) -> int: 
    '''
    Let  represent the sum of elements in set  of size . We shall call it a special sum set if for any two non-empty disjoint subsets,  and , the following properties are true:

    ; that is, sums of subsets cannot be equal.
    If  contains more elements than  then .
    For example,  is not a special sum set because , whereas  satisfies both rules for all possible subset pair combinations and .

    Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, , and find the value of .

    NOTE: This problem is related to Problem 103 and Problem 106.
    '''
    def is_special_sum_set(A):
        # S(B) != S(C); that is, sums of subsets cannot be equal.
        # If B  contains more elements than C  then  S(B), S(C) .
        n = len(A)
        sum_sets_i1 = set() # previus sum
        sum_sets = set() # all sums 
        for i in range(1, n+1):
            sum_sets_i = set() # actual sum

            for subset in combinations(A, i): # r-length tuples, in sorted order, no repeated elements

                subset_sum = sum(subset)
                # S(B) != S(C); that is, sums of subsets cannot be equal.
                if subset_sum in sum_sets: return False

                # If B  contains more elements than C  then  S(B), S(C) .
                for s in sum_sets_i1:
                    if subset_sum <= s: return False

                sum_sets_i.add(subset_sum)                
                sum_sets.add(subset_sum)

            for s in sum_sets_i: sum_sets_i1.add(s) 

        return True

    def get_next_special_sum_set(A):
        #  B={b,a1+b, a2+b,...,an+b}, where b is the "middle" element on the previous row.
        return [int(np.mean(A))+1] + [ int(np.mean(A) + a)+1 for i,a in enumerate(A)] 

    def get_optimum_special_sum_set(A, i, min_sum, opt_sum_set):

        if i < len(A):
            j = len(A)-i-1
            N = A[j]
            N_min = A[j]-4 if j == 0 else A[j-1] 
            N_max = A[j+1] if j < len(A)-1 else A[j]+4

            B = A.copy()
            #print(N ,N_max, N_min, j, i, B, A )
            for bi in range(int(N_min), int(N_max) ):
                B[j] = bi
                min_sum, opt_sum_set = get_optimum_special_sum_set(B, i+1, min_sum, opt_sum_set)
                #print(A, i)

        if i == len(A):
            A_sum = sum(A)
            if A_sum < min_sum and is_special_sum_set(A):
                print(A, A_sum)
                min_sum, opt_sum_set = A_sum, A
                return min_sum, opt_sum_set

        return min_sum, opt_sum_set

    suma = 0
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the content of the file
        for n in file:
            sum_set = [int(m) for m in n.split(',')] 
            if is_special_sum_set(sum_set): suma += sum(sum_set)
    return suma

print( P105('/home/akaris/Documents/code/Math/problems/ProjectEuler/files/problem105.txt') )