#include <iostream>
#include <vector>

// Utilizando el espacio de nombres estándar para simplificar el código
using namespace std;

// Clase para encapsular las funciones y variables relacionadas
class EulerCoinFinder {
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
private:
    // Estructura para almacenar el resultado del Algoritmo Extendido de Euclides
    struct EGCDResult {
        long long g;
        long long x;
        long long y;
    };

    // Algoritmo Extendido de Euclides
    EGCDResult extended_gcd(long long a, long long b) {
        if (a == 0) {
            return {b, 0, 1};
        } else {
            EGCDResult temp = extended_gcd(b % a, a);
            return {temp.g, temp.y - (b / a) * temp.x, temp.x};
        }
    }

    // Función para calcular el inverso modular
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

public:
    long long compute() {
        const long long a = 1504170715041707LL;
        const long long m = 4503599627370517LL;

        vector<long long> eulercoins;
        eulercoins.push_back(a);

        long long current_eulercoin = a;
        long long inv = powmod(a, m-2, m);
        long long n = 2;

        while (true) {
            long long number = (a * n) % m;
            if (number < current_eulercoin) {
                current_eulercoin = number;
                eulercoins.push_back(number);
            }

            if (current_eulercoin == 15806432) {
                long long new_curr_eulercoin = 1;
                long long curr_max = m;

                while (new_curr_eulercoin != 15806432) {
                    number = (inv * new_curr_eulercoin) % m;
                    if (number < curr_max) {
                        curr_max = number;
                        eulercoins.push_back(new_curr_eulercoin);
                    }
                    new_curr_eulercoin++;
                }
                break;
            }
            n++;
        }

        long long sum = 0;
        for (const auto& coin : eulercoins) {
            sum += coin;
        }

        return sum;
    }
};

int main() {
    EulerCoinFinder finder;
    cout << finder.compute() << endl;
    return 0;
}
