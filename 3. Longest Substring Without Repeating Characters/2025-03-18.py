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
                    for key, value in list(char_dic.items()):
                        if value < left:
                            del char_dic[key]
            else:
                ans = max(ans, right-left+1)
            char_dic[s[right]] = right
        return ans
