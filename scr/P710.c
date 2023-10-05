#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define MOD 1000000

// Función para calcular potencia con módulo
// Time Complexity: O(log(exponent))
long long pow_mod(long long base, long long exponent, long long mod) {
    long long result = 1;
    base %= mod;

    // Itera mientras el exponente sea mayor que cero
    while (exponent > 0) {
        // Si el exponente es impar, multiplica el resultado por la base
        if (exponent % 2 == 1) {
            result = (result * base) % mod;
        }

        // Duplica la base y reduce a la mitad el exponente
        base = (base * base) % mod;
        exponent /= 2;
    }

    return result % mod;
}

// Función principal para calcular el valor deseado
// Time Complexity: Depende del número de iteraciones, pero en general es O(n*log(n))
int P710() {
    long long pal_odd = 0, pal_odd_0b2 = 2, pal_odd_0b4 = 1;
    long long twopal_odd = 0, twopal_odd_0b2 = 1, twopal_odd_0b4 = 0;
    long long twopal = 0, suma_odd = 0, suma_even = 0;
    int n = 2;

    // Bucle principal: continua hasta que se cumpla la condición deseada
    while (twopal % MOD != 0 || n < 42) {
        n += 2;

        // Calcula pal_odd usando potencia con módulo
        pal_odd = pow_mod(2, n/2 - 1, MOD);

        // Calcula twopal_odd
        twopal_odd = (suma_odd - twopal_odd_0b4 + pal_odd_0b4) % MOD;

        // Calcula twopal
        twopal = (twopal_odd + suma_even - twopal_odd_0b2 + pal_odd_0b2) % MOD;

        // Actualiza suma_odd y suma_even
        suma_odd += twopal_odd;
        suma_even += twopal_odd;

        // Reordena valores para la siguiente iteración
        pal_odd_0b4 = pal_odd_0b2;
        pal_odd_0b2 = pal_odd;
        twopal_odd_0b4 = twopal_odd_0b2;
        twopal_odd_0b2 = twopal_odd;
    }

    return n;
}

int main() {
    // Ejecuta la función y muestra el resultado
    int result = P710();
    printf("Result of P710: %d\n", result);
    return 0;
}
