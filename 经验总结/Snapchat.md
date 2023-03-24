BQ: most challenge project, conflicts with manager and how to convince manager

力扣儿邀零。
1. 物流，2. 散尔酒
76
Task scheduler变种
415 Follow-up是如果2个string可以是负数该怎么办
三菱药
 起伞舞变形
 类似281，但是每个list 是动态的，要实现add and get，要求o1 复杂度
  1153 变种，要求输出需要多少steps
刷题网的二污二，和二污散
 而二期 琪琪儿
 1498

Netflix recommendation system

实现一个消息队列，多个消息源，多个消费线程；类似kafka


实现记住视频上次看到哪了

 Uber's backend

 Design Snap， 300M daily active users 需要有能够发text，photo和 video的功能:
我先给他定义好了，每天大概需要多少storage去存 这些contents。
提到了这个系统需要的non-functional requirements： availability, reliability, scalability
画了building blocks，从user requests 到databases
分析了一下text，phot 和video的存储，用到什么数据库（relational database and No SQL database）；
问了我如何处理group chat存储的问题 - messaging queue， kafka


3) System Design - shorten url
4) System Design - push notification system


Ins story


# snap

slidding puzzle:

step 状态加入dq (string, current_position), 之后pop 拿到当前

`while` 保持循环， `for` loop 一次step 之后可出现的所有possibility

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.**join(str(d) for row in board for d in row)**
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index('0')))
        steps, height, width = 0, len(board), len(board[0])
        **while dq:
            for _ in range(len(dq)):**
                **t, i= dq.popleft()**
                if t == '123450':
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        **ch[i], ch[r * width + c] = ch[r * width + c], '0'** # swap '0' and its neighbor.
                        s = ''.join(ch)
                        if s not in seen:
                            seen.add(s)
                            **dq.append((s, r * width + c))**
            **steps += 1**
        return -1
```

**210. Course Schedule II**

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = collections.defaultdict(list)
        indegree =  collections.defaultdict(int)
        for end, start in prerequisites:
            graph[start].append(end)
            indegree[end] += 1

        # 0 -indegree
        # q = collections.deque([ c for c in list(range(numCourses)) if c not in indegree])

        res = [ c for c in list(range(numCourses)) if c not in indegree]
        print ((graph.items()))
        # visited = set()
        # while q:
        for cur in res:
            # print (q)
            # cur = q.popleft()
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                # if nei not in visited:
                    res.append(nei)

                    # visited.add(nei)
            # res.append(cur)

        return res if len(res) == numCourses else []
```

**609. Find Duplicate File in System**

string.split (char [, maxsplit])

string.partition(char) = pre, equal, suffix **(only 1 time)**

```python

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        contents = collections.defaultdict(list)
        for l in paths:
            path, files = l.split(' ', 1)
            print (path, ', ', files)
            for f in files.split(" "):
                # fname = f[:f.index("(")]
                # content = f[f.index("(") + 1 : -1]
                fname, _, content = f[:-1].partition("(")
                contents[content].append(path.strip()+"/"+fname)

        res = []
        print (contents)
        for c, paths in contents.items():
            if len(paths) >= 2:
                res += [paths]

        return res
```

**1329. Sort the Matrix Diagonally**

[i- j ] for diagnal

```python
def diagonalSort(self, A):
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in xrange(n):
            for j in xrange(m):
                **d[i - j].append(A[i][j])**
        for k in d:
            d[k].sort(reverse=1)
        for i in xrange(n):
            for j in xrange(m):
                A[i][j] = d[i - j].pop()
        return A
```

pages

topogical but checks if indegree = 0 or uneven indegree & outdegree

```java
		firstPage = None
    for page in pageToNumOutpages:
        indegree = pageToNumInpages.get(page, 0)
        outdegree = pageToNumOutpages.get(page, 0)
        **if (indegree == 0) or (outdegree > indegree):**
            firstPage = page
            break
    lastPage = None
    for page in pageToNumInpages:
        indegree = pageToNumInpages.get(page, 0)
        outdegree = pageToNumOutpages.get(page, 0)
        if (outdegree == 0) or (indegree > outdegree):
            lastPage = page
            break
    return [firstPage, lastPage]
```

**Interesting Number**

binary search + hashmap

start = 1, end = target ** (1/expo)

```java
import collections, math

def getInterestingNumber(k):
    left, right  = 1, math.ceil(k ** (1/2))
    combo = collections.defaultdict(list)
    while left < right:

        combo[left **2 + right ** 2] += [left, right],
        combo[(left + 1) **2 + right ** 2] += [left + 1, right],
        combo[left **2 + (right - 1) ** 2] += [left, right - 1],
        left += 1
        right -= 1
        print (left, right, combo)
    return [v  for k, v in combo.items() if len(v) >= 2]
```

**1293. Shortest Path in a Grid with Obstacles Elimination**

状态：(row, column, step)

```java
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        w, h = len(grid[0]), len(grid)
        # manhatton boundary check
        if w + h - 2 < k:
            return w + h - 2

        q = collections.deque([(0, 0, k)]) # r, c, obstacle
        dirs, step = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        visited = set((0,0,k))
        while q:
            print (step, q)
            **for _ in range(len(q)): # loop through one bfs layer
                cur_r, cur_c, cur_obs = q.popleft()**

                # early return check
                **if cur_r == h - 1 and cur_c == w - 1:
                    return step**
                for dx, dy in dirs:
                    r, c = cur_r + dy, cur_c + dx
                    if 0<=r<h and 0<=c<w:
                        obs = cur_obs - grid[r][c]
                        if obs >= 0 and (r, c, obs) not in visited:
                            visited.add((r, c, obs))
                            q.append([r, c, obs])

            step += 1
        return -1
```

**394. Decode String**

when encounter "[", start a new recursive loop

get results which is the string till hits next "]", and move forward for the cursor `i` and reset num

```java
class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        def helper(s):
            i = 0
            num = 0
            acc = ""
            while i < len(s):
                e = s[i]

                if e.isdigit():
                    num = num*10 + int(e)

                elif e == "[":
                    res, e_index = helper(s[i+1:])
                    acc += res * num
                    i += e_index # move i to new beginning
                    num = 0 # reset to orig state

                elif e == "]":
                    return acc,  i + 1

                else:
                    acc += e
                i += 1

            return acc, i

        return helper(s)[0]
```

********************************Meeting Rooms II********************************

扫描线 +/- 计算concurrentcy

```java
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        events = [(it.start, +1) for it in intervals] + [(it.end, -1) for it in intervals]
        events = sorted(events)

        rooms = 0
        max_concurrent = 0
        for t, inc in events:
            **rooms += inc**
            max_concurrent = max(max_concurrent, rooms)

        return max_concurrent
```

**Merge k Sorted Lists**

create `dummy` node

move forward: `list[i] = list[i].next`

heapq 存只能是commparable， 所以存`(value, index of list)`

```markdown
each list's head is added to heap first
move forward: add (next node, index of lists) to heap since ListNode is not comparable
stop if head of list is `null`
```

```java
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop, heapreplace, heapify

        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq, (lists[i].val, i))

        dummy = head = ListNode(0)
        while pq:
            v, i = heappop(pq)

            **lists[i] = lists[i].next**
            head.next = ListNode(v) # lists[i] not working
            head = head.next
            if lists[i]:
                heappush(pq, (lists[i].val, i))

        return dummy.next
```

**210. Course Schedule II**

build graph: graph[起点] += [终点] 和 indegree counter

从 indegree = 0的点开始扫描，add to result when indegree[node] = 0

valid when `n == len(result)`

```java

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = collections.defaultdict(list)
        indegree =  collections.defaultdict(int)
        for end, start in prerequisites:
            graph[start].append(end)
            indegree[end] += 1

        # 0 - indegree
        # q = collections.deque([ c for c in list(range(numCourses)) if c not in indegree])

        res = [ c for c in list(range(numCourses)) if c not in indegree]
        print ((graph.items()))
        # visited = set()
        # while q:
        for cur in res:
            # print (q)
            # cur = q.popleft()
            for nei in graph[cur]:
                indegree[nei] -= 1
                **if indegree[nei] == 0:
                # if nei not in visited:
                    res.append(nei)**

                    # visited.add(nei)
            # res.append(cur)

        return res if len(res) == numCourses else []
```

**216. Combination Sum III**

```java
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Time: n splits for k times, O(n ^ k)
        # Space: O(k)
        lst, res = list(range(1, 10)), []
        def dfs(index, path, target, res):
            if index > 9 or target < 0:
                return
            print (index, path, target)
            if target == 0 and len(path) == k:
                res.append(path)
                return
            else:
								# increasing sequence
                for i in range(index, len(lst)):
                    # no repeat
                    dfs(i + 1, path+[lst[i]], target - lst[i], res)
        dfs(0, [], n, res)
        return res
```

**Combination Sum IV**

*duplicate* results are allowed, else reverse 2 for loops (coin change problem)

```java
class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        **for i in range(target + 1):**
            **for num in nums:**
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]

# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 116 ms
```

**Search Insert Position**

termination: `low = mid + 1 = high = mid`  which means `low < high`

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid] (and nums[mid-1]!=target): # () for duplicates
                low = mid + 1
            else:
                high = mid # insert before mid
        return low
```

**Car Fleet**

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)
```

**Concatenated Words**

dfs + memo

```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)

        @cache
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in wordSet and (suffix in wordSet or dfs(suffix)):
                    return True
            return False

        return [w for w in words if dfs(w)]
```

**329. Longest Increasing Path in a Matrix**

dfs

```python
def longestIncreasingPath(self, M):
        if not any(M): return 0
        d = {}
        def dfs(i, j):
            if not (i, j) in d:
                d[(i, j)] = max(dfs(x, y)
                    if 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y] > M[i][j] else 0
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]) + 1
            return d[(i, j)]
        return max(dfs(i, j) for i in range(len(M)) for j in range(len(M[0])))
```

**797. All Paths From Source to Target**

```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
```

**Backtracking**

```python
def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
```

**Count path for matrix / graph with weight**

**Number of Ways to Arrive at Destination (Dijktra)**

```python
def countPaths(self, A):
        m, n, mod = len(A), len(A[0]), 10 ** 9 + 7
        dp = [[1] * n for i in range(m)]
        for a, i, j in sorted([A[i][j], i, j] for i in range(m) for j in range(n)):
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if 0 <= x < m and 0 <= y < n and A[x][y] < A[i][j]:
                    dp[i][j] += dp[x][y] % mod
        return sum(map(sum, dp)) % mod
```

```python
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for nei, time in graph[u]:
                    if dist[nei] > d + time:
                        dist[nei] = d + time
                        ways[nei] = ways[u]
                        heappush(minHeap, (dist[nei], nei))
                    elif dist[nei] == d + time:
                        ways[nei] = (ways[nei] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)
```

**Cheapest Flights Within K Stops**

k: restriction purpose

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

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1
```

**1293. Shortest Path in a Grid with Obstacles Elimination**

bfs

```python
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        w, h = len(grid[0]), len(grid)
        # manhatton boundary check
        if w + h - 2 < k:
            return w + h - 2

        q = collections.deque([(0, 0, k)]) # r, c, obstacle
        dirs, step = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        visited = set((0,0,k))
        while q:
            print (step, q)
            for _ in range(len(q)): # loop through one bfs layer
                cur_r, cur_c, cur_obs = q.popleft()
                # visited.add((cur_r, cur_c, cur_obs))
                # early return check
                if cur_r == h - 1 and cur_c == w - 1:
                    return step
                for dx, dy in dirs:
                    r, c = cur_r + dy, cur_c + dx
                    if 0<=r<h and 0<=c<w:
                        obs = cur_obs - grid[r][c]
                        if obs >= 0 and (r, c, obs) not in visited:
                            visited.add((r, c, obs))
                            q.append([r, c, obs])

            step += 1
        return -1
```

remove duplicate and return string

```python
def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
```

minSlidingWindow

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        t_ctr = Counter(t)
        missing = len(t_ctr)
        l = 0
        ranges = [l, math.inf]

        for r, c in enumerate(s):
            if c in t_ctr:
                t_ctr[c] -= 1
                if t_ctr[c] == 0:
                    missing -= 1
            # print (r, c, t_ctr, missing)
            while missing == 0 and l <= r:
                c2 = s[l]
                if c2 in t_ctr:
                    t_ctr[c2] += 1
                    if t_ctr[c2] > 0:
                        missing += 1

                if ranges[1] - ranges[0] > r - l:
                    string = [l, r + 1]
                l += 1
                # print ('l', l)


        return s[ranges[0]: ranges[1]] if string[1] != math.inf  else ""
```

**Decode String**

```python
class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]
```

next permutation

```python
def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # prev_min, latter_min = -1, math.inf
        # decending = None
        # for i, e in enumerate(nums):
        #     if i == 0:
        #         continue
        #     if nums[i-1] < nums[i] and decending == None:
        #         prev_min = i -1
        #         decending = False

        #     elif  nums[i-1] > nums[i] and decending == False:
        #         decending = True
        #     elif nums[i-1] < nums[i] and decending == True:
        #         latter_min = min(latter_min, nums[i])

        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part
        print (l, r)

        return nums[:k+1] + nums[k+1:][::-1]
```
