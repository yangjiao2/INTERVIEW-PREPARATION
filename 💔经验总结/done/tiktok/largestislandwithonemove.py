class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq: return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp]+=self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        numRow, numCol, ans = len(grid), len(grid[0]), 1
        dsu, directions = DSU(numRow*numCol), [[1,0],[0,1],[-1,0],[0,-1]]
        
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        nextX, nextY = i+dx, j+dy
                        if nextX<0 or nextY<0 or nextX>=numRow or nextY>=numCol or grid[nextX][nextY] == 0: continue
                        dsu.union(i*numCol+j, nextX*numCol+nextY)
                        ans = max(ans, dsu.size[dsu.find(i*numCol+j)])
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 0:
                    neighborToSize = {}
                    for dx, dy in directions:
                        nextX, nextY = i+dx, j+dy
                        if nextX<0 or nextY<0 or nextX>=numRow or nextY>=numCol or grid[nextX][nextY] == 0: continue
                        p = dsu.find(nextX*numCol+nextY)
                        neighborToSize[p] = dsu.size[p]
                    ans = max(ans, sum(neighborToSize.values()) + 1)
        return ans