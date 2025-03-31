from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        cost_diff = []
        for i in range(n - 1):
            cost_diff.append(weights[i] + weights[i + 1])
        cost_diff.sort()
        max_score = sum(cost_diff[-(k-1):])
        min_score = sum(cost_diff[:k-1])
        return max_score - min_score
