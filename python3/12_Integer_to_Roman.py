class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        rst = ""
        for i, val in enumerate(values):
            while num >= val:
                num -= val
                rst += roman[i]
        return rst
        
if __name__ == "__main__":
    print(Solution().intToRoman(1994))