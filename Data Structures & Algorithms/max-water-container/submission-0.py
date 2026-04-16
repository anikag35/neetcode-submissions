class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        maximum = 0
        for _ in range(len(heights)):
            while (first < last):
                area = abs(last - first) * min(heights[first], heights[last])
                maximum = max(maximum, area)
                last-=1
            first+=1
            last = len(heights)-1
        return maximum
