import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # follow up = use O(k) space
        # w/ min heap, you have to push all n points and then pop k times
        max_heap = []
        for x, y in points:
            dist = -1 * ((x*x) + (y*y))
            heapq.heappush(max_heap, (dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [[x, y] for _, x, y in max_heap]