#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
/*  g++ -o P122 P122.cpp */ 
int sum_chain(int* L, int L_size, int N, int suma_actual, int lenth_min, int length_actual) {
    for (int i = L_size - 1; i >= 0; --i) {
        int l = L[i];
        int suma_actual_l = suma_actual + l;

        if (suma_actual_l > N) {
            continue;
        } else if (suma_actual_l == N && length_actual < lenth_min) {
            lenth_min = length_actual;
        } else if (suma_actual_l < N && length_actual < lenth_min) {
            int newL_size = L_size;
            bool exists = false;
            for (int j = 0; j < L_size; j++) {
                if (L[j] == suma_actual_l) {
                    exists = true;
                    break;
                }
            }
            
            if (!exists) {
                newL_size++;
            }

            int* newL = (int*) malloc(newL_size * sizeof(int));
            for (int j = 0; j < L_size; j++) {
                newL[j] = L[j];
            }

            if (!exists) {
                newL[L_size] = suma_actual_l;
            }

            lenth_min = sum_chain(newL, newL_size, N, suma_actual_l, lenth_min, length_actual + 1);
            free(newL);
        }
    }
    return lenth_min;
}

int P122(int M) {
    int total = 0;
    for (int n = 1; n <= M; ++n) {
        int L[1] = {1};
        total += sum_chain(L, 1, n, 0, 9999, 0);
    }
    return total;
}

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    int result = P122(200);
    end = clock();
    
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Resultado: %d (execution time %f seconds)\n", result, cpu_time_used);
    
    return 0;
}
