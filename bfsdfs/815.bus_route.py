class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        stop_to_bus = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
        seen = set([source])
        q = deque([(source, 0)])
        if target == source: return 0
        while q:
            s, step = q.popleft()

            for curr_bus in stop_to_bus[s]:
                for destination in routes[curr_bus]:
                    # print (destination, target)
                    if destination == target: # check end condition FIRST
                        return step + 1
                    # elif destination != s:
                    elif destination not in seen:
                        q += (destination, step + 1),
                    
                routes[curr_bus] = []  # clean up PRUNE
        return -1


Time Complexity analysis:
We are traversing through each element exactly once.
Hence, time complexity = O(n).

Space Complexity Analysis:
There are 2^h number of nodes in the last level of a full Binary Tree (worst case) with height h.
Also, for a full Binary Tree, height of the tree = (log2n) nearly.
At max we will be storing one complete level at a time in our queue, and max number of elements (in the worst case) are present in the last level.
So, max size of queue = 2 ^ (log2n) = O(n) = Space Complexity.