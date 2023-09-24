#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
/*
   <p>A non-decreasing sequence of integers $a_n$ can be generated from any positive real value $\theta$
     by the following procedure:
    \begin{align}
    \begin{split}
    b_1 &amp;= \theta \\
    b_n &amp;= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 
    1\right)~~~\forall ~ n \geq 2 \\
    a_n &amp;= \left\lfloor b_{n} \right\rfloor
    \end{split}
    \end{align}
    Where $\left\lfloor \cdot \right\rfloor$ is the floor function.</p>

    <p>For example, $\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 
    34, 55, 89, ...$</p>

    <p>The <i>concatenation</i> of a sequence of positive integers $a_n$ is a real value denoted $\tau$ 
    constructed by concatenating the elements of the sequence after the decimal point, starting at $a_1$: 
    $a_1.a_2a_3a_4...$</p>

    <p>For example, the Fibonacci sequence constructed from $\theta=2.956938891377988...$ yields the 
    concatenation $\tau=2.3581321345589...$ Clearly, $\tau \neq \theta$ for this value of $\theta$.</p>

    <p>Find the only value of $\theta$ for which the generated sequence starts at $a_1=2$ and the concatenation
     of the generated sequence equals the original value: $\tau = \theta$. Give your answer rounded to $24$ 
     places after the decimal point.</p>
*/

// Function to generate the next term in the sequence using the formula
// Time Complexity: O(1) [Constant time]
// Space Complexity: O(1) [Constant space]
double gen_next(double bn) {
    return floor(bn) * (bn - floor(bn) + 1);
}

// Function to generate the sequence up to a specified number of decimals
// This function keeps generating terms until the desired precision (length) is achieved.
// Time Complexity: O(n) [Where n is the desired length/precision]
// Space Complexity: O(n) [Storage for the number string]
char* gen_sequence(double seed, int decimals) {
    char *number = (char*)malloc(100 * sizeof(char));  // Allocate memory for the number string
    sprintf(number, "%d.", (int)seed);  // Initialize the string with the integer part of seed

    // Continue until we reach the desired length/precision
    while (strlen(number) - 1 < decimals) {
        seed = gen_next(seed);
        char temp[10];
        sprintf(temp, "%d", (int)seed);  // Convert the integer part of seed to string
        strcat(number, temp);  // Append to the number string
    }

    return number;
}

// Main function to find the value of theta
int main() {
    double seed = 2.2;
    char* number;

    // Keep generating sequences until the sequence is larger than the seed
    while (true) {
        number = gen_sequence(seed, 24);
        if (atof(number) > seed) {
            seed = atof(number);
        } else {
            break;
        }
    }

    printf("Result: %s\n", number);
    free(number);  // Release the allocated memory
    return 0;
}
/*
Note:

This C code uses the math.h library for the floor function.
Memory management in C requires manual handling. We allocate memory for the string using malloc and release it using free.
Instead of Decimal from Python, we use double in C. This may introduce some inaccuracies in the result.
The provided code assumes that the sequence string won't exceed 100 characters. Adjustments might be needed for larger sequences.
*/