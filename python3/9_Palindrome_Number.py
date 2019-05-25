class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = x
        rev = 0
        while x > 0:
            tmp = x % 10
            x = x // 10
            rev = rev * 10 + tmp
        return org == rev

    def isPalindrome2(self, x: int) -> bool:
        x_str = str(x)
        return x_str[::-1] == str(x)


if __name__ == "__main__":
    Solution().isPalindrome(121)
