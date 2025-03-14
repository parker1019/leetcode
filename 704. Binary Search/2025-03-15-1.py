from typing import List

# This solution is optimal.
# It is a binary search algorithm.
# Time complexity: O(log n)
# Space complexity: O(1)

"""
The nums is a sorted array.
The algorithm uses two pointers: left and right.
The algorithm calculates the middle index of the array.
If the middle element is greater than the target, the right pointer is moved to the left of the middle index.
If the middle element is less than the target, the left pointer is moved to the right of the middle index.
If the middle element is equal to the target, the middle index is returned.
If the target is not found, -1 is returned.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = left + (right-left) // 2
            if nums[middle] > target:
                right = middle -1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1