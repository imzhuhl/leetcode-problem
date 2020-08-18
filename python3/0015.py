"""

"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            pa = i + 1
            pb = len(nums) - 1
            cnt = 0 - nums[i]
            while pa < pb:
                if pa > i + 1 and nums[pa] == nums[pa - 1]:
                    pa += 1
                    continue
                if nums[pa] + nums[pb] == cnt:
                    rst.append([nums[i], nums[pa], nums[pb]])
                    pa += 1
                    pb -= 1
                elif nums[pa] + nums[pb] < cnt:
                    pa += 1
                else:
                    pb -= 1
        
        return rst


def testThreeSum():
    test_case = [
        [-1, 0, 1, 2, -1, -4],
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        rst = solu.threeSum(item)
        print('{}\nresult = {}\n'.format(item, rst))


if __name__ == '__main__':
    testThreeSum()
