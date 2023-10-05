package main

import (
  "fmt"
  "time"
)

const (
  N    = 6
  MOD  = 1000000
  SIZE = 1000000
)

func P710() int {
  // Arrays to hold the sequence values. Using fixed size for simplicity.
  var a [SIZE]int64
  var u [SIZE]int64

  // Initialization of first few values of the sequences.
  u[2] = 1
  a[1] = 1
  a[2] = 1
  a[3] = 1

  n := 3

  // Infinite loop to keep calculating values until the desired condition is met.
  for {
    // Calculate the next values of the 'a' sequence using previous values.
    a[n+1] = (a[n] + a[n-1] + a[n-3]) % MOD
    a[n+2] = (a[n+1] + a[n] + a[n-2]) % MOD

    n += 2

    // Calculate the next values of the 'u' sequence using previous values and the 'a' sequence.
    w := (u[n-2] + u[n-3]) % MOD
    v := (w + a[(n-1)/2]) % MOD

    u[n] = v
    u[n+1] = w

    // Breaking condition: if either of the calculated values is zero, we stop the loop.
    if w == 0 || v == 0 {
      break
    }
  }

  // Return the number of iterations.
  return n - 1
}

func main() {
  // Record the starting time.
  start := time.Now()

  // Execute the P710 function.
  result := P710()

  // Calculate the elapsed time in seconds.
  elapsedTime := time.Since(start)

  // Print the result and the execution time.
  fmt.Printf("Result of P710: %d (execution time %s)\n", result, elapsedTime)
}
