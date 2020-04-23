package main

import (
	"fmt"
	"strconv"
	"os"
)


// # This program takes two command line variables - an amount and a tax rate and calculates the tax owing
func main() {
	cost, _ := strconv.Atoi(os.Args[1])
	tax, _ := strconv.Atoi(os.Args[2])
	taxType := os.Args[3]

	afterTax := cost * tax

	if taxType == "GST" {
		fmt.Println("GST: ", afterTax)
		// fmt.Println("GST: " + strconv.Itoa(afterTax))
	} else {
		fmt.Println("Sales Tax: ", afterTax)
       // fmt.Println("Sales Tax: " + strconv.Itoa(afterTax))
	}

}
