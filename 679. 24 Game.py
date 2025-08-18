class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6
        
        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < eps

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    a, b = nums[i], nums[j]
                    cand = [a + b, a - b, b - a, a * b]
                    if abs(b) > eps:
                        cand.append(a / b)
                    if abs(a) > eps:
                        cand.append(b / a)
                    next_nums = nums[:]
                    next_nums.remove(a)
                    next_nums.remove(b)
                    for val in cand:
                        if dfs(next_nums + [val]):
                            return True
            return False
        return dfs([float(x) for x in cards])