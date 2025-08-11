class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        exps = []
        i = 0
        while n:
            if n & 1:
                exps.append(i)
            n >>= 1
            i += 1
        
        ps = [0]
        for e in exps:
            ps.append(ps[-1] + e)
        
        ans = []
        for start, end in queries:
            s = ps[end + 1] - ps[start]
            ans.append(pow(2, s, MOD))
        return ans
