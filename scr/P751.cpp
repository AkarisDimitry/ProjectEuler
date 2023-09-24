#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

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

/**
 * Function: gen_next
 * Description:
 *     Generates the next term in the sequence using the formula.
 * Parameters:
 *     - bn: The current term
 * Returns:
 *     The next term in the sequence.
 * Time Complexity: O(1) [Constant time]
 * Space Complexity: O(1) [Constant space]
 */
double gen_next(double bn) {
    return std::floor(bn) * (bn - std::floor(bn) + 1.0);
}

/**
 * Function: gen_sequence
 * Description:
 *     Generates the sequence up to a specified number of decimals.
 *     This function keeps generating terms until the desired precision (length) is achieved.
 * Parameters:
 *     - seed: The starting term
 *     - decimals: Desired precision/length
 * Returns:
 *     The sequence as a string.
 * Time Complexity: O(n) [Where n is the desired length/precision]
 * Space Complexity: O(n) [Storage for the number string]
 */
std::string gen_sequence(double seed, int decimals) {
    std::stringstream number;
    number << static_cast<int>(seed) << ".";  // Initialize with the integer part of seed

    // Continue until we reach the desired length/precision
    while (number.str().length() - 1 < static_cast<size_t>(decimals)) {
        seed = gen_next(seed);
        number << static_cast<int>(seed);  // Append the integer part of seed to the sequence
    }

    return number.str();
}

/**
 * Function: main
 * Description:
 *     The main driver function to find the value of theta.
 * Returns:
 *     Exit status.
 */
int main() {
    double seed = 2.2;
    std::string number;

    // Loop until the sequence becomes larger than the seed
    while (true) {
        number = gen_sequence(seed, 24);
        if (std::stod(number) > seed) {
            seed = std::stod(number);
        } else {
            break;
        }
    }

    std::cout << "Result: " << number << std::endl;
    return 0;
}
