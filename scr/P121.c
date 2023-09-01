#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// Función auxiliar para calcular las combinaciones de un conjunto.
void combine(int start, int n, int k, int* current, int currentSize, int** result, int* resultSize) {
    if (k == 0) {
        for (int i = 0; i < currentSize; i++) {
            result[*resultSize][i] = current[i];
        }
        (*resultSize)++;
        return;
    }
    for (int i = start; i <= n; i++) {
        current[currentSize] = i;
        combine(i + 1, n, k - 1, current, currentSize + 1, result, resultSize);
    }
}

// Función para verificar si un valor está en un arreglo.
bool inArray(int value, int* array, int size) {
    for (int i = 0; i < size; i++) {
        if (array[i] == value) {
            return true;
        }
    }
    return false;
}

// Función principal para resolver el problema.
int P121(int n, int m) {
    double prob = 0;

    for (int k = m; k <= n; k++) {
        int** combinations = (int**)malloc(sizeof(int*) * 100000); // Asumimos un tamaño máximo de combinaciones.
        for (int i = 0; i < 100000; i++) {
            combinations[i] = (int*)malloc(sizeof(int) * k);
        }
        int* current = (int*)malloc(sizeof(int) * k);
        int resultSize = 0;

        combine(1, n, k, current, 0, combinations, &resultSize);

        for (int i = 0; i < resultSize; i++) {
            double p_k = 1;
            for (int j = 0; j < k; j++) {
                p_k *= 1.0 / (combinations[i][j] + 1);
            }
            for (int j = 1; j <= n; j++) {
                if (!inArray(j, combinations[i], k)) {
                    p_k *= 1 - 1.0 / (j + 1);
                }
            }
            prob += p_k;
        }

        for (int i = 0; i < 100000; i++) {
            free(combinations[i]);
        }
        free(combinations);
        free(current);
    }

    return (int)(1.0 / prob);
}

int main() {
    int n = 15;
    int m = 8;

    clock_t start, end;
    double cpu_time_used;
    start = clock();

    int result = P121(n, m);

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Resultado de P121: %d (tiempo de ejecución %f s)\n", result, cpu_time_used);

    return 0;
}
