from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0 for _ in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        return dp[-1]


def testRob():
    test_case = [
        [1,2,3,1],
        [2,7,9,3,1]
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        rst = solu.rob(item)
        print('{}, result = {}\n'.format(item, rst))


if __name__ == '__main__':
    testRob()