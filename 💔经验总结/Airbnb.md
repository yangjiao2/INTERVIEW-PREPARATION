https://www.youtube.com/playlist?list=PLbhaS_83B97tFPucgkG5gL0OtMzD37lVE


而无益 三思瑶
时间复杂度


伊耳三吴

酒店预定


外星人字典


你为什么选择我们公司？
除了专业，还有什么可以激发你强烈兴趣？



warm up: 125
follow up: 336


题目1 是： 376
题目2是： 890



依依路路，多加了一个callback 方法，要求implement一个interface。



https://www.1point3acres.com/bbs/thread-954110-1-1.html


wallet design: https://newsletter.pragmaticengineer.com/p/designing-a-payment-system

https://www.infoq.com/news/2021/02/paypal-next-gen-data-movement/


warm up: 125
follow up: 336
依依路路
题目1 是： 376
题目2是： 890

伊耳三吴

外星人字典
倒水

boggle game

琪琪伞（board 3*3)

义务武器， 但是有环有环有环！！

design KV store

alien dictionary


queue with limited size



伊尔伞舞 饵遥而


https://leetcode.com/problems/fraction-to-recurring-decimal/




class DataStore {
    constructor() {
        this.data = new Map();
        this.change = new Map();
        this.dataEvent = new Map();
    }

    add (name, val) {
        if (this.change.has(name)) {
            if (val != this.data.get(name)) {
                // change happens
                this.change.get(name).call(this, this.data.get(name), val, name);
            }
        }
        if (this.dataEvent.has(name)) {
            this.dataEvent.get(name).call(this, this.data.get(name), val, name);
        }

        this.data.set(name, val);
    }

    has(name) {
        if (this.data.has(name)) {
            return true;
        }
        return false;
    }

    on (event, callbackFn) {
        const p = event.indexOf(':');
        if (p != -1) {
            if (event.substring(0, p) == 'change') {
                this.change.set(event.substring(p+1), callbackFn);
            }
        } else {
            this.dataEvent.set(event, callbackFn);
        }
    }
}

//  test
const ds = new DataStore();
console.log(`ds.add('name', 'Joe')`);
ds.add('name', 'Joe');
console.log(`ds.has("name") = ${ds.has("name")}`);

console.log(`ds.add('age', 30)`);
ds.add('age', 30);
console.log(`ds.has("age") = ${ds.has("age")}`);

console.log(`Sub change:name event`);
ds.on('change:name', (oldVal, newVal, key) => {
    console.log(`The ${key} changes from ${oldVal} to ${newVal}`);
})

console.log(`ds.add('name', 'Tom')`);
ds.add('name', 'Tom');


console.log(`Sub name event`);
ds.on('name', (oldVal, newVal, key) => {
    console.log(`Set ${key} to ${newVal}. The old value is ${oldVal}`);
})

console.log(`ds.add('name', 'Nick')`);
ds.add('name', 'Nick');




https://leetcode.com/problems/flatten-nested-list-iterator/
```py

251. Flatten 2D Vector.py

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i1 = 0 # outer level index
        self.i2 = 0 # inner level index

        self._moveToValid()

    def _moveToValid(self):
        """
        move i1 and i2 to a valid position, so that self.vec2d[self.i1][self.i2] is valid
        """
        while self.i1 < len(self.vec2d) and self.i2 >= len(self.vec2d[self.i1]):
            self.i1 += 1
            self.i2 = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.i1][self.i2]
        self.i2 += 1
        self._moveToValid()

        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.vec2d)
```


alien dictionary:
建立入度字典 (word[i-1], word[i])
topSortDFS

```py

class Solution2(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            if (len(words[i-1]) > len(words[i]) and
                    words[i-1][:len(words[i])] == words[i]):
                return ""
            self.findEdges(words[i - 1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""

        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break

    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False

```

pour water: 向左/右找最小， 遇到次高点stop, "fill water"

```java

// Time: O(VN)
// Space: O(1)
class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int V, int K) {
        while (V--) {
            int leftMin = K;
            for (int i = K - 1; i >= 0; --i) {
                if (heights[i] < heights[leftMin]) leftMin = i;
                if (heights[i] > heights[leftMin]) break;
            }
            if (leftMin != K) {
                heights[leftMin]++;
                continue;
            }
            int rightMin = K;
            for (int i = K + 1; i < heights.size(); ++i) {
                if (heights[i] < heights[rightMin]) rightMin = i;
                if (heights[i] > heights[rightMin]) break;
            }
            if (rightMin != K) {
                heights[rightMin]++;
                continue;
            }
            heights[K]++;
        }
        return heights;
    }
};

```



# airbnb

[https://www.1point3acres.com/bbs/thread-220456-1-1.html](https://www.1point3acres.com/bbs/thread-220456-1-1.html)

****251. Flatten 2D Vector****

```python
class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i1 = 0 # outer level index
        self.i2 = 0 # inner level index

        self._moveToValid()

    def _moveToValid(self):
        """
        move i1 and i2 to a valid position, so that self.vec2d[self.i1][self.i2] is valid
        """
        while self.i1 < len(self.vec2d) and self.i2 >= len(self.vec2d[self.i1]):
            self.i1 += 1
            self.i2 = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.i1][self.i2]
        self.i2 += 1
        self._moveToValid()

        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.vec2d)
```

**341. Flatten Nested List Iterator**

last item store [list, index]

if is a nested list: index + 1, add [list, 0] to tail

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = **[[nestedList, 0]]**

    def next(self) -> int:
        self.hasNext()
        lst, index = self.nestedList[-1]
        self.nestedList[-1][1] += 1
        return lst[index].getInteger()

    def hasNext(self) -> bool:
        nestedList = self.nestedList
        while nestedList:
            lst, index = self.nestedList[-1]

            if index == len(lst):
                nestedList.pop()
            else:
                cur = lst[index]
                **if cur.isInteger():
                    return True
                nestedList[-1][1] += 1
                nestedList.append([cur.getList(), 0])**

        return False
```

strongly connected component



```python
def strongly_connected_components_iterative(vertices, edges):
    """
    This is a non-recursive version of strongly_connected_components_path.
    See the docstring of that function for more details.
    Examples
    --------
    Example from Gabow's paper [1]_.
    >>> vertices = [1, 2, 3, 4, 5, 6]
    >>> edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
    >>> for scc in strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([3])
    set([2, 4, 5, 6])
    set([1])
    Example from Tarjan's paper [2]_.
    >>> vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> edges = {1: [2], 2: [3, 8], 3: [4, 7], 4: [5],
    ...          5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]}
    >>> for scc in  strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([6])
    set([3, 4, 5, 7])
    set([8, 1, 2])
    """
    identified = set()
    stack = []
    index = {}
    boundaries = []

    for v in vertices:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    # We reverse to keep the search order identical to that of
                    # the recursive code;  the reversal is not necessary for
                    # correctness, and can be omitted.
                    to_do.extend(
                        reversed([('VISITEDGE', w) for w in edges[v]]))
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    # operation_type == 'POSTVISIT'
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        yield scc
```

**Max Area of Island**

```python
def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
```

W**ord Search ii with trie**

建trie, recursive loop using trie.leaves[board[i][j]]

backtrack:

        visited[i][j] = True
        self.findWordsRecu(board, next_node, **cur + 1**, i + 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i - 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i, j + 1, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i, j - 1, visited, cur_word, result)
        visited[i][j] = False

```python
# Time:  O(m * n * 4 * 3^(h - 1)) ~= O(m * n * 3^h), h is the height of trie
# Space: O(t), t is the number of nodes in trie

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_complete = False
        self.leaves = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_complete = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        result = {}
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.findWordsRecu(board, trie, **0, # cur**
										 i, j, visited, [], result)

        return result.keys()

    def findWordsRecu(self, board, trie, cur, i, j, visited, cur_word, result):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return

        if board[i][j] not in trie.leaves:
            return

        cur_word.append(board[i][j])
        next_node = **trie.leaves[board[i][j]]**
        if next_node.is_complete:
            result["".join(cur_word)] = True

        visited[i][j] = True
        self.findWordsRecu(board, next_node, **cur + 1**, i + 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i - 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i, j + 1, visited, cur_word, result)
        self.findWordsRecu(board, next_node, **cur + 1**, i, j - 1, visited, cur_word, result)
        visited[i][j] = False
        cur_word.pop()
```

alien dictionary

```python
alien dictionary:
建立入度字典 (word[i-1], word[i])
topSortDFS

```py

class Solution2(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            **if (len(words[i-1]) > len(words[i]) and
                    words[i-1][:len(words[i])] == words[i]):
                return ""**
            self.findEdges(words[i - 1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""

        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break

    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False

```

Alien Dictionary

```python
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Construct Graph
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos+1]))):
                pre, next = words[pos][i], words[pos+1][i]
                if pre != next:
                	in_degree[next] += 1
                    neighbors[pre].append(next)
                    break

        # Topological Sort
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            for _ in range(len(heap)):
                ch = heappop(heap)
                order.append(ch)
                for child in neighbors[ch]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        heappush(heap, child)

        # order is invalid
        if len(order) != len(in_degree):
            return ""
        return ''.join(order)
```

Pour water

```python
pour water: 向左/右找最小， 遇到次高点stop, "fill water"

```java

// Time: O(VN)
// Space: O(1)
class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int V, int K) {
        while (V--) {
            int leftMin = K;
            for (int i = K - 1; i >= 0; --i) {
                if (heights[i] < heights[leftMin]) leftMin = i;
                if (heights[i] > heights[leftMin]) break;
            }
            if (leftMin != K) {
                heights[leftMin]++;
                continue;
            }
            int rightMin = K;
            for (int i = K + 1; i < heights.size(); ++i) {
                if (heights[i] < heights[rightMin]) rightMin = i;
                if (heights[i] > heights[rightMin]) break;
            }
            if (rightMin != K) {
                heights[rightMin]++;
                continue;
            }
            heights[K]++;
        }
        return heights;
    }
};

```
```

Palindrone pairs

Case1: If s1 is a blank string, then for any string that is palindrome s2, s1+s2 and s2+s1 are palindrome.

Case 2: If s2 is the reversing string of s1, then s1+s2 and s2+s1 are palindrome.

Case 3: If s1[0:cut] is palindrome and there exists s2 is the reversing string of s1[cut+1:] , then s2+s1 is palindrome.

Case 4: Similiar to case3. If s1[cut+1: ] is palindrome and there exists s2 is the reversing string of s1[0:cut] , then s1+s2 is palindrome.

```python
    def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_pals = []
    for word, k in words.iteritems():
        n = len(word)
        for j in range(n+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    valid_pals.append([words[back],  k])
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    valid_pals.append([k, words[back]])
    return valid_pals
```

787 Cheapest Flights Within K Stops

![Untitled](airbnb%20b8f10ce0798348ee9e4977ad923576b3/Untitled.png)

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

```python
O(V^2 ⋅log V)
**def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        pq,graph=[(0, src, 0)],collections.defaultdict(dict)**
        for u,v,w in flights:
            graph[u][v]=w
        **while pq:
            total, src, stops = heapq.heappop(pq)
            if src == dst: return total
            if stops > K: continue
            for dest, cost in graph[src].items():
                heapq.heappush(pq,(total+cost, dest, stops+1))**
        return -1

def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1
```

**1557. Minimum Number of Vertices to Reach All Nodes**

return the nodes with no in-degres.

```python
def findSmallestSetOfVertices(self, n, edges):
        return list(set(range(n)) - set(j for i, j in edges))
```

751 IP to CIDR

num & -num

```python
class Solution {
    public List<String> ipToCIDR(String ip, int n) {
        List<String> rst = new ArrayList<>();

        String[] ips = ip.split("\\.");
        long num = 0;
        for (int i = 0; i < ips.length; i++) {
            num = num * 256 + Integer.parseInt(ips[i]);
        }

        while (n > 0) {
            long step = num & -num;

            while (step > n) step /= 2;
            rst.add(toIpString(num, step));
            num += step;
            n -= step;
        }

        return rst;
    }

    private String toIpString(long num, long step) {
        int[] blocks = new int[4];

        blocks[0] = (int) (num & 255);
        num >>= 8;
        blocks[1] = (int) (num & 255);
        num >>= 8;
        blocks[2] = (int) (num & 255);
        num >>= 8;
        blocks[3] = (int) (num & 255);
        num >>= 8;

        int count = 0;
        while (step > 0) {
            count++;
            step /= 2;
        }

        return blocks[3] + "." + blocks[2] + "." + blocks[1] + "." + blocks[0] + "/" + (33 - count);
    }
}
```

773 sliding puzzle

BFS with state

```python
class Solution(object):
    def slidingPuzzle(self, board):
        """
		"""
        moves = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        state = "".join(str(c) for c in board[0] + board[1])
        start = state.index('0')
        visited = set()

        queue = collections.deque([(start, state, 0)])
        **while queue:**
            cur, state, steps = queue.popleft()
            if state == '123450':
                return steps
            elif state in visited:
                continue
            else:
                visited.add(state)
                for nxt in moves[cur]:
                    tmp = list(state)
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = ''.join(tmp)
                    queue.append((nxt, **tmp**, steps + 1))
        return -1
```

39 Combination sum

```python
class Solution:

    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
```

76 **Minimum Window Substring**

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Keep t_counter of char counts in t

        We make a sliding window across s, tracking the char counts in s_counter
        We keep track of matches, the number of chars with matching counts in s_counter and t_counter
        Increment or decrement matches based on how the sliding window changes
        When matches == len(t_counter.keys()), we have a valid window. Update the answer accordingly

        How we slide the window:
        Extend when matches < chars, because we can only get a valid window by adding more.
        Contract when matches == chars, because we could possibly do better than the current window.

        How we update matches:
        This only applies if t_counter[x] > 0.
        If s_counter[x] is increased to match t_counter[x], matches += 1
        If s_counter[x] is increased to be more than t_counter[x], do nothing
        If s_counter[x] is decreased to be t_counter[x] - 1, matches -= 1
        If s_counter[x] is decreased to be less than t_counter[x] - 1, do nothing

        Analysis:
        O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
        O(s + t) space: O(t) space for t_counter and O(s) space for s_counter
        '''

        if not s or not t or len(s) < len(t):
            return ''

        t_counter = Counter(t)
        chars = len(t_counter.keys())

        s_counter = Counter()
        matches = 0

        answer = ''

        i = 0
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase

        while i < len(s):

            # extend
            if matches < chars:

                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer

                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1

            # update answer
            if matches == chars or (j - i + 1) < len(answer):
                answer = s[i:j+1]


        return answer
```

```
def mergeKLists_heapq(self, lists):
	h = []
	head = tail = ListNode(0)
	for i in range(len(lists)):
		heapq.heappush(h, (lists[i].val, i, lists[i]))

	while h:
		node = heapq.heappop(h)
		node = node[2]
		tail.next = node
		tail = tail.next
		if node.next:
			i+=1
			heapq.heappush(h, (node.next.val, i, node.next))

	return head.next
```

Convert Sorted Array to Binary Search Tree

```
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )

Time Complexity: O(n log n)
Space Complexity: O(n)
```

Reverse Bits

1. `out = (out << 1)^(n & 1)` adds last bit of `n` to `out`
2. `n >>= 1` removes last bit from `n`.

```
class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
```

**Word Search II**

build trie + dfs

```python
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
```

```python
def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False
```

327 [https://leetcode.com/problems/coin-change/](https://leetcode.com/problems/coin-change/) *fewest number of coins*

```python
def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for remaining in range(coin, amount + 1):
                dp[remaining] = min(dp[remaining - coin] + 1, dp[remaining])
        return dp[amount] if dp[amount] != math.inf else -1
```

**Coin Change II** combination of coins

```python
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for remaining in range(1, amount + 1):
               if remaining >= coin:
                   dp[remaining] += dp[remaining - coin]
        return dp[amount]
```

**Cheapest Flights Within K Stops (Dijkstra's)**

```python
 def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1
```

**815. Bus Routes (BFS with modified item in format (stop, counter) and append latest at end of seen set)**

`routes = [[1,2,7],[3,6,7]], source = 1, target = 6`

```python
def numBusesToDestination(self, routes, S, T):
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1
```

**42. Trapping Rain Water**

![Untitled](airbnb%20b8f10ce0798348ee9e4977ad923576b3/Untitled%201.png)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res, stack = 0, []
        for i, n in enumerate(height):
            while stack and stack[-1] < n:
                prev = stack.pop()
                height = height[i] - height[prev]
                width = i - stack[-1] - 1
                res += height * width
            stack.append(i)
        return res
```

**Word Search II** [https://leetcode.com/problems/word-search-ii/solutions/59790/python-dfs-solution-directly-use-trie-implemented/?orderBy=most_votes](https://leetcode.com/problems/word-search-ii/solutions/59790/python-dfs-solution-directly-use-trie-implemented/?orderBy=most_votes)

```python
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
```

**Jump Game II**

**next_right_range = max(i + nums[i] for i in range(l, r + 1))**

[https://leetcode.com/problems/jump-game-ii/solutions/170518/8-lines-in-python-easiest-solution/?orderBy=most_votes](https://leetcode.com/problems/jump-game-ii/solutions/170518/8-lines-in-python-easiest-solution/?orderBy=most_votes)

```python
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
```

**Accounts Merge**

```python
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    # 196 ms, 82.09%.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                **if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i**

        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            **ans[uf.find(owner)].append(email)**

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
```

```python
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    # 196 ms, 82.09%.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
```

**Sliding Window Maximum**

```python
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
            while d and nums[d[-1]] < n:
                d.pop()
                print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            print("\t Added i to d")
            if d[0] == i - k:
                d.popleft()
                print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i>=k-1:
                out.append(nums[d[0]])
        return out
```

1. Design file system

每个node: value 是文件内容

```python
class TrieNode:
  def __init__(self, value: int = 0):
    self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
    **self.value = value**

class FileSystem:
  def __init__(self):
    self.root = TrieNode()

  def createPath(self, path: str, value: int) -> bool:
    node: TrieNode = self.root
    subpaths = path.split('/')

    for i in range(1, len(subpaths) - 1):
      **if subpaths[i] not in node.children:**
        return False
      node = node.children[subpaths[i]]

    if subpaths[-1] in node.children:
      return False
    node.children[subpaths[-1]] = TrieNode(value)
    return True

  def get(self, path: str) -> int:
    node: TrieNode = self.root

    for subpath in path.split('/')[1:]:
      if subpath not in node.children:
        return -1
      node = node.children[subpath]

    return node.value

# add file watcher

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "D:/Test/bitstamp/btcEur/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:  #
						print ("event triggered on path - %s" % event.src_path)
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()

LoggingEventHandler class itslef is a subclass of watchdog.events.FileSystemEventHandler:
on_created, on_deleted, on_modified, on_moved

class LoggingHandler(LoggingEventHandler):
    def on_modified(self, event):
        print("Doh")

class Handler(watchdog.events.LoggingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now


if __name__ == "__main__":
    src_path = r"C:\Users\GeeksforGeeks\PycharmProjects\requests hotel"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

Basic Calculator

sign 继承前一个（default +)

+ -stack 写入 v, -v

 * / stack pop 出

( recursive and update iterator

) return sum(), iterator

```python
class Solution:
    def calculate(self, s):
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
```

**Jump game II**: next right jump = max from (iter_step + nums[iter_step])

```python
def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            **nxt = max(i + nums[i] for i in range(l, r + 1))**
            l, r = r, nxt
        return times
```

**Text Justification**

forward checking and reset to original in checks

default addition is applied in each for loop

```python
def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                **cur[i%(len(cur)-1 or 1)] += ' '**
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]

```

**44. Wildcard Matching**

- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

```python
class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    **dp[i][j] = dp[i-1][j-1]  // previous character**
                elif p[j-1] == '*':
                    **dp[i][j] = dp[i-1][j] or dp[i][j-1] // match nothing or everything //**
        return dp[-1][-1]
```

**Pour water**

```python
class Solution {
    public int[] pourWater(int[] heights, int V, int K) {
        for(int i = 0; i < V; i++) {
            int cur = K;
            // Move left
            while(cur > 0 && heights[cur] >= heights[cur - 1]) {
                cur--;
            }
            // Move right
            while(cur < heights.length - 1 && heights[cur] >= heights[cur + 1]) {
                cur++;
            }
            // Move left to K
            while(cur > K && heights[cur] >= heights[cur - 1]) {
                cur--;
            }
            heights[cur]++;
        }

        return heights;
    }
}
```

253. Meeting Rooms [II](http://ii.py/)

```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappush, heappop

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        SI = sorted(intervals, key=lambda it: (it.start, it.end))  # sorted intervals

        ret = 0
        heap = []  # contains end times

        for it in SI:
            start, end = it.start, it.end

            while heap and heap[0] <= start:
                heappop(heap)

            heappush(heap, end)

            ret = max(ret, len(heap))

        return ret
```

sliding puzzle 穷举bfs

每次check “while dq” 时 step += 1

记录状态：(chars, row * width + c)

```python
def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, **s.index('0')**))
        steps, height, width = 0, len(board), len(board[0])
        while dq:
            **for _ in range(len(dq)):**
                t, i= dq.popleft()
                if t == '123450':
                    return steps
                **x, y = i // width, i % width**
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = ch[r * width + c], '0' # swap '0' and its neighbor.
                        s = ''.join(ch)
                        **if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))**
            **steps += 1**
        return -1
```

652. Find Duplicate Subtrees

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.counter = collections.Counter()

        self.results = []

        self.helper(root)

        return self.results

    def helper(self, root):
        if not root:
            return '#'

        serial = "{}, {}, {}".format(root.val, self.helper(root.left), self.helper(root.right))

        self.counter[serial] += 1

        if self.counter[serial] == 2:
            self.results.append(root)

        return serial
```

**341. Flatten Nested List Iterator**

嵌套 list， 把正在loop 的和它的index，放入最后

[real_list, [looping_list, index]]

```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = **[[nestedList, 0]]**

    def next(self) -> int:
        self.hasNext()
        **lst, index = self.nestedList[-1]
        self.nestedList[-1][1] += 1**
        return lst[index].getInteger()

    def hasNext(self) -> bool:
        nestedList = self.nestedList
        while nestedList:
            lst, index = self.nestedList[-1]

            if **index == len(lst):**
                **nestedList.pop()**
            else:
                cur = lst[index]
                if cur.isInteger():
                    return True
                **nestedList[-1][1] += 1
                nestedList.append([cur.getList(), 0])**

        return False
```

**Find and Replace Pattern**

{char: unique index }

```python
def findAndReplacePattern(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        Fp = F(p)
        return [w for w in words if F(w) == Fp]
```

**Wiggle Subsequence**

The question can now reduced to find number of times array changes pattern.

=

**COUNT THE NUMBER OF PEAKS AND VALLEY POINTS.**

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        f = 1
        d = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                **f = d+1**
            elif nums[i] < nums[i-1]:
                **d = f+1**
        res = max(f, d)
        return res
```

**1557. Minimum Number of Vertices to Reach All Nodes**

无环：查indegree = 0  ⇒ difference between end node with all nodes

有环：uf

```python
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        # Just return the nodes with no in-degres.
        print (range(n))
        result =  list(set(range(n)) -  (set (j for i, j in edges)))

        # with cycle

        self.parent = [i for i in range(n)]

        def find(i):
            p_i = self.parent[i]
            if p_i != i:
                self.parent[i] = find(p_i)
            return i

        def union(a, b):
            p_a, p_b = self.parent[a], self.parent[b]
            self.parent[p_b] = p_a

        visited = set()
        for s, e in edges:
            if e not in visited:
                union(s, e)
            visited.add(e)
        print (self.parent)
        res = { node for _, node in enumerate(self.parent) if node == self.parent[node]}

        return res

print(Solution().findSmallestSetOfVertices(3, [[0,1],[1,2],[2,0]]))
```

[](https://goodtecher.com/tag/airbnb-interview-question/page/4/)

1. Given: A string strTask: Find a way to convert it into a palindrome by inserting characters in front of it and the shortest palindrome that can be returned
2. Find the sum of all right leaves in a given binary tree.
3. Given: A string of alphanumeric characters with a length between 0 and 1000Task: Return the first character in the string that does not repeat
4. Design an algorithm that takes a string, for example, abc, and prints out all possible permutations of the string.
5. Design a file system that lets you create new paths and associate them with different values.
6. Design an iterator to flatten a 2D vector. It should support *next* and *hasNext* operations.
7. Given: A list of unique wordsTask: Return all the pairs of distinct indices (i, j) so that the concatenation of the two words, words[i] + words[j], is a palindrome
8. Given: An array of distinct integers, *candidates*, and a target integer *target*Task: Return a list of all unique combinations of *candidates,* where the sum of numbers is *target*
9. Given: A puzzle boardTake: Return the least number of moves required so that the state of the board is solved; if it is impossible, return -1
10. Given: A positive integer nTask: Write a method to return the fewest number of perfect-square numbers that sum to n

336 Palindrome Pairs

251 Flatten 2D Vector

269 Alien Dictionary

68 Text Justification

1 Two Sum

198 House Robber

212 Word Search II

219 Contains Duplicate II

10 Regular Expression Matching

202 Happy Number

108 Convert Sorted Array to Binary Search Tree

136 Single Number

2 Add Two Numbers

160 Intersection of Two Linked Lists

217 Contains Duplicate

190 Reverse Bits

20 Valid Parentheses

220 Contains Duplicate III

385 Mini Parser

221 Maximal Square

23 Merge k Sorted Lists

227 Basic Calculator II

415 Add Strings
