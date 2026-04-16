class Solution:

    def encode(self, strs: List[str]) -> str:
        masterStr = ""
        for string in strs:
            masterStr = masterStr + str(len(string)) + "^" + string
        return masterStr
    def decode(self, s: str) -> List[str]:
        newStr = []
        i = 0
        while (i < len(s)):
            n = ""
            while (s[i] != "^"):
                n += s[i]
                i+=1
            n = int(n)
            i+=1
            string = s[i:i+n]
            i += n
            newStr.append(string)
        return newStr