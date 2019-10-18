from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    # print(row, col)
    dp = [[0 for j in range(col)] for i in range(row)]
    dp[0][0] = grid[0][0]

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
    
    return dp[row-1][col-1]


def minPathSum_1d(grid):
    row, col = len(grid), len(grid[0])
    dp = [0 for i in range(col)]

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                dp[j] = grid[0][0]
            elif i == 0:
                dp[j] = grid[i][j] + dp[j-1]
            elif j == 0:
                dp[j] = grid[i][j] + dp[j]
            else:
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])

    return dp[col-1]



if __name__ == "__main__":
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(minPathSum_1d(grid))
