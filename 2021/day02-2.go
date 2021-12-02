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
	aim := 0

	for i := range tableau {
		commande := strings.Split(tableau[i], " ")
		valeur, _ := strconv.Atoi(commande[1])
		switch commande[0] {
		case "up":
			aim -= valeur
		case "down":
			aim += valeur
		case "forward":
			horizontal += valeur
			descente += aim * valeur
		}
	}

	fmt.Println(horizontal * descente)
}
