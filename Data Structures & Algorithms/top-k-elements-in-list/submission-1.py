class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for val in nums:
            if val in myDict:
                myDict[val] = myDict[val] + 1
            else:
                myDict[val] = 1
        #sorts by value in descending order
        sortedDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))
        dictList = list(sortedDict.keys())
        i = 0
        masterArr = []
        while (k > 0):
            masterArr.append(dictList[i])
            k -= 1
            i+=1
        return masterArr