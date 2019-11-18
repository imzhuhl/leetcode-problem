
def minDistance(word1: str, word2: str) -> int:
    len1, len2 = len(word1), len(word2)
    dp = [[0 for col in range(len1 + 1)] for row in range(len2 + 1)]
            
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i == 0:
                dp[i][j] = j
                continue
            if j == 0:
                dp[i][j] = i
                continue
            base = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if word1[j - 1] == word2[i - 1]:
                base = min(base, dp[i - 1][j - 1])
            dp[i][j] = base

    return dp[-1][-1]

if __name__ == "__main__":
    print(minDistance("intention", "execution"))