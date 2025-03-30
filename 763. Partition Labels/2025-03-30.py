from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        limit = {}
        for i, word in enumerate(s):
            if word not in limit:
                limit[word] = [i, -1]
            else:
                limit[word][1] = max(limit[word][1], i)
        check = -1
        last = -1
        ans = []
        for i, word in enumerate(s):
            if limit[word][1] == -1 and check == -1:
                ans.append(1)
                last = i

            if limit[word][1]>check:
                check = limit[word][1]
            elif i==check:
                if last == -1:
                    ans.append(check+1)
                    last = check
                    check = -1
                else:
                    ans.append(check-last)
                    last = check
                    check = -1
        return ans