#include <stdio.h>
#include <time.h>

/**
 * Calculate the maximum remainder for a given 'a'.
 * 
 * @param a The base number for which to calculate the maximum remainder.
 * @return The maximum remainder when (a - 1)^n + (a + 1)^n is divided by a^2.
 */
int maxRemainder(int a) {
    int remainders[a * a]; // Array to store remainders
    int count = 0;
    int maxR = 0;
    int n = 1;
    int r;

    while (1) {
        r = ((int)pow(a - 1, n) + (int)pow(a + 1, n)) % (a * a);
        
        // Check if the remainder is already found
        int found = 0;
        for (int i = 0; i < count; i++) {
            if (remainders[i] == r) {
                found = 1;
                break;
            }
        }

        if (found) {
            // Break if the remainder starts repeating
            break;
        }

        remainders[count++] = r;
        if (r > maxR) {
            maxR = r;
        }

        n += 2; // Increment by 2 as even 'n' does not produce max remainder
    }

    return maxR;
}

/**
 * Main function to calculate the sum of maximum remainders for each 'a' in the range 3 to N.
 * 
 * @param N The upper limit of the range.
 * @return The sum of the maximum remainders.
 */
int P120(int N) {
    int sum = 0;
    for (int a = 3; a <= N; a++) {
        sum += maxRemainder(a);
    }
    return sum;
}

int main() {
    int N = 1000;

    clock_t start, end;
    double cpu_time_used;

    start = clock();
    int result = P120(N);
    end = clock();

    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Result of P120: %d (execution time %f seconds)\n", result, cpu_time_used);

    return 0;
}
