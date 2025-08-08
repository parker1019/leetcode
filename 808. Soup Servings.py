# DP + Recursion

class Solution:
    def recursive_func(self, a: int, b: int) -> float:
        # A empty
        if a <= 0 and b > 0:
            return 1
        # Both A and B empty
        elif a <= 0 and b <= 0:
            return 0.5
        # B empty
        elif a > 0 and b <= 0:
            return 0

        # Check the dp if exist or not
        if self.dp[a][b] != -1:
            return self.dp[a][b]

        # Not empty, do the condition
        cond1 = self.recursive_func(a - 4, b - 0)
        cond2 = self.recursive_func(a - 3, b - 1)
        cond3 = self.recursive_func(a - 2, b - 2)
        cond4 = self.recursive_func(a - 1, b - 3)

        self.dp[a][b] = (cond1 + cond2 + cond3 + cond4) / 4
        return self.dp[a][b]

    def soupServings(self, n: int) -> float:
        # Edge cases
        if n > 4800:
            return 1

        n = int((n + 24) // 25)  # ceil division

        # create a dp 2D array, size = (n+1) * (n+1)
        self.dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.recursive_func(n, n)
