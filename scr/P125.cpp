// Include necessary libraries.
#include <iostream>  // For input and output.
#include <set>       // For set data structure.
#include <cmath>     // For math functions like sqrt.
#include <string>    // For string manipulation functions.
#include <algorithm> // For algorithms like reverse.

using namespace std;  // Use the standard namespace to avoid prepending std:: to every standard library object.

// Function that calculates all the sums of consecutive squares up to N.
// Function to compute all possible sums of consecutive squares up to a given number N.
// Time Complexity: O(sqrt(N) * sqrt(N)) = O(N) since we have two nested loops running up to sqrt(N).
// Space Complexity: O(N) as the set can hold up to N/2 sums.
set<long long> squared_sum(int N) {
    // Set to store the sums of consecutive squares.
    set<long long> squared_sum_numbers;

    // Calculate the maximum number whose square will be less than N.
    int max_square = static_cast<int>(sqrt(N)) + 1;

    // Iterate over all numbers less than max_square.
    for (int n = 1; n < max_square; ++n) {
        long long s = 0;  // Variable to store the sum of squares.

        // Calculate the sum of squares starting from n.
        for (int m = n; m < max_square; ++m) {
            s += static_cast<long long>(m) * m;  // Add m^2 to the sum.

            // If the sum exceeds N, break out of the loop.
            if (s > N) {
                break;
            }

            // If m is greater than n, it means we have a sum of more than one square, so add it to the set.
            if (m > n) {
                squared_sum_numbers.insert(s);
            }
        }
    }
    return squared_sum_numbers;  // Return the set of sums.
}

// Function that checks if a number is palindromic.
// Function to check if a given number is palindromic.
// Mathematically, a number is palindromic if its digits read the same way forwards and backwards.
// Time Complexity: O(log(num)) since we're working with the number of digits.
// Space Complexity: O(log(num)) due to the storage of the string representation of the number.
bool is_palindrome(long long num) {
    string str_num = to_string(num);  // Convert the number to a string.
    string reversed_str = str_num;   // Create a copy of the string to reverse.
    reverse(reversed_str.begin(), reversed_str.end());  // Reverse the string.
    return str_num == reversed_str;  // Check if the original and reversed strings are the same.
}

// Main function to solve the problem.
// Function to compute the sum of all numbers less than N that are both palindromic and can be written as the sum of consecutive squares.
// Time Complexity: O(N + N*log(N)) = O(N*log(N)) due to generating sums and then filtering palindromic sums.
// Space Complexity: O(N) due to storing the sums.
long long P125(int N = 50) {
    
    // <p>The palindromic number $595$ is interesting because it can be written as 
    // the sum of consecutive squares: $6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2$.
    // </p>
    // <p>There are exactly eleven palindromes below one-thousand that can be written 
    // as consecutive square sums, and the sum of these palindromes is $4164$. Note 
    // that $1 = 0^2 + 1^2$ has not been included as this problem is concerned with 
    // the squares of positive integers.</p>
    // <p>Find the sum of all the numbers less than $10^8$ that are both palindromic 
    // and can be written as the sum of consecutive squares.</p>

    

    // Get all sums of consecutive squares up to N.
    set<long long> squared_sums = squared_sum(N);

    // Set to store the sums that are also palindromic.
    set<long long> palindrome_sums;

    // Iterate over each sum and check if it's palindromic.
    for (long long s : squared_sums) {
        if (is_palindrome(s)) {
            palindrome_sums.insert(s);  // If it's palindromic, add it to the set.
        }
    }

    long long total = 0;  // Variable to store the total sum of palindromic sums.
    for (long long p : palindrome_sums) {
        total += p;  // Add each palindromic sum to the total.
    }

    return total;  // Return the total.
}

// Main function to execute the program.
int main() {
    cout << P125(100000000) << endl;  // Print the result for N = 100,000,000.
    return 0;  // End the program.
}
