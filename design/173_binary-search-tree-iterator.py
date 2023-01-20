# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = collections.deque([])
        self.next_node = root

    def next(self) -> int:
        while self.next_node:
            self.stack.append( self.next_node)
            self.next_node = self.next_node.left
        node = self.stack.pop()
        self.next_node = node.right
        return node.val
        # return self.stack.pop()

    def hasNext(self) -> bool:
        return self.stack or self.next_node != None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
