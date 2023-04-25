

from collections import defaultdict

def solution(inputs, exe_times):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    res = defaultdict(int)

    for n1, n2 in inputs: # O(E)
        graph[n1].append(n2)
        indegree[n2] += 1
        indegree[n1] += 0
    dependency = defaultdict(int)

    q = [n for n in indegree if indegree[n] == 0] # O(V)

    # # dp[]
    # dp['a'] = 10
    # dp ['c'] = 5 + max(dp['a'] + dp['b'])

    while q:
        node = q.pop(0)
        if node not in exe_times:
            raise ValueError('not known execution for ' + node)
        # print (node, dependency)
        if node in dependency:
            res[node] = exe_times[node] + dependency[node]
        else:
            res[node] = exe_times[node]
        for nei in graph[node]:
            dependency[nei] = max(dependency[nei],  res[node])
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return res

inputs = [['a', 'c'], ['b', 'c']]
exe_times = {'a': 10, 'b': 15, 'c': 5}
# print (solution(inputs, exe_times))

inputs = [['a', 'c'], ['b', 'c'], ['b', 'd'], ['c', 'e'], ['d', 'e']]
exe_times = {'a': 10, 'b': 15, 'c': 5, 'd': 15, 'e': 5}
print (solution(inputs, exe_times))

# TIME: O(V + E)
