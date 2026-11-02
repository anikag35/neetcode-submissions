from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # shortest path problem
        wordSet = set(wordList)
        queue = deque([beginWord])

        length = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft() 
                if word == endWord:
                    return length
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                for i in range(len(word)):
                    for j in range(26):
                        newWord = word[:i] + alphabet[j] + word[i+1:]
                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.remove(newWord)
            length += 1
        
        return 0