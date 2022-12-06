# structure

```
class UnionFind:
    parent = []

    def dsu(n: int):
        for i in range(len(parent + 1)):
            parent[i] = i

        
    def find(x):
        if (parent[x] != x): 
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y)
        parent[find(x)] = find(y)

```
