from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:  
        if not digits: return []
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }
        rst = []
        def dfs(idx: int, path: str):
            if idx == len(digits):
                rst.append(path)
                return
            for item in m[digits[idx]]:
                dfs(idx+1, path+item)
        dfs(0, "")
        return rst 

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
