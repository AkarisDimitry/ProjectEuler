package main

import (
	"fmt"
	"math"
	"time"
)

// maxRemainder calculates the maximum remainder for a given 'a'.
// It iterates through odd values of 'n' and checks the remainder
// of (a - 1)^n + (a + 1)^n when divided by a^2. If a remainder starts
// repeating, it breaks out of the loop and returns the maximum remainder.
func maxRemainder(a int) int {
	remainders := make(map[int]bool)
	maxR := 0
	n := 1

	for {
		r := (int(math.Pow(float64(a-1), float64(n))) + int(math.Pow(float64(a+1), float64(n)))) % (a * a)
		if _, found := remainders[r]; found {
			// Break if the remainder starts repeating
			break
		}
		remainders[r] = true
		if r > maxR {
			maxR = r
		}
		n += 2 // Increment by 2 as even 'n' does not produce max remainder
	}

	return maxR
}

// P120 calculates the sum of maximum remainders for each 'a' in the range 3 to N.
func P120(N int) int {
	sum := 0
	for a := 3; a <= N; a++ {
		sum += maxRemainder(a)
	}
	return sum
}

func main() {
	N := 1000

	start := time.Now()
	result := P120(N)
	duration := time.Since(start)

	fmt.Printf("Result of P120: %d (execution time %v)\n", result, duration)
}
