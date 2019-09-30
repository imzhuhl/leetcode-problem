"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

def longest_valid_parenthese(s: str) -> int:
    d = []
    for i in range(len(s)):
        d.append(0)
    
    rst = 0
    for i in range(1, len(s)):
        p = i - 1
        while p >= 0 and d[p] != 0:
            p = p - d[p]
        
        if p >= 0 and s[p] == "(" and s[i] == ")":
            p -= 1
            while p >= 0 and d[p] != 0:
                p = p - d[p]
            d[i] = i - p
            if d[i] > rst:
                rst = d[i]
    return rst

if __name__ == "__main__":
    # import ipdb
    # ipdb.set_trace()

    print(longest_valid_parenthese("())()("))




