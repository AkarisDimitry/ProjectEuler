#include <iostream>
#include <set>
#include <chrono>
#include <cmath>

using namespace std;
using namespace std::chrono;

/**
 * Calculate the maximum remainder for a given 'a'.
 * 
 * @param a The base number for which to calculate the maximum remainder.
 * @return The maximum remainder when (a - 1)^n + (a + 1)^n is divided by a^2.
 */
int maxRemainder(int a) {
    set<int> remainders;
    int maxR = 0;
    int n = 1;

    while (true) {
        int r = (int)(pow(a - 1, n) + pow(a + 1, n)) % (a * a);
        if (remainders.find(r) != remainders.end()) {
            // Break if the remainder starts repeating
            break;
        }
        remainders.insert(r);
        maxR = max(maxR, r);
        n += 2; // Only odd n is considered as even n will not produce the max remainder
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
    for (int a = 3; a <= N; ++a) {
        sum += maxRemainder(a);
    }
    return sum;
}

int main() {
    int N = 1000;

    // Start the timer
    auto start = high_resolution_clock::now();

    // Perform the calculation
    int result = P205(N);

    // Stop the timer
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Result of P205: " << result << " (execution time " << duration.count() << " microseconds)" << endl;
    return 0;
}
