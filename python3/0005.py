'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

    输入: "cbbd"
    输出: "bb"
'''



def longest_palindrome_1(s: str) -> str:
    '''
    总共 2n-1 个位置，往两边扩展
    '''
    if len(s) == 0:
        return ''
    largest = 1
    a, b = 0, 0
    n_pos = len(s) * 2 - 1
    for i in range(1, n_pos):
        if i % 2 == 1:  # 位置出于字母之间
            left = i // 2
            right = left + 1
            length = 0
        else:  # 位置为某个字符处
            left = i // 2 - 1
            right = left + 2
            length = 1
    
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            length += 2

        if length > largest:
            largest = length
            a = left + 1
            b = right - 1

    return s[a:b+1]


def longest_palindrome_2(s: str) -> str:
    '''
    动态规划 p[i][j] 表示字符串从 i 到 j 是否为回文(0 or 1)
    '''
    if len(s) == 0:
        return ''
    longest, a, b = 1, 0, 0
    p = []
    for i in range(len(s)):
        p.append([0] * len(s))

    for i in range(len(s)):
        p[i][i] = 1
        if i < len(s) - 1 and s[i] == s[i+1]:
            if 2 > longest:
                a, b = i, i + 1
                longest = 2
            p[i][i+1] = 1
    
    # 依次查找 n 个字符的回文串，从 3 开始
    for l in range(3, len(s) + 1):
        left = 0
        right = left + l - 1
        while right < len(s):
            if s[left] == s[right] and p[left+1][right-1] == 1:
                if l > longest:
                    a, b = left, right
                p[left][right] = 1
            left += 1
            right += 1


    return s[a:b+1]


if __name__ == "__main__":
    s = 'ccc'
    # import ipdb
    # ipdb.set_trace()
    print(longest_palindrome_2(s))

