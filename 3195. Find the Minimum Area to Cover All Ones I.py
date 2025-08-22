class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left = 1000
        right = -1
        up = 1000
        down = -1
        tmp = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    if tmp == 0:
                        tmp = 1
                    if up > i:
                        up = i
                    if down < i:
                        down = i
                    if right < j:
                        right = j
                    if left > j:
                        left = j
        if tmp == 0:
            return 0
        return (right - left + 1)*(down - up + 1) 
