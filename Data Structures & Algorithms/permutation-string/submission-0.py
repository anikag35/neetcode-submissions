class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        need = Counter(s1)
        
        #get the first valid window
        curr = Counter(s2[:windowSize])
         
        if need == curr:
            return True

        for right in range(windowSize, len(s2)):
            curr[s2[right]] += 1
            leftChar = s2[right - windowSize]
            curr[leftChar] -= 1
            if (curr[leftChar] == 0):
                del curr[leftChar]
            if curr == need:
                return True
        return False