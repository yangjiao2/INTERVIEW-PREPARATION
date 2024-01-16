
class Solution:
    def reverseBetween(self, head, m, n):
        if m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
            
        curr = pre.next
        nxt = curr.next
        
        for i in range(n-m):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
            
        
        pre.next.next, pre.next = nxt, curr
         
        return dummy.next



class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev