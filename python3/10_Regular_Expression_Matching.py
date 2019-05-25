import pdb, sys

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_len = len(p)
        s_len = len(s)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for j in range(p_len):  # first char must not be "*"
            if p[j] == "*":
                dp[0][j+1] = dp[0][j-1]
            else:
                dp[0][j+1] = False
        
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    if p[j-1] == s[i] or p[j-1] == ".":
                        dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
        print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))
