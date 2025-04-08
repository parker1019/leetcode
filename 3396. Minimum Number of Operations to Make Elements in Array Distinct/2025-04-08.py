from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        existed_nums = []
        l = len(nums)
        stop = -1
        for i in range(l-1, -1, -1):
            if nums[i] not in existed_nums:
                existed_nums.append(nums[i])
            else:
                stop = i
                break
        if stop == -1:
            return 0
        ans = (stop+1)//3
        if (stop+1)%3==0:
            return ans
        else:
            return ans+1
