class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # connected components
        # if we find a new 1, another component, so run dfs
        number = 0
        visited = set()
        
        def dfs(i, j):
            stack = [(i, j)]
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while stack:
                ci, cj = stack.pop()
                for r, c in dirs:
                    ni, nj = ci + r, cj + c
                    if 0 <= ni < len(grid) and 0 <= nj <   len(grid[0]) and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        if grid[ni][nj] == "1":
                            stack.append((ni, nj))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    number += 1
                    visited.add((i, j))
                    dfs(i, j)

    
        return number
      
        
            



