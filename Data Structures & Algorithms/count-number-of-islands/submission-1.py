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
      
        
            



'''
What goes on your stack? You’re pushing grid[0][0], which is the value '1'. Once you pop '1', can you find its neighbors? What do you need to store instead?
Who counts? Right now the counting happens inside the DFS, once per land cell. Should the count go up once per cell, or once per island? Which of the two jobs knows when a new island starts?
Where does the DFS start? It always starts at [0][0]. Shouldn’t it start wherever the scanner found new land?
What does visited need to survive? You create a new visited set inside dfs on every call. If the scanner later reaches a cell from an island you already painted, how would it know?
Neighbors: for a cell (r, c), what are its 4 neighbors, and which of them should you skip? Think about the grid’s edges and water.
'''