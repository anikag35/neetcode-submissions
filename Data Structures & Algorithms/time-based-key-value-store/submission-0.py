class TimeMap:

    def __init__(self):
        self.keyStore = {}
         

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        lo = 0
        hi = len(values) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return res

        
