class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        curr = []
        lengths = []
        if nums == []:
            return 0
        curr.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] in curr:
                continue
            elif (nums[i] == nums[i-1] + 1):
                curr.append(nums[i])
            else:
                lengths.append(len(curr))
                curr = []
                curr.append(nums[i])
        lengths.append(len(curr))
        return max(lengths)
            