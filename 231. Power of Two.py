class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power_list = []
        tmp = 1
        for i in range(32):
            power_list.append(tmp)
            tmp *= 2
        if n in power_list:
            return True
        return False