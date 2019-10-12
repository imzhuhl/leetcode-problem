"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

"""

def is_match(s, p):
    dp = []
    for i in range(len(p) + 1):
        dp.append([0] * (len(s) + 1))
    dp[0][0] = 1

    for i in range(1, len(p) + 1):
        for j in range(len(s) + 1):
            if p[i - 1].isalpha():
                if j != 0 and p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
            elif p[i - 1] == "?":
                if j != 0:
                    dp[i][j] = dp[i-1][j-1]
            else:  # "*"
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
    print(dp)
    return dp[len(p)][len(s)] == 1

if __name__ == "__main__":
    s = "acdcb"
    p = "*a*b"
    # import ipdb
    # ipdb.set_trace()
    print(is_match(s, p))
