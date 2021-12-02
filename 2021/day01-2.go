package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	contenu, _ := os.ReadFile("day01-puzzle-input.txt")

	tableau := strings.Split(string(contenu), "\n")
	var resultats []int

	for i := range tableau[:len(tableau)-2] {
		entier1, _ := strconv.Atoi(tableau[i])
		entier2, _ := strconv.Atoi(tableau[i+1])
		entier3, _ := strconv.Atoi(tableau[i+2])
		resultats = append(resultats, entier1 + entier2 + entier3)
	}

	compteur := 0
	precedente := resultats[0]

	for _, nombre := range resultats[1:] {
		if nombre > precedente {
			compteur += 1
		}
		precedente = nombre
	}

	fmt.Println(compteur)
}