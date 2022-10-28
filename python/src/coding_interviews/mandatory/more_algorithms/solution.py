from collections import defaultdict, deque
from typing import DefaultDict, Deque, List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # {1: 3, 2: 2: 3: 0}
        # Course 1 has 2 prerequisites.
        # Course 2 has 1 prerequisites.
        # Course 3 has 0 prerequisites.
        degrees: DefaultDict[int, int] = defaultdict(int)

        # {1: {2, 3}, 2: {3}, 3: {}}
        # Course 1 is a prerequisite for courses 2 and 3.
        # Course 2 is a prerequisite for course 3.
        # Course 3 is a prerequisite for no courses.
        graph: DefaultDict[int, Set[int]] = defaultdict(set)

        # Initialize the degrees dict with default value of 0.
        for i in range(numCourses):
            degrees[i] = 0

        # We go through each prerequisite and add one degree to the reference course.
        # We also add to the set of degrees that course is a prerequisite for (directed graph).
        for pair in prerequisites:
            degrees[pair[0]] += 1
            graph[pair[1]].add(pair[0])

        # Queue starts with all courses that don't have a prerequisite.
        queue: Deque[int] = deque()
        for key, val in degrees.items():
            if val == 0:
                queue.append(key)

        stack: List[int] = []
        while queue:
            curr = queue.popleft()
            stack.append(curr)
            for child in graph[curr]:
                degrees[child] -= 1
                if degrees[child] == 0:
                    queue.append(child)

        if len(stack) != numCourses:
            return []
        else:
            return stack
