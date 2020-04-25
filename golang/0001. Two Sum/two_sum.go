package main

import "fmt"

func twoSum(nums []int, target int) []int {
	nmap := make(map[int]int)
	for i, v := range nums {
		tmp := target - v
		idx, ok := nmap[tmp]
		if ok {
			return []int{idx, i}
		}
		nmap[v] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
