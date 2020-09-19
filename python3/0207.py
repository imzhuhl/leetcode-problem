'''
Author       : Zhu Honglin
Date         : 2020-09-19 21:08:39
LastEditTime : 2020-09-19 21:23:43
'''

from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """BFS + queue
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for item in prerequisites:
            graph[item[1]].append(item[0])
            indegree[item[0]] += 1
        
        s = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                s.append(i)

        cnt = 0
        while s:
            n = s.popleft()
            cnt += 1
            for v in graph[n]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    s.append(v)
                
        return cnt == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass
        