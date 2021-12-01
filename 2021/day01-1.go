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
	compteur := 0
	precedente, _ :=  strconv.Atoi(tableau[0])

	for _, nombre := range tableau[1:] {
		entier, _ := strconv.Atoi(nombre)
		if entier > precedente {
			compteur += 1
			fmt.Println(entier, " plus grand que ", precedente)
		}
		precedente = entier
	}

	fmt.Println(compteur)
}