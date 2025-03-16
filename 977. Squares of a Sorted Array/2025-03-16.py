from typing import List

# Function: Returns the squares of a sorted integer list in non-decreasing order.
# Time Complexity: O(nlog(n)), due to the use of the built-in sorted() function.
# Space Complexity: O(n), as additional space is required to store the squared values and sorting results.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for num in nums:
            num = num**2
            new_nums.append(num)
        new_nums = sorted(new_nums)
        return new_nums