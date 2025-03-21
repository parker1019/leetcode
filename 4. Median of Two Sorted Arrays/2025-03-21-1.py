from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always make sure that nums2 is the smaller list.
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # Binary search
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, n, (m+n+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            if i < n and nums2[i] < nums1[j-1]:
                imin = i + 1
            elif i > 0 and nums1[j] < nums2[i-1]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums1[j-1]
                elif j == 0: max_of_left = nums2[i-1]
                else: max_of_left = max(nums1[j-1], nums2[i-1])
                
                if (m+n) % 2 == 1:
                    return max_of_left
                
                if i == n: min_of_right = nums1[j]
                elif j == m: min_of_right = nums2[i]
                else: min_of_right = min(nums1[j], nums2[i])
                
                return (max_of_left + min_of_right) / 2.0
