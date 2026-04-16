class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        maximum = 0
        while (first < last):
            area = abs(last - first) * min(heights[first], heights[last])
            maximum = max(maximum, area)
            if heights[first] < heights[last]:
                first += 1
            else:
                last -= 1
        return maximum
