# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, pre, fast = head, None, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None # cut left sub list here
        n = TreeNode(slow.val)
        n.left = self.sortedListToBST(head)
        n.right = self.sortedListToBST(slow.next)
        return n