package leetcode

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}

	var idx int = -1
	var left, right int = 0, len(nums) - 1

	for left <= right {
		mid := (left + right) / 2
		if target == nums[mid] {
			idx = mid
			break
		} else if target < nums[mid] {
			right = mid - 1
		} else { // target > nums[mid]
			left = mid + 1
		}
	}

	if idx == -1 {
		return []int{-1, -1}
	}

	// find left margin
	l, r := left, idx
	var lidx int = -1
	for l <= r {
		mid := (l + r) / 2
		if target == nums[mid] {
			lidx = mid
			r = mid - 1
		} else if target > nums[mid] {
			l = mid + 1
		}
	}

	l, r = idx, right
	var ridx int = -1
	for l <= r {
		mid := (l + r) / 2
		if target == nums[mid] {
			ridx = mid
			l = mid + 1
		} else if target < nums[mid] {
			r = mid - 1
		}
	}

	return []int{lidx, ridx}
}
