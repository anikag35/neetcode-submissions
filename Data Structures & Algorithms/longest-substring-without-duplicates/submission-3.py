class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        state = set()
        right = 0
        maxLen = 0
        for right in range(len(s)):
            while s[right] in state:
                state.remove(s[left])
                left+=1
            state.add(s[right])
            maxLen = max(maxLen, len(state))
        return maxLen

