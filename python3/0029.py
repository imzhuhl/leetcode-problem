"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

思路：
位移运算

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) is (divisor < 0 )
        dividend, divisor = abs(dividend), abs(divisor)
        rst = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                rst += i
                i <<= 1
                temp <<= 1
        if not sign:
            rst = -rst
        return min(max(-2147483648, rst), 2147483647)



if __name__ == "__main__":
    divisor = 7
    divisor <<= 1  # 相当于乘 2
    print(divisor)

    print(Solution().divide(10, 3))
