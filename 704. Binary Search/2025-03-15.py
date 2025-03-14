from typing import List

# This solution is not optimal, but it works.
# It is a simple linear search algorithm.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i == target:
                return count
            count += 1
        return -1