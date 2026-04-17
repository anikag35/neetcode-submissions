class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxArr = []
        left = 0
        window = nums[:k]
        maxArr.append(max(window))
        for right in range(k, len(nums)):
            left += 1
            window = nums[left:right+1]
            maxArr.append(max(window))
        return maxArr