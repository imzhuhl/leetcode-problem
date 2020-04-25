package main

import "fmt"

func longestPalindrome(s string) string {
	length := len(s)
	if length == 0 {
		return ""
	}
	p := [1000][1000]bool{} // p[i][j] 表示 s[i:j] 是否回文
	idx, maxLen := 0, 1
	for i := 0; i < length; i++ {
		p[i][i] = true
		if i >= 1 && s[i-1] == s[i] {
			p[i-1][i] = true
			idx = i - 1
			maxLen = 2
		}
	}

	for l := 3; l <= length; l++ {
		left := 0
		right := left + l - 1
		for right < length {
			if s[left] == s[right] && p[left+1][right-1] {
				p[left][right] = true
				idx = left
				maxLen = l
			}
			right++
			left++
		}
	}
	return s[idx : idx+maxLen]
}

func main() {
	s := "babad"
	fmt.Println(longestPalindrome(s))
}
