#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#define N 6
#define MOD 1000000

// Arrays to hold the sequence values. These arrays have a fixed size of 1000000 elements.
// Space Complexity for each array: O(1000000) = O(n), where n is the size of the array.
long long a[1000000];
long long u[1000000];

// Function to compute the desired value for the problem.
// Overall Time Complexity: O(n), where n is the number of iterations required to find the desired number.
int P710() {
    // Initialization of first few values of the sequences.
    u[0] = 0;
    u[1] = 0;
    u[2] = 1;
    u[3] = 0;
    a[0] = 0;
    a[1] = 1;
    a[2] = 1;
    a[3] = 1;

    int n = 3;

    // Infinite loop to keep calculating values until the desired condition is met.
    while (true) {
        // Calculate the next values of the 'a' sequence using previous values.
        // Time Complexity for each operation inside the loop: O(1)
        a[n+1] = (a[n] + a[n-1] + a[n-3]) % MOD;
        a[n+2] = (a[n+1] + a[n] + a[n-2]) % MOD;

        n += 2;

        // Calculate the next values of the 'u' sequence using previous values and the 'a' sequence.
        long long w = (u[n-2] + u[n-3]) % MOD;
        long long v = (w + a[(n-1)/2]) % MOD;

        u[n] = v;
        u[n+1] = w;

        // Breaking condition: if either of the calculated values is zero, we stop the loop.
        if (w == 0 || v == 0) {
            break;
        }
    }

    // Return the number of iterations.
    return n-1;
}

// Main function to execute the P710 function and measure its execution time.
int main() {
    // Record the starting time.
    clock_t start = clock();

    // Execute the P710 function.
    int result = P710();

    // Record the ending time.
    clock_t end = clock();

    // Calculate the elapsed time in seconds.
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    // Print the result and the execution time.
    printf("Result of P710: %d (execution time %f seconds)\n", result, time_spent);
    return 0;
}
