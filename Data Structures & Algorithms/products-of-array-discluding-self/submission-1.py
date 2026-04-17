import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        masterArr = []
        for i in range(len(nums)):
            newArr = nums[0:i] + nums[i+1:]
            masterArr.append(math.prod(newArr))
        return masterArr