from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half_total = sum(nums)/2
        if half_total != int(half_total):
            return False

        half_total = int(half_total)
        dp = [False] * (half_total + 1)
        dp[0] = True
        for num in nums:
            for j in range(half_total, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[half_total]