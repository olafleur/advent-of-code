package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	contenu, _ := os.ReadFile("day03-puzzle-input.txt")

	tableau := strings.Split(string(contenu), "\n")
	var gamma []int
	var epsilon []int
	nbZeros := 0
	nbUn := 0

	for i := 0; i < len(tableau[0]); i++ {
		nbUn = 0
		nbZeros = 0
		for j := 0; j < len(tableau); j++ {
			valeur := tableau[j][i] - 48

			if valeur == 1 {
				nbUn += 1
			} else {
				nbZeros += 1
			}
		}

		if nbUn	> nbZeros {
			gamma = append(gamma, 1)
			epsilon = append(epsilon, 0)
		} else {
			gamma = append(gamma, 0)
			epsilon = append(epsilon, 1)
		}
	}

	fmt.Println(BinToDec(gamma) * BinToDec(epsilon))
}

func BinToDec(nombreBin []int) float64 {
	var nombreDec = 0.0

	for i:= 11; i >= 0; i-- {
		if nombreBin[11 - i] == 1 {
			nombreDec += math.Pow(2, float64(i))
		}
	}
	return nombreDec
}