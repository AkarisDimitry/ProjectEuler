// <p>A non-decreasing sequence of integers $a_n$ can be generated from any positive real value $\theta$
//   by the following procedure:
//  \begin{align}
//  \begin{split}
//  b_1 &amp;= \theta \\
//  b_n &amp;= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 
//  1\right)~~~\forall ~ n \geq 2 \\
//  a_n &amp;= \left\lfloor b_{n} \right\rfloor
//  \end{split}
//  \end{align}
//  Where $\left\lfloor \cdot \right\rfloor$ is the floor function.</p>

//  <p>For example, $\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 
//  34, 55, 89, ...$</p>

//  <p>The <i>concatenation</i> of a sequence of positive integers $a_n$ is a real value denoted $\tau$ 
//  constructed by concatenating the elements of the sequence after the decimal point, starting at $a_1$: 
//  $a_1.a_2a_3a_4...$</p>

//  <p>For example, the Fibonacci sequence constructed from $\theta=2.956938891377988...$ yields the 
//  concatenation $\tau=2.3581321345589...$ Clearly, $\tau \neq \theta$ for this value of $\theta$.</p>

//  <p>Find the only value of $\theta$ for which the generated sequence starts at $a_1=2$ and the concatenation
//   of the generated sequence equals the original value: $\tau = \theta$. Give your answer rounded to $24$ 
//   places after the decimal point.</p>

// Package main provides a solution for generating sequences from a seed value.
package main

import (
	"fmt"
	"math"
	"strconv"
)

// The genNext function is designed to produce the next term in a sequence based on a given value.
// This function computes the next term using a formula that involves the floor operation and arithmetic operations.
//
// Parameters:
//     - bn: The current term from which the next term is to be generated. It's a float64 type.
//
// Returns:
//     The function returns the next term in the sequence as a float64 type.
//
// Time Complexity:
//     The time complexity of this function is O(1), which means it runs in constant time.
//     This is because it does a fixed number of operations regardless of the size of the input.
//
// Space Complexity:
//     The space complexity is also O(1) since it uses a constant amount of space.
func genNext(bn float64) float64 {
	return math.Floor(bn) * (bn - math.Floor(bn) + 1)  // Compute the next term using the formula and return it.
}

// The genSequence function is responsible for generating a sequence of terms up to a specified number of decimals.
// The sequence is generated iteratively by continuously computing the next term until the desired precision is achieved.
//
// Parameters:
//     - seed: The initial value or starting term for the sequence generation.
//     - decimals: The desired precision or length for the generated sequence.
//
// Returns:
//     The function returns the sequence as a string.
//
// Time Complexity:
//     The time complexity of this function is O(n), where n is the desired length or precision.
//     This is because the function runs in a loop until the sequence reaches the desired length.
//
// Space Complexity:
//     The space complexity is O(n) because the function builds a string that grows with the desired length or precision.
func genSequence(seed float64, decimals int) string {
	number := strconv.Itoa(int(seed)) + "."  // Convert the seed value to its integer representation and initialize the sequence string with it.

	// This loop is used to continuously generate terms in the sequence until the desired length is achieved.
	for len(number)-1 < decimals {  
		seed = genNext(seed)                 // Generate the next term in the sequence.
		number += strconv.Itoa(int(seed))    // Convert the term to its integer representation and append it to the sequence string.
	}

	return number  // Return the generated sequence.
}

// The main function serves as the driver function for the program.
// It initializes a seed value and then generates a sequence from it.
// The function iterates until the sequence becomes larger than the seed.
func main() {
	seed := 2.2  // Initialize the seed value.
	var number string  // Declare a variable to store the generated sequence.

	// This loop iteratively generates sequences from the seed and updates the seed if the sequence is larger than the current seed.
	for {
		number = genSequence(seed, 24)           // Generate a sequence from the current seed value with a precision of 24 decimals.
		newSeed, err := strconv.ParseFloat(number, 64)  // Convert the sequence string back to a float64 type.
		if err == nil && newSeed > seed {        // If the conversion is successful and the sequence is larger than the seed, update the seed.
			seed = newSeed
		} else {
			break  // If the sequence is not larger than the seed, exit the loop.
		}
	}

	fmt.Println("Result:", number)  // Print the resulting sequence.
}
