from typing import List
import pdb


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rst = []

        def aux(left: int, right: int, s: str):
            if left == 0 and right == 0:
                rst.append(s)
                return
            if left == 0:
                aux(left, right-1, s+")")
            elif left == right:
                aux(left-1, right, s+"(")
            elif left < right:
                aux(left-1, right, s+"(")
                aux(left, right-1, s+")")
            return

        aux(n, n, "")
        return rst


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
