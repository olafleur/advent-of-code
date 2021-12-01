package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	contenu, _ := os.ReadFile("day01-puzzle-input.txt")

	tableau := strings.Split(string(contenu), "\n")
	compteur := 0
	precedente := tableau[0]

	for _, nombre := range tableau[1:] {
		if nombre > precedente {
			compteur += 1
			fmt.Println(nombre, " plus grand que ", precedente)
		}
		precedente = nombre
	}

	fmt.Println(compteur)
}