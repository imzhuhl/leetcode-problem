package main

import "fmt"

func sortColors(nums []int) {
	curr, left, right := 0, 0, len(nums)-1
	for curr <= right {
		switch nums[curr] {
		case 0:
			nums[curr], nums[left] = nums[left], nums[curr]
			curr++
			left++
		case 1:
			curr++
		case 2:
			nums[curr], nums[right] = nums[right], nums[curr]
			right--
		}
	}
}

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Println(nums)
}
