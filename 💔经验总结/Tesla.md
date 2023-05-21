Minimum number of characters to delete from a string so that each character appears unique number of times. Note: You can delete all occurances of characters.
eg: “aaaabbbb” -> 1 “a” or 1"b" would make “a” and “b” appear unique number of times.

Given number in binary form, if its even -> you can divide it by 2; if its odd -> you can substract 1 from it. You can repeat above steps as many times as you want to reach 0. How many steps it took to reach zero?


```py

# List to equation

# idea:
# topological sort

    if vertex.isalpha() and  not vertex in visited:

# adjacencyList store mapping {'char': ['char', value]}
# topological pop out and get result

while order:
        element = order.pop(0)
        for char in adjacencyList[element]:
            if char.isalpha():
                result[element] += result[char]
            else:
                result[element] += int(char)

    # *************   solution      *************  #

from collections import defaultdict
def topologicalSort(vertex, adjacencyList, order, visited):
    if vertex.isalpha() and  not vertex in visited:
        visited.add(vertex)
        for neighbor in adjacencyList[vertex]:
            topologicalSort(neighbor, adjacencyList, order, visited)
        order.append(vertex)

def solve(equations):
    # *************    generate the adjacency-list for the DAG(directed acyclic graph)   ****************
    equationList = equations.split('\n')
    adjacencyList = defaultdict(list)
    for equation in equationList:
        lhs, rhs = equation.split('=')
        lhs_new = ''
        for char in lhs:
            if char == ' ': continue
            lhs_new += char
        for char in rhs:
            if char == '+' or char == ' ': continue
            adjacencyList[lhs_new].append(char)

    # **************  get the topological sort order of the DAG *************
    order = []
    visited = set()
    for vertex in adjacencyList:
        topologicalSort(vertex, adjacencyList, order, visited)

    # ************ solve the equations using topological sort order *********
    result = defaultdict(int)
    while order:
        element = order.pop(0)
        for char in adjacencyList[element]:
            if char.isalpha():
                result[element] += result[char]
            else:
                result[element] += int(char)
    return result

equations = ' A = B + C \n B = C + D + 5 \n C = 5 \n D = 6 '
result = solve(equations)
print(result)
```

```py
def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

```


```py

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    ans = 0
    distinct = 0
    count = collections.Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      if count[c] == 1:
        distinct += 1
      while distinct == k + 1:
        count[s[l]] -= 1
        if count[s[l]] == 0:
          distinct -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```



# # What does this print out?
# a = 1
# b = a
# b += 1
# print(a)
1
# # What does this print out?
# a = [1, 2, 3]
# b = a
# b += [4, 5, 6]
# print (b)
[1, 2, 3, 4, 5, 6]

# # What does this print out?
# a = [1, 2, 3]
# def append(val):
#     val.append(4)

# append(a)
# print(a)
[1, 2, 3, 4]

# # What's the output?
# a = 10
# def inc(val):
#     val += 10
# inc(a)
# print(a)
10
# What does this output?
# a = 1
# def my_func1():
#     a = 3
# my_func1()
# print(a)
1
# print integers from 0 to 9
# lst = [e for e in range(10)]
# for i in lst:
#     if i > 5:
#         break
#     print (i)

# Write a class that:
# * Has two integer properties, x and y
# * Add a method returns a string representation

# obj.x , obj.y

# class Sol1:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def printout(self):
#         print (str(self.x) + ", " + str(self.y))

# s = Sol1(3, 5)
# s.printout()

# Open /home/coderpad/README_IF_YOU_ARE_HACKING_ME
# Read the file
# print the contents

# filepath = '/home/coderpad/README_IF_YOU_ARE_HACKING_ME'
# # with(filepath, 'r') as f:
# f = open(filepath, 'r')
# print (f.read())

# Write a function that extracts the numeric keys from each of these data structures and returns them as a list
A = [{'a': 1.0, 'b': {3: [4, 5.0]}}, 'd', 6]  # [1.0, 4, 5.0, 6]

B = [[[[1.0, 'a'], [2, {}]], [[3, []], [4.0, '4']]], [[[5, ''], [6, 'f']], [[7, 'g'], [8, 'h']]]]  # [1.0, 2, 3, 4.0, 5, 6, 7, 8]

C = {'1': {1: 'a'}, '2': [1, 2.0, 3]}  # [1, 2.0, 3]

res = []

def extract(obj):
    res = []
    # print ('isinstance(obj, dict)', obj, isinstance(obj, float))
    if isinstance(obj, dict):
        res += extract([obj[k] for k in obj])
    elif isinstance(obj, list):
        for ele in obj:
            res += extract(ele)
    elif isinstance(obj, float) or  isinstance(obj, int):
        res.append(obj)

    return res


print (extract([{'a': 1.0, 'b': {3: [4, 5.0]}}, 'd', 6] ))
print (extract([[[[1.0, 'a'], [2, {}]], [[3, []], [4.0, '4']]], [[[5, ''], [6, 'f']], [[7, 'g'], [8, 'h']]]]))



https://app.coderpad.io/7DZWXHDY
