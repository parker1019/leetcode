from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = sum(nums)
        if sums < target:
            return 0

        s, l, ans = 0, 0, len(nums)
        for i, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[l]
                ans = min(ans, i-l+1)
                l += 1
        return ans