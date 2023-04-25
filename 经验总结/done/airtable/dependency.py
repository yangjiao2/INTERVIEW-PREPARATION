# NOTE: PLEASE SELECT PYTHON 3 IN HACKERRANK
#
#
#           bin
#          /   \
#         /     \
#      foo.o   bar.o   baz.o
#       /  \    /  \    /
#      /    \  /    \  /
#   foo.c  utils.h  bar.c
#
rules = {
    'utils.h': [],
    'foo.c': [],
    'bar.c': [],
    'baz.o': ['bar.c'],
    'foo.o': ['foo.c', 'utils.h'],
    'bar.o': ['bar.c', 'utils.h'],
    'bin': ['foo.o', 'bar.o'],
    # ... tens of thousands more targets
}

from collections import defaultdict
class Solution:

    def __init__(self, rules):
        self.rules = rules
        self.degree = defaultdict(int)
        self.reverse_map = defaultdict(set)
        self.visited = set()
        # Feel free to add more instance variables.

    def start_build(self, target):
        '''
        Returns targets to start building that are unblocked, with the end goal being
        to build the passed in primary target.

        `start_build()` is called by the client at the beginning of a build. It is
        guaranteed to be called at most one time, before any calls to `on_complete()`.
        '''
        # Time: O(E)
        # Space: O(V)

        res = set()
        q = [target]
        while q:
            node = q.pop(0)
            self.degree[node] += len(self.rules[node])
            self.visited.add(node)
            if self.rules[node] == []:
                res.add(node)
            for dep in self.rules[node]:
                if dep not in self.visited:
                    q.append(dep)
                self.reverse_map[dep].add(node)

        return list(res)

    def on_complete(self, target):
        '''
        Returns targets to start building that are now unblocked due to the passed in
        target having completed. The end goal is still to build the primary target
        passed into the original `start_build()` call.

        `on_complete()` is called whenever a target has finished building. It will
        only be called once for each target, and will only be called for targets that
        have previously been returned by `start_build()` or other calls to `on_complete()`.
        '''
        # Time: O(target's parents edges)
        # Space: O(V)

        res = set()
        parents = self.reverse_map[target]

        for p in parents:
            self.degree[p] -= 1
            if self.degree[p] == 0:
                res.add(p)
        return res

def assert_dependency_arrays_equal(test_case_name, actual, expected):
    assert len(actual) == len(expected) and sorted(actual) == sorted(expected), \
        "Test case {}: Expecting: {}, but got: {}".format(test_case_name, expected, actual)

solution = Solution(rules)
assert_dependency_arrays_equal("start_build('bin')", solution.start_build("bin"), ["utils.h", "foo.c", "bar.c"])
assert_dependency_arrays_equal("on_complete('foo.c')", solution.on_complete("foo.c"), [])
assert_dependency_arrays_equal("on_complete('bar.c')", solution.on_complete("bar.c"), [])
assert_dependency_arrays_equal("on_complete('utils.h')", solution.on_complete("utils.h"), ["bar.o", "foo.o"])
assert_dependency_arrays_equal("on_complete('foo.o')", solution.on_complete("foo.o"), [])
assert_dependency_arrays_equal("on_complete('bar.o')", solution.on_complete("bar.o"), ["bin"])
print('Succeeded')
