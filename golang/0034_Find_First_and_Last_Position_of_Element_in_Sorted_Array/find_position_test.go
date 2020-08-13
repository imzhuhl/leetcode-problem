package leetcode

import (
	"fmt"
	"testing"
)

func TestSearchRange(t *testing.T) {
	nums := [][]int{
		[]int{5, 7, 7, 8, 8, 10},
		[]int{1},
	}
	targets := []int{8, 1}
	fmt.Println("----------------- Test -----------------")
	for i := 0; i < len(targets); i++ {
		fmt.Printf("nums = %v, target = %v, result = %v\n",
			nums[i], targets[i], searchRange(nums[i], targets[i]))
	}
}
