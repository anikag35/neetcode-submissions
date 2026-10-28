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


''' 
tracking = [[1,3]]
i=1: left,right = 1,3   curr = 2,6
     3 > 2 → overlap → right = 6
     tracking is still [[1,3]]   ✗

The main bug: left, right = tracking[-1] copies the numbers into new variables. Changing right doesn’t touch the list inside tracking. You need to write back into the last interval itself. How would you set the end of tracking[-1] directly?

Three smaller things:

Touching intervals: with [1,4] and [4,5], is 4 > 4 true? Should they merge? Adjust the comparison.
if left > currLeft can never be true, because you sorted by start. You can delete it.
No return at the end, and empty input should give [].


'''