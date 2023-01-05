
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Create a prerequisite dict. (containing courses (nodes) that need to be taken (visited)
		# before we can visit the key.
        preq = {i:set() for i in range(numCourses)}
        graph = [0] * numCourses
        res = []
        for i,j in prerequisites:
            preq[j].add(i)
            graph[i] += 1

        q = collections.deque([])
        for node in graph:
            if graph[node] == 0:
                q += node,

        while (len(q) != 0):
            node = q.popleft()
            res += node,
            for neighbor in preq[node]:
                graph[neighbor] -= 1

                if graph[neighbor] == 0:
                    q.append(neighbor)
        return res if len(res) == numCourses else []
