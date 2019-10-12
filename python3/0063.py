
def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = []
    for i in range(m):
        dp.append([0] * n)
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
            elif i != 0 and j == 0:
                dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] != 1 else 0
            else:
                dp[i][j] += dp[i-1][j] if obstacleGrid[i][j] != 1 else 0
                dp[i][j] += dp[i][j-1] if obstacleGrid[i][j] != 1 else 0

    return dp[-1][-1]

if __name__ == "__main__":
    x = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ]
    print(uniquePathsWithObstacles([[0]]))



    