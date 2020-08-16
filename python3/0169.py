from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_num = nums[0]
        cur_cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == cur_num:
                cur_cnt += 1
            else:
                if cur_cnt == 0:
                    cur_cnt = 1
                    cur_num = nums[i]
                else:
                    cur_cnt -= 1

        return cur_num
        

def testMajorityElement():
    test_case = [
        [3, 3, 4],
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        rst = solu.majorityElement(item)
        print('{}, result = {}\n'.format(item, rst))


if __name__ == '__main__':
    testMajorityElement()