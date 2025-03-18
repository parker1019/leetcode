class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dic = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in char_dic:
                dup_position = char_dic.get(s[right])
                if left <= dup_position:
                    left = dup_position + 1
                else:
                    ans = max(ans, right-left+1)
            else:
                ans = max(ans, right-left+1)
            char_dic[s[right]] = right
        return ans