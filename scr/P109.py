import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

#from functions import timer
import math, copy

import time 
from functools import reduce
from itertools import combinations_with_replacement

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        r = func(*args, **kwargs)
        name = str(func).split(' ')[1]
        print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' ) 
        return r

    return wrapper

@timer
def P109(N:int=101) -> int: 
    '''
    In the game of darts a player throws three darts at a target board which is 
    split into twenty equal sized sections numbered one to twenty.


    The score of a dart is determined by the number of the region that the dart
     lands in. A dart landing outside the red/green outer ring scores zero. The 
     black and cream regions inside this ring represent single scores. However, 
     the red/green outer ring and middle ring score double and treble scores 
     respectively.

    At the centre of the board are two concentric circles called the bull region,
     or bulls-eye. The outer bull is worth 25 points and the inner bull is a 
     double, worth 50 points.

    There are many variations of rules but in the most popular game the players
     will begin with a score 301 or 501 and the first player to reduce their 
     running total to zero is a winner. However, it is normal to play a "doubles
      out" system, which means that the player must land a double (including the
       double bulls-eye at the centre of the board) on their final dart to win;
        any other dart that would reduce their running total to one or lower 
        means the score for that set of three darts is "bust".

    When a player is able to finish on their current score it is called a 
    "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s 
    and double bull).

    There are exactly eleven distinct ways to checkout on a score of 6:

                         
    D3      
    D1  D2  
    S2  D2  
    D2  D1  
    S4  D1  
    S1  S1  D2
    S1  T1  D1
    S1  S3  D1
    D1  D1  D1
    D1  S2  D1
    S2  S2  D1
    Note that D1 D2 is considered different to D2 D1 as they finish on different
     doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

    In addition we shall not include misses in considering combinations; for example,
     D3 is the same as 0 D3 and 0 0 D3.

    Incredibly there are 42336 distinct ways of checking out in total.

    How many distinct ways can a player checkout with a score less than 100?
   ''' 

    # Define all possible scores for a single dart
    singles = [f'S{n}' for n in range(1, 21)]  # single scores
    singles_scores = {f'S{n}':n for n in range(1, 21)}  # single scores
    
    doubles = [f'D{n}' for n in range(1, 21)] + [50] # double scores
    doubles_scores = {**{f'D{n}':n*2 for n in range(1, 21)}, **{'OB2':50} }  # double scores

    trebles = [f'T{n}' for n in range(1, 21)]  # treble scores
    trebles_scores = {f'T{n}':n*3 for n in range(1, 21)}  # treble scores

    outerbull = [f'OB']  # outer bull
    outerbull_scores = {f'OB':25 }  # outer bull

    # Combine all possible scores into a single list
    alls = singles + doubles + trebles + outerbull
    alls_scores = {**singles_scores, **doubles_scores, **trebles_scores, **outerbull_scores}

    
    count, count_list = 0, np.zeros(N+1, dtype=np.int64)
    for score in range(0,N+1):
        for S3 in doubles_scores:
            shots = []
            if alls_scores[S3] == score:
                count += 1 ; count_list[score] += 1
                shots.append([S3])
            elif alls_scores[S3] < score:

                for S1 in alls_scores:

                    if alls_scores[S1]+alls_scores[S3] == score:
                        count += 1 ; count_list[score] += 1
                        shots.append([S1])
                    elif alls_scores[S1]+alls_scores[S3] < score:

                        for S2 in alls_scores:
                            S1S2 = sorted([S1,S2])
                            if alls_scores[S1]+alls_scores[S2]+alls_scores[S3] == score and not S1S2 in shots:
                                count += 1; count_list[score] += 1
                                shots.append(S1S2)
        #print(score, count)

    '''
    print(count_list)

    # Establecer el estilo de Seaborn
    sns.set_style("whitegrid")

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.bar(range(1, count_list.shape[0]+1), count_list, color='#ff9999') # Color rojo pastel

    # Personalizar el gráfico
    ax.set_xlabel('Número del elemento', fontsize=14)
    ax.set_ylabel('Distinct ways', fontsize=14)
    ax.set_title('P109 - Darts - distinct ways per score', fontsize=16)

    # Ajustar el tamaño de las etiquetas de los ejes
    ax.tick_params(axis='both', labelsize=12)

    # Mostrar el gráfico
    plt.show()
    '''

    return count
    
P109(N=171) # 38182
'''
[  0   0   1   1   4   5  11  12  22  22  36  36  53  52  76  71 100  95
 128 120 162 148 197 181 233 211 273 241 310 275 348 305 389 335 426 368
 463 396 505 424 541 456 577 481 615 503 642 526 663 538 687 547 702 562
 713 567 728 566 730 571 724 563 727 550 714 549 699 535 695 517 676 511
 652 488 640 464 612 455 582 430 564 404 531 391 496 364 478 338 445 328
 413 303 396 277 362 266 327 240 311 215 281 207 251 184 238 159 210 153
 181 133 173 113 148 112 126  94 122  77 102  77  85  62  83  51  68  53
  56  41  55  32  44  33  33  25  35  19  27  21  20  15  23  10  15  13
  10   9  13   5   9   7   6   4   7   1   4   4   1   2   4   0   2   2
   0   0   2   0   0   1   0   0   1   0]
'''