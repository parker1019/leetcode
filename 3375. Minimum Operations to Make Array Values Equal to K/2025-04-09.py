from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        min_num = min(num_set)
        if min_num < k:
            return -1
        elif min_num == k:
            return len(num_set) - 1
        else:
            return len(num_set)
