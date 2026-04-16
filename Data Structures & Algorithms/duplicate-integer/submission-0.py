class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for n in nums:
            if n in myDict:
                return True
            else:
                myDict[n] = 1
            print(myDict)
        return False