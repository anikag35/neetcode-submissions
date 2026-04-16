class Solution:
    def isPalindrome(self, s: str) -> bool:
        slow = 0
        fast = len(s) - 1
        while slow < fast:
            if not s[slow].isalnum():
                slow += 1
                continue
            if not s[fast].isalnum():
                fast -= 1
                continue
            if not s[slow].lower() == s[fast].lower():
                return False
            slow += 1
            fast -= 1
        return True