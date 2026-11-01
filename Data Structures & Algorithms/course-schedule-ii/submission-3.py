from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        #courses w no prereqs
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        order = []
        while q:
            course = q.popleft()
            taken += 1
            order.append(course)
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        if taken != numCourses:
            return []
        return order