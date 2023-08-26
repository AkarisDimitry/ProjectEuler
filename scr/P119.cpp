#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <string>
#include <cmath>

using namespace std;

// Function to get the sum of digits of a number
int sum_of_digits(long long n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// Timer decorator equivalent
template<typename Func>
auto timer(Func func, int N) {
    clock_t start = clock();
    auto result = func(N);
    double duration = (clock() - start) / (double)CLOCKS_PER_SEC;
    cout << "Result: " << result << " (execution time " << duration << "s)" << endl;
    return result;
}

long long P119(int N = 30) {
    vector<long long> numbers_with_property;


    // Max value for long long
    const long long MAX_LL = numeric_limits<long long>::max();

    // Consider sums from 2 to 300 (chosen based on Python code)
    for (int digit_sum = 2; digit_sum <= 500; ++digit_sum) {
        int i = 1;

        while (true) {
            // Check for potential overflow
            if (digit_sum > pow(MAX_LL, 1.0/i)) {
                break;
            }


            long long num = pow(digit_sum, i);
            cout << "Result: " << num << " (ds " << digit_sum << " (numL "  << to_string(num).length() << " (execution time " << endl;
            if (sum_of_digits(num) == digit_sum && num > 10) {
                numbers_with_property.push_back(num);
            }

            // If number of digits in num > digit_sum, break the loop
            if (to_string(num).length() > digit_sum) {
                break;
            }

            i++;
        }
    }

    // Sort the numbers
    sort(numbers_with_property.begin(), numbers_with_property.end());

    // Return the Nth number
    return numbers_with_property[N-1];
}

int main() {
    // Call the function with timer
    timer(P119, 30);

    return 0;
}
