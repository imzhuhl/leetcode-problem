from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            return ""
        idx = 0
        for i in range(len(strs[0])):
            c = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if i == len(strs[j]):
                    return strs[0][:idx]
                if strs[j][i] != c:
                    flag = False
                    break
            if flag is False:
                break
            idx = i + 1
        return strs[0][:idx]

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if strs:
            return ""
        rst = ""
        lst = list(zip(*strs))
        for x in lst:
            st = set(x)
            if len(st) == 1:
                rst += st.pop()
            else:
                break
        return rst


if __name__ == "__main__":
    s = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix2(s))
