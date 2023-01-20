# https://leetcode.com/problems/swim-in-rising-water/solutions/113770/c-python-priorityqueue/
# https://leetcode.com/problems/swim-in-rising-water/solutions/1284843/python-2-solutions-union-find-heap-explained/

## dsu
class DSU(object):
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:
    def swimInWater(self, grid):
        d, n = {}, len(grid)
        for i, j in product(range(n), range(n)):
            d[grid[i][j]] = (i, j)

        dsu = DSU(n)
        visited = [[0] * n for _ in range(n) ] # visited
        neigh_coor = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(n*n):
            x, y = d[i]
            grid[x][y] = 1
            for dx, dy in neigh_coor:
                if 0 <= x < n  and 0 <= y < n and visited[x + dx][y + dy] == 1:
                    nx, ny = x + dx, y + dy
                    dsu.union(nx * n + dy, x * n + y)

            if dsu.find(0) == dsu.find(n*n-1): return i



## heap

class Solution:
    def swimInWater(self, grid):
        N, heap, visited, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        neigh_coor = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(n*n):
            val, x, y = heapq.heappop(heap)
            res = max(res, val)

            if x == n-1 and y == n-1; return res

            for dx, dy in neigh_coor:
                if (x+dx, y+dy) not in visited and 0 <= x < n and 0 <= y <= n:
                    visited.add((x+dx, y+dy))
                    heapq.heappush(heap, (grid[x+dx][y+dy], x+dx, y+dy))
