# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        lst = [i for i in range(1, n+1)]
        def dfs(idx, path, res):
            if (len(path) == k):
                res.append(path)
                return

            for i in range(idx+1, n+1):
                dfs(i, path + [i], res)

        dfs(0, [], res)
        return res
