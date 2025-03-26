from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total_num = []
        for part in grid:
            total_num += part

        total_num.sort()

        mid = total_num[len(total_num) // 2]

        op = 0

        for num in total_num:
            if abs(num - mid) % x != 0:
                return -1

            op += abs(num - mid) // x

        return op

