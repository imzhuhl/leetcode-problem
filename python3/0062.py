
def unique_path(m, n):
    dp = []
    for i in range(m):
        dp.append([0] * n)

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

if __name__ == "__main__":
    print(unique_path(7, 3))
