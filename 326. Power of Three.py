class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power_list = []
        tmp = 1
        while True:
            if tmp > (2**31 - 1):
                break
            power_list.append(tmp)
            tmp *= 3
        if n in power_list:
            return True
        return False