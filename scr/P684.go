package main

import (
	"fmt"
)

// Propiedad de Exponenciación:
// Para la exponenciación modular, donde queremos calcular a^b \mod ma 
// b
//  modm, utilizamos un algoritmo eficiente que explota las propiedades del operador módulo.

// La exponenciación modular se basa en las siguientes observaciones:

// (a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m(a⋅b)modm=((amodm)⋅(bmodm))modm
// (a \cdot b) \cdot c \mod m = ((a \mod m) \cdot (b \mod m) \cdot (c \mod m)) \mod m(a⋅b)⋅cmodm=((amodm)⋅(bmodm)⋅(cmodm))modm
// Entonces, para calcular a^b \mod ma 
// b
//  modm, el algoritmo es algo como esto (usando una versión de la exponenciación binaria):

// Inicializar un resultado a 11.
// Mientras b > 0b>0:
// Si bb es impar, entonces multiplicar el resultado por aa y tomar \mod mmodm.
// Dividir bb por 22 (o realizar un desplazamiento hacia la derecha si estamos trabajando en nivel de bits).
// Elevar aa al cuadrado y tomar \mod mmodm.
// El resultado final es a^b \mod ma 
// b
//  modm.
// Así, el algoritmo utiliza la propiedad de que puedes tomar el módulo en cada paso del cálculo sin afectar el resultado final.



// Modulo for calculations
const MOD int64 = 1000000007

// Power calculates the power of a number modulo MOD
// Time Complexity: O(log(exp))
// Space Complexity: O(1)
func Power(base int64, exp int) int64 {
	var result int64 = 1
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % MOD // Multiply the result by base if exp is odd
		}
		base = (base * base) % MOD // Square the base
		exp /= 2                    // Divide the exponent by 2
	}
	return result
}

// S computes S(k) in a non-modular space
// Time Complexity: O(log(k))
// Space Complexity: O(1)
func S(k int) int64 {
	n := k / 9
	r := k%9 + 2
	return (((int64(r-1) * int64(r) + 10) * Power(10, n) - 2*int64(r+9*n+4)) / 2)
}

// ModularS computes S(k) in a modular space
// Time Complexity: O(log(k))
// Space Complexity: O(1)
func ModularS(k int) int64 {
	n := k / 9
	r := k%9 + 2
	return (((int64(r-1)*int64(r)+10)*Power(10, n) - 2*int64(r+9*n+4)) * Power(2, int(MOD-2))) % MOD
}

// Fib generates Fibonacci numbers up to n
// Time Complexity: O(n)
// Space Complexity: O(n)
func Fib(n int) []int64 {
	fibNumbers := make([]int64, n)
	a, b := int64(0), int64(1)
	for i := 0; i < n; i++ {
		fibNumbers[i] = a
		a, b = b, a+b
	}
	return fibNumbers
}

// Main function to compute the result
// Time Complexity: O(n*log(k)) where n is the number of Fibonacci numbers and k is the Fibonacci number
// Space Complexity: O(n)
func main() {
	// Testing the functions
	if S(20) != 1074 || S(49) != 1999945 || ModularS(20) != 1074 || ModularS(49) != 1999945 {
		panic("Function tests failed!")
	}

	// Calculating the result
	n := 91
	fibNumbers := Fib(n)
	var result int64 = 0
	for i := 2; i < n; i++ {
		result = (result + ModularS(int(fibNumbers[i]))) % MOD
	}

	fmt.Printf("Result: %d\n", result)
}
