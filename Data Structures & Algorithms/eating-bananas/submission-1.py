class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.can(mid, h, piles):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def can(self, k, h, piles):
        return sum(math.ceil(p / k) for p in piles) <= h