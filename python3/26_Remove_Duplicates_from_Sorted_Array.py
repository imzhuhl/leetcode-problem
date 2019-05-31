from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_num = nums[0]
        idx = 1
        for i, val in enumerate(nums):
            if val != cur_num:
                nums[idx] = val
                idx += 1
                cur_num = val
        return idx

if __name__ == "__main__":
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))