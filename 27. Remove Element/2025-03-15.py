from typing import List

# This solution is optimal.
# It is a simple linear search algorithm.
# Time complexity: O(n)
# Space complexity: O(1)

""""
The algorithm uses two pointers: i and k.
The algorithm iterates over the array.
If the element is not equal to the target, the element is copied to the k-th index.
The k-th index is incremented.
The algorithm returns the k-th index.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        return k
