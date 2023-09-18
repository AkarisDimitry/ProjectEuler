package main

/*
Bottom to top search: See Equation (2) below:

The last Eulercoin will be 1 when n = 3451657199285664, but we can reverse this 
process, if we increase the possible Eulercoin and check if n = 3451657199285664*
(possible Eulercoin) mod(4503599627370517) is smaller than the previous n

For example lets test Eulercoin = 2 =>3451657199285664*(2) mod(4503599627370517)
 = 2399714771200811, and 2399714771200811 < 3451657199285664, this means that 2 
 is also an Eulercoin

This way we only need to check Eulercoin from 1 to 15806432, which is very manageable!

######################################

Vamos a descomponer esto para que sea más claro.

La relación entre la búsqueda de \( x \) y la búsqueda de \( n \) se basa en las 
propiedades del inverso modular. Si dos números son inversos modulares entre sí 
con respecto a un módulo, multiplicarlos resultará en 1 (módulo ese módulo). En 
este caso, \( 1504170715041707 \) y \( 3451657199285664 \) son inversos modulares
 con respecto a \( 4503599627370517 \). Esto significa que:

\[
1504170715041707 \times 3451657199285664 \equiv 1 \mod 4503599627370517
\]

Esto es fundamental para entender la relación entre las dos búsquedas.

Ahora, cuando buscas "de arriba hacia abajo", estás incrementando \( n \) y 
calculando:

\[
x = 1504170715041707 \times n \mod 4503599627370517
\]

Esto te da los valores de \( x \) en orden, y estás buscando los que son más 
pequeños que el mínimo anterior.

Cuando cambias a la búsqueda "de abajo hacia arriba", estás tratando de aprovechar
 el inverso modular. Dado que sabes que el último Eulercoin es 1 cuando \( 
 n = 3451657199285664 \), puedes usar este \( n \) para "predecir" cuál será el 
 próximo Eulercoin. Haces esto multiplicando el \( n \) por un "posible Eulercoin"
  y tomando el módulo con \( 4503599627370517 \). Si el resultado es menor que el 
  \( n \) anterior, entonces ese "posible Eulercoin" es en efecto un Eulercoin.

El truco aquí es que estás utilizando la propiedad del inverso modular para "invertir"
 el cálculo. En lugar de aumentar \( n \) y ver cómo cambia \( x \), estás fijando
  \( x \) (como un "posible Eulercoin") y viendo cómo cambia \( n \). Esta inversión 
  es lo que te permite buscar de manera eficiente en el espacio de posibles Eulercoins
   en lugar de en el espacio mucho más grande de posibles valores de \( n \).

La razón por la que solo necesitas buscar hasta 15806432 es porque ese es el valor 
más pequeño que encontraste en la búsqueda "de arriba hacia abajo". Cualquier Eulercoin
 que sea mayor que ese valor ya habría sido encontrado en la búsqueda "de arriba hacia
 abajo", por lo que no es necesario buscar más allá de ese punto en la búsqueda "de
 abajo hacia arriba".
*/

import (
	"fmt"
)

// Función para calcular el Algoritmo Extendido de Euclides
func extendedGCD(a, b int64) (int64, int64, int64) {
	if a == 0 {
		return b, 0, 1
	} else {
		g, y, x := extendedGCD(b%a, a)
		return g, x - (b/a)*y, y
	}
}

// Función para calcular el inverso modular
func modInv(a, m int64) int64 {
	g, x, _ := extendedGCD(a, m)
	if g != 1 {
		panic("Inverso modular no existe")
	} else {
		return (x%m + m) % m
	}
}

// Función para calcular la exponenciación modular
func powMod(base, exp, mod int64) int64 {
	result := int64(1)
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % mod
		}
		base = (base * base) % mod
		exp /= 2
	}
	return result
}

func compute() int64 {
	a := int64(1504170715041707)
	m := int64(4503599627370517)
	var eulercoins []int64
	eulercoins = append(eulercoins, a)

	currentEulercoin := a
	inv := powMod(a, m-2, m)
	n := int64(2)

	for {
		number := (a * n) % m
		if number < currentEulercoin {
			currentEulercoin = number
			eulercoins = append(eulercoins, number)
		}

		if currentEulercoin == 15806432 {
			newCurrEulercoin := int64(1)
			currMax := m

			for newCurrEulercoin != 15806432 {
				number = (inv * newCurrEulercoin) % m
				if number < currMax {
					currMax = number
					eulercoins = append(eulercoins, newCurrEulercoin)
				}
				newCurrEulercoin++
			}
			break
		}
		n++
	}

	sum := int64(0)
	for _, coin := range eulercoins {
		sum += coin
	}

	return sum
}

func main() {
	result := compute()
	fmt.Println(result)
}
