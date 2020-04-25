package main

import "fmt"

func numIslands(grid [][]byte) int {
	rst := 0
	for i := range grid {
		for j, v := range grid[i] {
			if v == '1' {
				dfs(i, j, grid)
				rst++
			}
		}
	}
	return rst
}

func dfs(i, j int, grid [][]byte) {
	if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[i]) {
		return
	}
	if grid[i][j] == '0' || grid[i][j] == '2' {
		return
	}
	grid[i][j] = '2'

	dfs(i+1, j, grid)
	dfs(i, j+1, grid)
	dfs(i-1, j, grid)
	dfs(i, j-1, grid)
}

func main() {
	a := [][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	}
	fmt.Println(numIslands(a))
}
