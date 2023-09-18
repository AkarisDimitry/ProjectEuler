#include <stdio.h>

// Estructura para almacenar el resultado del Algoritmo Extendido de Euclides
typedef struct {
    long long g;
    long long x;
    long long y;
} EGCDResult;

// Algoritmo Extendido de Euclides
// Complejidad temporal: O(log(min(a, b)))
// Complejidad espacial: O(1)
EGCDResult extended_gcd(long long a, long long b) {
    if (a == 0) {
        EGCDResult result = {b, 0, 1};
        return result;
    } else {
        EGCDResult temp = extended_gcd(b % a, a);
        EGCDResult result = {
            temp.g,
            temp.y - (b / a) * temp.x,
            temp.x
        };
        return result;
    }
}

// Función para calcular el inverso modular
// Complejidad temporal: O(log(m)) debido al algoritmo extendido de Euclides
// Complejidad espacial: O(1)
long long modinv(long long a, long long m) {
    EGCDResult res = extended_gcd(a, m);
    if (res.g != 1) {
        // Inverso modular no existe
        return -1;
    } else {
        return (res.x % m + m) % m; // Asegura que sea positivo
    }
}

// Función para calcular la exponenciación modular
// Complejidad temporal: O(log(exp))
// Complejidad espacial: O(1)
long long powmod(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
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
    // Inicialización de constantes y variables
    long long a = 1504170715041707LL;
    long long m = 4503599627370517LL;
    long long am_inv = modinv(a, m);
    long long eulercoins[2000]; // Array para almacenar Eulercoins. Se asume un tamaño máximo de 2000
    int coins_count = 0; // Contador de Eulercoins encontrados
    eulercoins[coins_count++] = 1504170715041707LL;

    long long current_eulercoin = 1504170715041707LL;
    long long inv = powmod(1504170715041707LL, m-2, m); // Cálculo del inverso modular
    long long n = 2;

    // Búsqueda principal de Eulercoins
    while (1) {
        long long number = (a * n) % m; // Calcula el siguiente posible Eulercoin
        if (number < current_eulercoin) {
            current_eulercoin = number;
            eulercoins[coins_count++] = number; // Almacena el Eulercoin encontrado
        }

        // Condición para cambiar de estrategia de búsqueda
        if (current_eulercoin == 15806432) {
            long long new_curr_eulercoin = 1;
            long long curr_max = m;

            // Búsqueda de abajo hacia arriba
            while (new_curr_eulercoin != 15806432) {
                number = (inv * new_curr_eulercoin) % m;
                if (number < curr_max) {
                    curr_max = number;
                    eulercoins[coins_count++] = new_curr_eulercoin;
                }
                new_curr_eulercoin++;
            }
            break;
        }
        n++;
    }

    // Suma todos los Eulercoins encontrados
    long long sum = 0;
    for (int i = 0; i < coins_count; i++) {
        sum += eulercoins[i];
    }

    // Imprime el resultado
    printf("%lld\n", sum);
    return 0;
}
