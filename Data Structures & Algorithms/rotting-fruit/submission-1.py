from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        queue = deque()
        fresh = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # add all source vertices to the queue
        # track how many fresh fruits we have
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1   
        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            minutes += 1
        if fresh > 0:
            return -1
        return minutes
        