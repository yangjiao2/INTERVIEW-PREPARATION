class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        g = defaultdict(list)
        for index, nodes in enumerate(graph):
            g[index] = nodes

        res = []
        n = len(graph) - 1
        def dfs(node, path, res):
            if node == n:
                res.append(path + [node])
                return
            for nei in g[node]:
                dfs(nei, path + [node], res)

        dfs(0, [], res)
        return res
