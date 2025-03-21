from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans_list = sorted(nums1+nums2)
        middle = len(ans_list)//2
        if len(ans_list) == 1:
            return float(ans_list[0])
        if len(ans_list)%2 == 0:
            mean = (ans_list[middle]+ans_list[middle-1])/2.0
        else:
            mean = ans_list[middle]
        return float(mean)