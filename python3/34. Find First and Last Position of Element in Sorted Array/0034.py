
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        idx = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                idx = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:  # target > nums[mid]
                left = mid + 1
        
        if idx == -1:
            return [-1, -1]

        # find left margin
        ll, lr = left, idx  # ll: left idx of left part, lr: right idx of left part
        lidx = -1
        while ll <= lr:
            mid = (ll + lr) // 2
            if target == nums[mid]:
                lidx = mid
                lr = mid - 1
            elif target > nums[mid]:
                ll = mid + 1
        
        # find right margin
        rl, rr = idx, right
        ridx = -1
        while rl <= rr:
            mid = (rl + rr) // 2
            if target == nums[mid]:
                ridx = mid
                rl = mid + 1
            elif target < nums[mid]:
                rr = mid - 1
        
        return [lidx, ridx]
        

if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8

    nums = [1]
    target = 1
    solution = Solution()
    print(solution.searchRange(nums, target))