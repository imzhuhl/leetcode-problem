"""
回溯 + 剪枝
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def search(remain, idx):
            for i in range(idx, len(candidates)):
                c = candidates[i]
                if c == remain:
                    rst.append(path + [c])
                elif c < remain:
                    path.append(c)
                    search(remain - c, i)
                    path.pop()
                else:
                    return         
            return 

        rst = []
        path = []
        candidates.sort()
        search(target, 0)
        return rst


def testCombinationSum():
    test_case = [
        {
            'candidates': [2, 3, 7, 6],
            'target': 7
        },
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        # import ipdb; ipdb.set_trace()
        rst = solu.combinationSum(item['candidates'], item['target'])
        print('result = {}\n'.format(rst))


if __name__ == '__main__':
    testCombinationSum()
