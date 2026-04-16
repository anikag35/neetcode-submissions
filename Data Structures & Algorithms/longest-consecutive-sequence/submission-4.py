class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for val in nums:
            if val - 1 not in nums:
                currNum = val
                currLen = 1
                while currNum + 1 in nums:
                    currNum += 1
                    currLen += 1
                longest = max(longest, currLen)
        return longest