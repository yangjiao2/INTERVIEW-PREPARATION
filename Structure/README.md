1. [trie](#trie)
2. [segment tree](#segment-tree)

## heap

> h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
> children 2*k + 1 & 2*k + 2, parent (k - 1) // 2.


## trie

## segment tree

```py

# Algorithm:
# 1. Create a segment tree with the given array on indexes
#    Time: O(N) for traversing array, Space: O(N)
#
# 2. Query and Update the tree
#    Time: O(logN) for traversing the heigh of tree, Space: O(logN) for call stack

# Tree Node that stores the low, high index of a segment and the sum of values of the segment
class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.total = 0

    # Method to print the node (For debugging)
    def __str__(self):
        return f'[{self.low}-{self.high}-{self.total}]'

class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.left = None
        self.right = None
        self.node = None

    def __str__(self):
        return f'{self.node} -> {self.left} {self.right}'

    # Recursively create a binary segment tree
    def build(self, low, high):
        self.node = Node(low, high)
        if low == high:
            self.node.total = self.array[low]
            return

        mid = (low + high) // 2

        self.left = SegmentTree(self.array)
        self.left.build(low, mid)

        self.right = SegmentTree(self.array)
        self.right.build(mid + 1, high)

        self.node.total = self.right.node.total + self.left.node.total
        return

    def query(self, low, high):
        # Case 1: Given low and high is completely overlapped by the segment
        if self.node.low >= low and self.node.high <= high:
            return self.node.total

        # Case 2: If it's completely out of segment
        if self.node.high < low or self.node.low > high:
            return 0

        # Case 3: Partial overlap case, ask the children for values
        left = self.left.query(low, high) if self.left else 0
        right = self.right.query(low, high) if self.right else 0
        return left + right

    def update(self, index, val):
        if self.node != None:
            # Recursively update all the segments where the index appears
            if self.node.low <= index <= self.node.high:
                self.node.total += val
                if self.left != None:   self.left.update(index, val)
                if self.right != None:  self.right.update(index, val)

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)
        self.tree.build(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        current = self.tree.query(index, index)
        delta = val - current
        self.tree.update(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)

```
