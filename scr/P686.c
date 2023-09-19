#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
/*'''
Here, we are importing necessary libraries:

math for mathematical operations.
numba and its jit decorator to optimize Python functions to run as native machine code using industry-standard C compilers.
time for measuring time intervals.
'''
*/

/*
    '''
    <p>$2^7=128$ is the first power of two whose leading digits are "12".<br />
    The next power of two whose leading digits are "12" is $2^{80}$.</p>

    <p>Define $p(L, n)$ to be the $n$th-smallest value of $j$ such that the base 10 representation of $2^j$ begins with the digits of $L$.<br />
    So $p(12, 1) = 7$ and $p(12, 2) = 80$.</p>

    <p>You are also given that $p(123, 45) = 12710$.</p>

    <p>Find $p(123, 678910)$.</p>
    '''
*/

// Function to measure the execution time of another function
double timeit(clock_t start_time, clock_t end_time) {
    /*    '''
    This is a decorator function timeit which, when applied to another 
    function, measures the time that function takes to run and prints it.
     The decorator also prints the output of the function.
    '''

    """Decorator to measure the execution time of a function and show its output."""
    */
    double elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    return elapsed_time;
}

// Function to get the leading digits of 2^j
long long leading_digits_of_power_of_two(long long j, int num_digits) {
    /*    '''
    The leading_digits_of_power_of_two function calculates the first few digits of 2**j.
     It uses properties of logarithms to do this efficiently:

    j * math.log10(2) calculates the logarithm (base 10) of 2**j.
    
    The fractional part of the logarithm gives information about the leading digits of 2**j.
    By raising 10 to the power of this fractional part, we get the leading digits.
    '''

    """Get the leading digits of 2^j."""
    */

    double log_val = j * log10(2);
    double fractional_part = log_val - floor(log_val);
    double leading_value = pow(10, fractional_part);
    return (long long)(leading_value * pow(10, num_digits - 1));
}

// Function to find the nth-smallest value of j such that the base 10 representation of 2^j starts with L
long long p(long long L, long long n) {
    /*    '''
    The function p finds the n-th smallest power of 2 that starts with the digits L. It does this by iterating through powers of 2 and checking their leading digits. This function has a time complexity of ()
    O(n) and a space complexity of O(1) (excluding the storage required for the function's code and the Python interpreter).
    '''
    */
    long long j = 1;
    long long count = 0;
    int num_digits = floor(log10(L)) + 1;
    
    while (1) {
        if (leading_digits_of_power_of_two(j, num_digits) == L) {
            count++;
            if (count == n) {
                return j;
            }
        }
        j++;
    }
}

// Main function to solve the problem
int main() {
    clock_t start_time, end_time;
    long long L = 123;
    long long n = 678910;  // Note: This is a very large number. You may want to test with smaller numbers first.
    
    start_time = clock();
    long long result = p(L, n);
    end_time = clock();
    
    double elapsed_time = timeit(start_time, end_time);
    printf("p took %.5f seconds to run.\n", elapsed_time);
    printf("Output: %lld\n", result);
    
    return 0;
}
