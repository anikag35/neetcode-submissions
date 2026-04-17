class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            window_size = right - left + 1
            changes_needed = window_size - max(count.values())
            
            while changes_needed > k:
                count[s[left]] -= 1
                left += 1
                window_size = right - left + 1
                changes_needed = window_size - max(count.values())
            
            max_len = max(max_len, right - left + 1)

        return max_len


            