#include <iostream>
#include <cassert>

/*
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
*/

// Modulo for calculations
#define MOD 1000000007

// A function to calculate the power of a number modulo MOD
// Time Complexity: O(log(exp))
// Space Complexity: O(1)
long long power(long long base, int exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % MOD; // multiply the result by base if exp is odd
        }
        base = (base * base) % MOD; // square the base
        exp /= 2; // divide the exponent by 2
    }
    return result;
}

// A function to compute S(k) in a non-modular space
// Time Complexity: O(log(k))
// Space Complexity: O(1)
long long S(int k) {
    int n = k / 9;
    int r = k % 9 + 2;
    return (((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) / 2;
}

// A function to compute S(k) in a modular space
// Time Complexity: O(log(k))
// Space Complexity: O(1)
long long modular_S(int k) {
    int n = k / 9;
    int r = k % 9 + 2;
    return (((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) * power(2, MOD - 2) % MOD;
}

// A function to generate Fibonacci numbers up to n
// Time Complexity: O(n)
// Space Complexity: O(n)
void fib(int n, long long fib_numbers[]) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        fib_numbers[i] = a;
        long long temp = a;
        a = b;
        b = temp + b;
    }
}

// The main function to compute the result
// Time Complexity: O(n*log(k)) where n is the number of Fibonacci numbers and k is the Fibonacci number
// Space Complexity: O(n)
int main() {
    // Testing the functions
    assert(S(20) == 1074);
    assert(S(49) == 1999945);
    assert(modular_S(20) == 1074);
    assert(modular_S(49) == 1999945);

    // Calculating the result
    int n = 91;
    long long fib_numbers[n];
    fib(n, fib_numbers);

    long long result = 0;
    for (int i = 2; i < n; i++) {
        result = (result + modular_S(fib_numbers[i])) % MOD;
    }

    std::cout << "Result: " << result << std::endl;
    return 0;
}
