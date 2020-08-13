package leetcode

import (
	"fmt"
	"testing"
)

type question34 struct {
	nums   []int
	target int
}

func TestSearchRange(t *testing.T) {
	qu := []question34{
		question34{
			nums:   []int{5, 7, 7, 8, 8, 10},
			target: 8,
		},
		question34{
			nums:   []int{1},
			target: 1,
		},
	}

	fmt.Println("----------------- Test -----------------")
	for i := 0; i < len(qu); i++ {
		q := qu[i]
		fmt.Printf("nums = %v, target = %v, result = %v\n",
			q.nums, q.target, searchRange(q.nums, q.target))
	}
}
