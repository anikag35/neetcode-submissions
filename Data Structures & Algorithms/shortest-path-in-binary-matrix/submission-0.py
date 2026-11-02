class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        n = len(grid)
        length = 1
        if not grid:
            return -1

        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        queue.append((0, 0))
       
        visited = set()
        visited.add((0, 0))
        

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n-1 and c == n-1:
                    return length
                for dl, dr in dirs:
                    nr, nc = r + dl, c + dr
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 0 and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            length += 1
        
        return -1
