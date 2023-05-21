
Leetcode 694. Number of Distinct Islands (Python)


```py
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = {'l':[-1,  0], 'r':[ 1,  0], \
                      'u':[ 0,  1], 'd':[ 0, -1]}

        def dfs(i, j, grid, island):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            for k, v in directions.iteritems():
                island.append(k);
                dfs(i+v[0], j+v[1], grid, island)
            return True

        islands = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                island = []
                if dfs(i, j, grid, island):
                    islands.add("".join(island))
        return len(islands)
```

We want to build a bridge between blue and red lands at minimum cost. The cost of a bridge is proportional to its length.
Write a function to return the shortest distance between the two lands.
Please note that the bridge must be connected in 4-directions; up, right, down and left.



Example 1:
[input]
.RR...
R....B
R....B
RR....
[output]
3
Example 2:
[input]
.RB...
R....B
..B...
‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌R.....
[output]
0

```py
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = {'l':[-1,  0], 'r':[ 1,  0], \
                      'u':[ 0,  1], 'd':[ 0, -1]}

        def dfs(i, j, grid, island):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            for k, v in directions.iteritems():
                island.append(k);
                dfs(i+v[0], j+v[1], grid, island)
            return True

        islands = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                island = []
                if dfs(i, j, grid, island):
                    islands.add("".join(island))
        return len(islands)
```
