class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for string in strs:
            if "".join(sorted(string)) in myDict:
                myDict["".join(sorted(string))].append(string)
            else:
                myDict["".join(sorted(string))] = [string]
        return list(myDict.values())