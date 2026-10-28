class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # returning disjoint intervals
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: (x[0], x[1]))
        tracking = [intervals[0]]

        for i in range(1, len(intervals)):
            # [[1,3], [2,6], [8,10]]
            left, right = tracking[-1]
            currLeft, currRight = intervals[i]
            if right >= currLeft: # overlap
                if currRight > right:
                    tracking[-1] = [left, currRight]
            else:
                tracking.append([currLeft, currRight])

        return tracking


