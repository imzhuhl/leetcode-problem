package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	curSet := make(map[uint8]struct{})
	var curStr []uint8
	var rst int = 0
	for i := 0; i < len(s); i++ {
		if _, ok := curSet[s[i]]; ok {
			idx := 0
			for s[i] != curStr[idx] {
				delete(curSet, curStr[idx])
				idx++
			}
			curStr = curStr[idx+1:]
			curStr = append(curStr, s[i])
		} else {
			curStr = append(curStr, s[i])
			curSet[s[i]] = struct{}{}
			if rst < len(curStr) {
				rst = len(curStr)
			}
		}
	}

	return rst
}

func main() {
	fmt.Println(lengthOfLongestSubstring(" "))
}
