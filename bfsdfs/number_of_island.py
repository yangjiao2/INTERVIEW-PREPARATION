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






class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n, res = len(grid), len(grid[0]), 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            grid[row][col] = "-1"
            
            for d in dirs:
                if 0 <= row + d[0] < m and 0 <= col + d[1] < n and grid[row + d[0]][col + d[1]] == '1':
                    dfs(row + d[0], col + d[1])

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1

        return res
            
        