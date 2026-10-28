from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        res = []
        queue = deque()

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            i = queue.popleft()
            res.append(i)
            for val in graph[i]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
        
        return len(res) == numCourses
