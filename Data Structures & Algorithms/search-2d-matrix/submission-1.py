class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first, let's find the right row
        lo = 0
        hi = len(matrix) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        #now lo = hi
        row = hi

        lo, hi = 0, len(matrix[row]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
