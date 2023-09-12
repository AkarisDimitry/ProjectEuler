/*
A number consisting entirely of ones is called a repunit. We shall
define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and gcd(n, 10) = 1, it can 
be shown that there always exists a value, k, for which R(k) is 
divisible by n, and let A(n) be the least such value of k; for 
example, A(7) = 6 and A(41) = 5.
The least value of n for which A(n) first exceeds ten is 17.
Find the least value of n for which A(n) first exceeds one-million.
*/

#include <iostream>
#include <chrono>

int P129b(int N) {
    int k_max = 0; // Initializing the maximum value of k
    for (int n = N/10-1000; n < N; n++) {
        // Ensuring the number isn't divisible by 2 or 5
        if (n % 2 != 0 && n % 5 != 0) {
            int k = 2; // Initializing the value of k
            int res = 11; // Initializing the residual value
            int res0 = 10; // Another residual value

            while (res != 0) {
                // Updating the value of res0
                res0 = (res0 * 10) % n;
                // Updating the value of res
                res = (res0 + res) % n;
                k++; // Incrementing the value of k
            }

            // Updating the maximum value of k if the current k is greater
            if (k > k_max) k_max = k;
            if (k > 1000000) break;
        }
    }
    return k_max; // Returning the maximum value of k
}

int main() {
    auto start = std::chrono::high_resolution_clock::now(); // Starting the timer
    int result = P129b(10000000); // Calling the P129b function
    auto stop = std::chrono::high_resolution_clock::now(); // Stopping the timer

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "Result of P129b : " << result << " (execution time " << duration.count()/1000.0 << " seconds)" << std::endl;
    return 0;
}
