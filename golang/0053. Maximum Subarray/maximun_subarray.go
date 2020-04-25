package main

import (
	"fmt"
)

func maxSubArray(nums []int) int {
	maxSum, lastSum := -1<<31, 0
	for _, v := range nums {
		curSum := lastSum + v
		if curSum > 0 {
			lastSum = curSum
		} else {
			lastSum = 0
		}
		if curSum > maxSum {
			maxSum = curSum
		}
	}
	return maxSum
}

func main() {
	nums := []int{-2}
	fmt.Println(maxSubArray(nums))
}
