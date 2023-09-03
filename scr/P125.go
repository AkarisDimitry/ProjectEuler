package main

import (
	"fmt"
	"math"
)

func isPalindrome(num int) bool {
	original := num
	reversedNum := 0
	for num > 0 {
		reversedNum = reversedNum*10 + num%10
		num /= 10
	}
	return original == reversedNum
}

func squaredSum(N int) []bool {
	maxSquare := int(math.Sqrt(float64(N))) + 1
	sums := make([]bool, N+1)

	for n := 1; n < maxSquare; n++ {
		s := 0
		for m := n; m < maxSquare; m++ {
			s += m * m
			if s > N {
				break
			}
			if m > n {
				sums[s] = true
			}
		}
	}
	return sums
}

func P125(N int) int64 {
	sums := squaredSum(N)
	palindromeSums := make([]bool, N+1)

	var total int64
	for i := 0; i <= N; i++ {
		if sums[i] && isPalindrome(i) && !palindromeSums[i] {
			total += int64(i)
			palindromeSums[i] = true
		}
	}
	return total
}

func main() {
	fmt.Println(P125(100000000))
}
