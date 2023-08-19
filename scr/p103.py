from itertools import combinations
import numpy as np

def P103() -> int: 
    '''
    Let S(A)  represent the sum of elements in set A  of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B  and C , the following properties are true:

    S(B) != S(C); that is, sums of subsets cannot be equal.
    If B  contains more elements than C  then  S(B), S(C) .

    If S(A) is minimised for a given , we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

    n=1 : {1}
    n=2: {1,2}
    n=3: {2,3,4}
    n=4: {3,5,6,7}
    n=5: {6,9,11,12,13} 
    It seems that for a given optimum set, A = {a1,a2,...an}, the next optimum set is of the form B={b,a1+b, a2+b,...,an+b}, where  b is the "middle" element on the previous row.

    By applying this "rule" we would expect the optimum set for n=6   to be A={11,17,20,22,23,24} , with S(A)=117 . However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for  n=6 is A= {11,18,19,20,22,25} , with S(A)=115  and corresponding set string: 111819202225.

    Given that  is an optimum special sum set for n=7 , find its set string.
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

    optimum_set_n5 = [6, 9, 11, 12, 13]
    optimum_set_n6 = [11, 18, 19, 20, 22, 25]
    suboptimum_set_n7 = get_next_special_sum_set(optimum_set_n6)
    optimum_set_n7 = get_optimum_special_sum_set(suboptimum_set_n7, 0, 9999, suboptimum_set_n7)
    
    set_string_n7 = "".join(map(str, optimum_set_n7))
    return set_string_n7

print( P103() )