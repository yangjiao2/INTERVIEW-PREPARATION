# We want to find employees who badged into our secured room unusually often. We have an unordered list of names and access times over a single day. Access times are given as three or four-digit numbers using 24-hour time, such as "800" or "2250".
# Write a function that finds anyone who badged into the room 3 or more times in a 1-hour period, and returns each time that they badged in during that period. (If there are multiple 1- hour periods where this was true, just return the first one.)
badge_records = [
  ["Paul", 1315],
  ["Jennifer", 1910],
  ["John", 830],
  ["Paul", 1355],
  ["John", 835],
  ["Paul", 1405],
  ["Paul", 1630],
  ["John", 855],
  ["John", 915],
  ["John", 930],
  ["Jennifer", 1335],
  ["Jennifer", 730],
  ["John", 1630],
  ]
# Expected output:
# {"John": [830, 835, 855, 915, 930]
#  "Paul": [1315, 1355, 1405]}



import heapq
from collections import deque
d = dict()
for e, t in badge_records:
    # print (e, e not in d)
    if e not in d:
        d[e] = []
        heapq.heappush(d[e], t)
    else:
        heapq.heappush(d[e], t)

print (d)
res = dict()
for e, times in d.items():
    stack = deque([])

    stack.append(heapq.heappop(d[e]))
    stack.append(heapq.heappop(d[e]))
    print(2, d[e], stack)
    while len(d[e]) > 0:

        if d[e][0] - stack[0] <= 100:  # time format
            stack.append(d[e][0])
            res[e] = stack
            break
        stack.append(heapq.heappop(d[e]))
        stack.popleft()

print(res)
