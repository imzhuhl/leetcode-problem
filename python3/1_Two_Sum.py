from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for idx, val in enumerate(nums):
            tmp = target - val
            if tmp in nmap:
                return [nmap[tmp], idx]
            nmap[val] = idx
        return None

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    a = Solution()
    rst = a.twoSum(nums, target)
    print(rst)