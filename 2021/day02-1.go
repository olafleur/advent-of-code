package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	contenu, _ := os.ReadFile("day02-puzzle-input.txt")

	tableau := strings.Split(string(contenu), "\n")
	horizontal := 0
	descente := 0

	for i := range tableau {
		commande := strings.Split(tableau[i], " ")
		valeur, _ := strconv.Atoi(commande[1])
		switch commande[0] {
		case "up":
			descente -= valeur
		case "down":
			descente += valeur
		case "forward":
			horizontal += valeur
		}
	}

	fmt.Println(horizontal * descente)
}
