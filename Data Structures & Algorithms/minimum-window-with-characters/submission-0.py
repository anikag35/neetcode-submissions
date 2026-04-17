from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        need = Counter(t)
        required = len(need)         
        window = defaultdict(int)
        have = 0                     
        
        left = 0
        # (length, left_idx, right_idx)
        best = (float('inf'), 0, 0) 
        
        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if (right - left + 1) < best[0]:
                    best = (right - left + 1, left, right)
                
                
                window[s[left]] -= 1
                
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        
        length, l, r = best
        return s[l:r+1] if length != float('inf') else ""