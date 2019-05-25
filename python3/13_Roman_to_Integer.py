class Solution:
    def romanToInt(self, s: str) -> int:
        # ["M", "CM","D", "CD","C","XC","L","XL","X","IX","V","IV","I"]
        # [1000,900,  500, 400, 100,90,  50, 40,  10, 9,   5,   4,  1]
        rst = 0
        i = 0
        while i < len(s):
            nxt = None
            if i + 1 < len(s):
                nxt = s[i+1]
            if s[i] == "M":
                rst += 1000
            elif s[i] == "C":
                if nxt == "M":
                    rst += 900
                    i += 1
                elif nxt == "D":
                    rst += 400
                    i += 1
                else:
                    rst += 100
            elif s[i] == "D":
                rst += 500
            elif s[i] == "X":
                if nxt == "C":
                    rst += 90
                    i += 1
                elif nxt == "L":
                    rst += 40
                    i += 1
                else:
                    rst += 10
            elif s[i] == "L":
                rst += 50
            elif s[i] == "I":
                if nxt == "X":
                    rst += 9
                    i += 1
                elif nxt == "V":
                    rst += 4
                    i += 1
                else:
                    rst += 1
            else:  # V
                rst += 5
            i += 1
        return rst
            

if __name__ == "__main__":
    print(Solution().romanToInt("IV"))