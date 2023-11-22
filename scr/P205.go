package main

import (
    "fmt"
    "math"
    "time"
)

// Function to generate all possible outcomes of dice rolls
func rollDice(numDice int, sides int) []int {
    outcomes := make([]int, int(math.Pow(float64(sides), float64(numDice))))
    for i := range outcomes {
        sum := 0
        temp := i
        for j := 0; j < numDice; j++ {
            sum += temp%sides + 1
            temp /= sides
        }
        outcomes[i] = sum
    }
    return outcomes
}

// Function to calculate the probability distribution
func calculateProbabilityDistribution(numDice int, sides int) map[int]float64 {
    outcomes := rollDice(numDice, sides)
    frequency := make(map[int]int)
    for _, sum := range outcomes {
        frequency[sum]++
    }

    probabilityDistribution := make(map[int]float64)
    totalOutcomes := float64(len(outcomes))
    for sum, freq := range frequency {
        probabilityDistribution[sum] = float64(freq) / totalOutcomes
    }
    return probabilityDistribution
}

// Main function to calculate the probability
func P205() float64 {
    startTime := time.Now()

    peterDistribution := calculateProbabilityDistribution(9, 4)
    colinDistribution := calculateProbabilityDistribution(6, 6)

    var peterBeatsColinProbability float64 = 0.0
    for peterSum, peterProb := range peterDistribution {
        var colinProbSum float64 = 0.0
        for colinSum, colinProb := range colinDistribution {
            if colinSum < peterSum {
                colinProbSum += colinProb
            }
        }
        peterBeatsColinProbability += peterProb * colinProbSum
    }

    elapsedTime := time.Since(startTime)
    fmt.Printf("Execution time: %s\n", elapsedTime)
    return peterBeatsColinProbability
}

func main() {
    probability := P205()
    fmt.Printf("Probability that Pyramidal Peter beats Cubic Colin: %.7f\n", probability)
}
