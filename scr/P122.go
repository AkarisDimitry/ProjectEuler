// Para compilar este código:
// go build P122.go
// Luego, para ejecutar:
// ./P122 (en Linux/macOS) o P122.exe (en Windows)

package main

import (
	"fmt"
	"time"
)

func sumChain(L []int, N, sumaActual, lenthMin, lengthActual int) int {
	for i := len(L) - 1; i >= 0; i-- {
		l := L[i]
		sumaActualL := sumaActual + l

		if sumaActualL > N {
			continue
		} else if sumaActualL == N && lengthActual < lenthMin {
			lenthMin = lengthActual
		} else if sumaActualL < N && lengthActual < lenthMin {
			newL := append(L, sumaActualL)
			lenthMin = sumChain(newL, N, sumaActualL, lenthMin, lengthActual+1)
		}
	}
	return lenthMin
}

func P122(M int) int {
	total := 0
	for n := 1; n <= M; n++ {
		L := []int{1}
		total += sumChain(L, n, 0, 9999, 0)
	}
	return total
}

func main() {
	startTime := time.Now()
	result := P122(200)
	elapsedTime := time.Since(startTime)

	fmt.Printf("Resultado: %d (execution time %s)\n", result, elapsedTime)
}
