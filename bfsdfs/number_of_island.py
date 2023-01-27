class Solution(object):
    def numIslands(self, grid):
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                # self.area.add((i, j))
                dfs(i-1, j); dfs(i+1, j); dfs(i, j-1); dfs(i, j+1)
return
        res = 0
        # areas = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    # self.area = set()
                    dfs(i, j)
                    # areas += [self.area]
        # print(areas)
return res
