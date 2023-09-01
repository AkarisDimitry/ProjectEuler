import time
from itertools import combinations

# Esta función 'timer' es un decorador que mide y muestra el tiempo que tarda en ejecutarse una función.
def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()  # Guarda el tiempo actual antes de ejecutar la función.
        r = func(*args, **kwargs)  # Ejecuta la función original y guarda su resultado.
        name = str(func).split(' ')[1]  # Obtiene el nombre de la función.
        print( f'Resuldo of {name} : {r} (execution time {time.time()-before}s)' )  # Muestra el nombre, resultado y tiempo de ejecución de la función.
        return r

    return wrapper

# Esta función resuelve el problema propuesto.
@timer
def P121(n,m) -> int: 
    '''
    Disc Game Prize Fund
    Toggle Pin=121

     Show HTML problem content 
    Problem 121
    A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

    The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

    If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

    Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
    '''

    """
    Calcula la probabilidad de que un evento ocurra m o más veces en n evaluaciones.
    
    Parámetros:
    n -- número total de evaluaciones
    m -- número mínimo de veces que queremos que ocurra el evento
    
    Retorna:
    prob -- probabilidad de que el evento ocurra m o más veces en n evaluaciones
    """
    prob = 0  # Inicializa la probabilidad en 0.
    
    # Bucle que itera desde m hasta n.
    for k in range(m, n+1):
        # Genera combinaciones de tamaño k de los números del 1 al n.
        for combi in combinations(range(1, n+1), k):
            p_k = 1  # Inicializa una probabilidad parcial.
            
            # Bucle que calcula la probabilidad de sacar un disco azul en los turnos especificados en 'combi'.
            for i in combi:
                p_k *= 1/(i+1)  # Multiplica la probabilidad parcial por la probabilidad de sacar un disco azul en el turno i.
            
            # Bucle que calcula la probabilidad de sacar un disco rojo en los turnos que no están en 'combi'.
            for i in set(range(1, n+1)) - set(combi):
                p_k *= 1 - 1/(i+1)  # Multiplica la probabilidad parcial por la probabilidad de sacar un disco rojo en el turno i.
            
            prob += p_k  # Suma la probabilidad parcial al total.
    
    # Retorna el valor inverso de la probabilidad total, que indica cuánto debería pagar el banco como premio máximo.
    return int(1/prob)
    
P121(n=15, m=8) # Llamada a la función con n=15 y m=8.