
```py
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in xrange(numCourses)] # DAG detection
        for x in xrange(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res

    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


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
        ```
