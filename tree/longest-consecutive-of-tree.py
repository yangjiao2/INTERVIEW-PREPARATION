class Solution(object):
    def longestConsecutive(self, root):
        self.max_length = 0
        def dfs(root):
            if not root:
                return 0
            # Default the sequence is expanding.
            L = dfs(root.left) + 1
            # Same procedure for the left and right branches.
            R = dfs(root.right) + 1
            # Condition not satisfied, reset the length to 1.
            if root.left and root.val + 1 != root.left.val:
L=1
if root.right and root.val + 1 != root.right.val:
R=1
length = max(L, R)
self.max_length = max(self.max_length, length) return length
        dfs(root)
        return self.max_length
