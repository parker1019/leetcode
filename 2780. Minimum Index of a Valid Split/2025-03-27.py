from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counters = Counter(nums)
        dominant = 0
        for k, v in counters.items():
            if v > n//2:
                dominant = k
                break

        times = 0

        for i, num in enumerate(nums):
            if num == dominant:
                times += 1
            index = i+1
            if index // 2 < times and (n-index) // 2 < counters[dominant] - times:
                return i
        return -1