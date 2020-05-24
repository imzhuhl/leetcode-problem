package main

import "fmt"

func reverse(x int) int {
	rst := 0
	for x != 0 {
		num := x % 10
		x /= 10
		rst = rst*10 + num
	}

	if rst > 2147483647 || rst < -2147483648 {
		return 0
	}
	return rst
}

func main() {
	var a int = -120
	fmt.Println(reverse(a))

}
