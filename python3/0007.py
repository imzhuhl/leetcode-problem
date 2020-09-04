"""
"""
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        lp = rp = len(nums) - 1
        while lp > 0:
            if nums[lp - 1] < nums[lp]:
                break
            lp -= 1

        if lp != 0:
            lp -= 1
            while nums[rp] <= nums[lp]:
                rp -= 1
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
        
        # 反转 lp 及其之后的数字
        i, j = lp, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            

def testNextPermutation():
    test_case = [
        [1, 5, 1],
        [2, 3, 1],
        [1, 3, 2],
        [1, 2, 3],
        [3, 2, 1],
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        print(item, end=' -> ')
        solu.nextPermutation(item)
        print(item)


if __name__ == '__main__':
    testNextPermutation()
