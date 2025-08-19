class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_dic = {}
        tmp = 0
        for num in nums:
            if num == 0:
                tmp += 1
                continue
            if tmp != 0:
                if tmp not in total_dic:
                    total_dic[tmp] = 1
                else:
                    total_dic[tmp] += 1
                tmp = 0
        if tmp != 0:
            if tmp not in total_dic:
                total_dic[tmp] = 1
            else:
                total_dic[tmp] += 1
        total = 0
        for k in total_dic:
            total += int(total_dic[k]*k*(k+1)/2)
        return total