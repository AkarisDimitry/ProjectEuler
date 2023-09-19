package main

import (
	"fmt"
	"math"
	"time"
)

func pe686(target int64) int64 {
	upperLimit := math.Log10(1.24)
	lowerLimit := math.Log10(1.23)
	n := math.Log10(math.Pow(2, 196))
	m := math.Log10(math.Pow(2, 93))
	x := math.Log10(math.Pow(2, 12710))
	i := int64(12710)
	nth := int64(45)

	for nth < target {
		x += n
		i += 196
		d := x - math.Floor(x)

		if d > lowerLimit && d < upperLimit {
			nth++
			continue
		}

		x += m
		i += 93
		d = x - math.Floor(x)

		if d > lowerLimit && d < upperLimit {
			nth++
		}
	}

	return i
}

func main() {
	startTime := time.Now()
	result := pe686(678910)
	elapsedTime := time.Since(startTime)

	fmt.Printf("pe686 took %s to run.\n", elapsedTime)
	fmt.Printf("Output: %d\n", result)
}
