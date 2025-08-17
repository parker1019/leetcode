# Only DP
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        # Start with 0, s.t. probability will be 1
        dp[0] = 1

        # Go through all point to get the probability
        for i in range(1, n + 1):
            # Go through [1, maxPts] to calculate the next point probability
            for j in range(1, maxPts + 1):
                # Filter none exist & stop condition
                if i - j >= 0 and i - j < k:
                    dp[i] += dp[i - j] / maxPts
        return sum(dp[k:])

# DP and Sliding Window
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k - 1 + maxPts <= n:
            return 1
        if n < k:
            return 0
        
        dp = [0] * (n + 1)
        # Start with 0, s.t. probability will be 1
        dp[0] = 1
        # Init slide window with 1 
        slide_window = 1
        # Go through all point to get the probability
        for i in range(1, n + 1):
            dp[i] = slide_window / maxPts
            if i < k:
                slide_window += dp[i]

            left = i - maxPts
            # Out of window
            if 0 <= left < k:
                slide_window -= dp[left]
        return sum(dp[k:])