from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        #courses w no prereqs
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        return taken == numCourses        