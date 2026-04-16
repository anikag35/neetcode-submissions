class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for val in nums:
            if val in myDict:
                myDict[val] = myDict[val] + 1
            else:
                myDict[val] = 1
        #sorts by value in descending order
        sortedDict = sorted(myDict, key=myDict.get, reverse=True)
        return sortedDict[:k]