

def egg_drop(k: int, n: int):
    memo = dict()
    def dp(k, n) -> int:
        # base case
        if k == 1: return n
        if n == 0: return 0
        # 避免重复计算
        if (k, n) in memo:
            return memo[(k, n)]

        res = float('inf')
        # 穷举所有可能的选择
        for i in range(1, n + 1):
            res = min(res, 
                      max(
                            dp(k, n - i), 
                            dp(k - 1, i - 1)
                         ) + 1
                  )
        # 记入备忘录
        memo[(k, n)] = res
        return res
    
    return dp(k, n)


if __name__ == '__main__':
    rst = egg_drop(2, 100)
    print(rst)
