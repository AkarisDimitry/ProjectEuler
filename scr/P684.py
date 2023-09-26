from sympy import prime
import time, math
import numpy as np
from itertools import product
from decimal import Decimal
from multiprocessing import Pool, cpu_count

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
def P684(N=int(0)) -> int:

	def power(base, exp, mod):
		'''
		Propiedad de Exponenciación:
		Para la exponenciación modular, donde queremos calcular a^b \mod ma 
		b
		 modm, utilizamos un algoritmo eficiente que explota las propiedades del operador módulo.

		La exponenciación modular se basa en las siguientes observaciones:

		(a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m(a⋅b)modm=((amodm)⋅(bmodm))modm
		(a \cdot b) \cdot c \mod m = ((a \mod m) \cdot (b \mod m) \cdot (c \mod m)) \mod m(a⋅b)⋅cmodm=((amodm)⋅(bmodm)⋅(cmodm))modm
		Entonces, para calcular a^b \mod ma 
		b
		 modm, el algoritmo es algo como esto (usando una versión de la exponenciación binaria):

		Inicializar un resultado a 11.
		Mientras b > 0b>0:
		Si bb es impar, entonces multiplicar el resultado por aa y tomar \mod mmodm.
		Dividir bb por 22 (o realizar un desplazamiento hacia la derecha si estamos trabajando en nivel de bits).
		Elevar aa al cuadrado y tomar \mod mmodm.
		El resultado final es a^b \mod ma 
		b
		 modm.
		Así, el algoritmo utiliza la propiedad de que puedes tomar el módulo en cada paso del cálculo sin afectar el resultado final.
		'''

	# Definición de las funciones y variables
	MOD = 1000000007

	def S(k):
	    n = k // 9
	    r = k % 9 + 2
	    return (((r - 1) * r + 10) * pow(10, n) - 2 * (r + 9 * n + 4)) // 2

	def modular_S(k):
	    n = k // 9
	    r = k % 9 + 2
	    return (((r - 1) * r + 10) * pow(10, n, MOD) - 2 * (r + 9 * n + 4)) * pow(2, MOD - 2, MOD) % MOD

	def fib(n):
	    a, b = 0, 1
	    result = []
	    for _ in range(n):
	        result.append(a)
	        a, b = b, a + b
	    return result

	# Verificación de las funciones

	assert S(20) == 1074
	assert S(49) == 1999945

	assert modular_S(20) == 1074
	assert modular_S(49) == 1999945

	# Cálculo del resultado

	fib_numbers = fib(91)[2:]  # Comenzando desde el tercer número de Fibonacci
	result = sum(modular_S(f) for f in fib_numbers) % MOD
	return result

P684(N=0)
