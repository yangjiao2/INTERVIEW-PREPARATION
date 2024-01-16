from collections import deque

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    # Queue to perform BFS
    queue = deque()
    queue.append([start])

    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph.getFriends(node)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path

            visited.add(node)

    return None  # No path exists

# Example usage:
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def getFriends(self, node):
        return self.graph.get(node, [])
