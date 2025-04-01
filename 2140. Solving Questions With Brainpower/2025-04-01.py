class Solution:
    def mostPoints(self, questions: list) -> int:
        dp = [0]*(len(questions) + 1)

        """
        1. dp[i] = dp[i + questions[i][1] + 1] + questions[i][0]
        2. dp[i] = dp[i + 1]
        max(1, 2)
        """

        for i in range(len(questions) - 1, -1, -1):
            solve = questions[i][0]
            next_index = i + questions[i][1] + 1
            if next_index < len(questions):
                solve += dp[next_index]
            skip = dp[i + 1]
            dp[i] = max(solve, skip)
        return dp[0]