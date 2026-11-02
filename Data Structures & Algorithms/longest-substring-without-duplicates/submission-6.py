class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        letters = set()
       
        res = 0
        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            res = max(res, right - left + 1)
        return res


        