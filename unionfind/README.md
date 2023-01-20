# structure


```py
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


```

```py
class UnionFind:
    parent = []

    def dsu(n: int):
        for i in range(len(parent + 1)):
            parent[i] = i


    def find(x):
        if (parent[x] != x):
            parent[x] = find(parent[x])
        return parent[x]


    def union(x, y):
        parent[find(x)] = find(y)

```

weighted:

```py
class UnionFind:
    parent = []
    rank = []

    def dsu(n: int):
        for i in range(len(parent)):
            parent[i] = i
        rank = [1] * len(parent)

    def find(x):
        if (parent[x] != x):
            parent[x] = find(parent[x])
        return parent[x]


    def union(x, y):
        parent_x, parent_y =  find(x), find(y)
        if (parent_x == parent_y):
            return

        if (rank[parent_x] < rank[parent_y]):
            parent[parent_x] = parent_y
        elif (rank[parent_x] > rank[parent_y]):
            parent[parent_y] = parent_x
        else:
            # rank is equal between x, y, so we need to append and increase rank (one of them attach to another)
            parent[parent_x] = parent_y
            rank[parent_y] += 1

```
 or

```py
class DisJointSets():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]

    def find(self, u):
        while u != self._parents[u]:
            # path compression technique
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return False
```
