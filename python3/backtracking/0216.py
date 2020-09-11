'''
Author       : Zhu Honglin
Date         : 2020-09-11 15:19:59
LastEditTime : 2020-09-11 15:24:25
'''

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        rst = []
        self.dfs(1, k, n, path, rst)

        return rst

    def dfs(self, cur, k, rest, path, rst):
        if len(path) == k and rest == 0:
            rst.append(path.copy())
            return
        
        if len(path) == k:
            return
        
        if cur > 9:
            return
        
        path.append(cur)
        self.dfs(cur+1, k, rest-cur, path, rst)
        path.pop()

        self.dfs(cur+1, k, rest, path, rst)


if __name__ == '__main__':
    s = Solution()
    rst = s.combinationSum3(3, 9)
    print(rst)