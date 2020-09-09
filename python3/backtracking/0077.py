
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(cur):
            if len(path) + (n - cur + 1) < k:
                return
            
            if len(path) == k:
                rst.append(path.copy())
                return

            for i in range(cur, n+1):
                path.append(i)
                dfs(i+1)
                path.pop()
            
            return

        path = []
        rst = []
        dfs(1)
        return rst


def testCombinationSum():
    test_case = [
        [4, 2],
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        # import ipdb; ipdb.set_trace()
        rst = solu.combine(item[0], item[1])
        print('result = {}\n'.format(rst))


if __name__ == '__main__':
    testCombinationSum()
