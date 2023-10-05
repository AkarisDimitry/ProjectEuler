package main

import (
	"fmt"
	"math"
)

const (
	MOD = 1000000
)

// Función para calcular potencia con módulo
func powMod(base, exponent, mod int64) int64 {
	result := int64(1)
	base %= mod

	// Itera mientras el exponente sea mayor que cero
	for exponent > 0 {
		// Si el exponente es impar, multiplica el resultado por la base
		if exponent%2 == 1 {
			result = (result * base) % mod
		}

		// Duplica la base y reduce a la mitad el exponente
		base = (base * base) % mod
		exponent /= 2
	}

	return result % mod
}

// Función principal para calcular el valor deseado
func P710() int {
	var palOdd, palOdd0b2, palOdd0b4 int64 = 0, 2, 1
	var twoPalOdd, twoPalOdd0b2, twoPalOdd0b4 int64 = 0, 1, 0
	var twoPal, sumaOdd, sumaEven int64 = 0, 0, 0
	n := 2

	// Bucle principal: continua hasta que se cumpla la condición deseada
	for twoPal%MOD != 0 || n < 42 {
		n += 2

		// Calcula palOdd usando potencia con módulo
		palOdd = powMod(2, int64(n/2-1), MOD)

		// Calcula twoPalOdd
		twoPalOdd = (sumaOdd - twoPalOdd0b4 + palOdd0b4) % MOD

		// Calcula twoPal
		twoPal = (twoPalOdd + sumaEven - twoPalOdd0b2 + palOdd0b2) % MOD

		// Actualiza sumaOdd y sumaEven
		sumaOdd += twoPalOdd
		sumaEven += twoPalOdd

		// Reordena valores para la siguiente iteración
		palOdd0b4 = palOdd0b2
		palOdd0b2 = palOdd
		twoPalOdd0b4 = twoPalOdd0b2
		twoPalOdd0b2 = twoPalOdd
	}

	return n
}

func main() {
	// Ejecuta la función y muestra el resultado
	result := P710()
	fmt.Printf("Result of P710: %d\n", result)
}
