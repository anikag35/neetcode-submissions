class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['} 
        stack = []
        
        for char in s:
            #in -> if its a key
            if char in pairs:
                #if we find a closing char w no opening one alr processed
                #or if we find a closing char and the most recent char (now popped) isn't its pair
                if len(stack) == 0 or stack.pop() != pairs[char]:
                    return False
          #add opening char
            else:
                stack.append(char)
        return len(stack) == 0

    