from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        high, width, ans = 0, 0, 0
        for x in nums:
            ans = max(ans, width*x)
            width = max(high - x, width)
            high = max(high, x)
        return ans