top_3 = heapq.nsmallest(
...     3, results.splitlines(), key=lambda x: float(x.split()[-1])


Its first child is at 2*k + 1.
Its second child is at 2*k + 2.
Its parent is at (k - 1) // 2.

```py
h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
```

```py
>>> import heapq
>>> a = [2, 5, 3, 7, 6, 8]
>>> heapq.heappush(a, 4)
>>> a
[2, 5, 3, 7, 6, 8, 4]
>>> heapq.heappop(a)
2
>>> heapq.heappop(a)
3
>>> heapq.heappop(a)
4
```
