
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, rest):
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > rest:
                    break
                
                if candidates[i] == rest:
                    rst.append(path + [candidates[i]])
                    break
                
                path.append(candidates[i])
                dfs(i + 1, rest - candidates[i])
                path.pop()
            return

        candidates.sort()
        path = []
        rst = []

        dfs(0, target)
        return rst


def testCombinationSum2():
    test_case = [
        {
            'candidates': [10,1,2,7,6,1,5],
            'target': 8
        }
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        # import ipdb; ipdb.set_trace()
        rst = solu.combinationSum2(item['candidates'], item['target'])
        print('result = {}\n'.format(rst))


if __name__ == '__main__':
    testCombinationSum2()

