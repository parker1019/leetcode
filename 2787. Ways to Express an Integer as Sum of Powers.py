class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        sum_list = []
        i = 1
        while True:
            tmp = i ** x
            if tmp > n:
                break
            sum_list.append(tmp)
            i += 1

        dp = [0 for _ in range(n+1)]
        dp[0] = 1

        MOD = 10**9 + 7

        for num in sum_list:
            for x in range(n, num - 1, -1):
                dp[x] = (dp[x] + dp[x - num]) % MOD

        return dp[n]