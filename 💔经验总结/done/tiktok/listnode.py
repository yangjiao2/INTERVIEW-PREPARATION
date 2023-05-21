

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#  
# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol2(head):
    dummy = ListNode(0)
    dummy.next = head
    curr, prev = dummy.next, dummy
    while curr:
        # print (prev.val, curr.val)
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            prev.next = curr.next # (*)
        else:
            # if curr.next and curr.val != curr.next.val:
            prev = prev.next
        curr = curr.next


    return dummy.next
            # prev   cur
head_lst = [1, 2, 3, 3,4, 4, 5] # 4,5
# 1 , 2
# 2 , 3
# 2 , 3(2) -> 4 4 (*)

dummy1 = ListNode(0)
node = dummy1
for e in head_lst:
    node.next = ListNode(e)
    node = node.next


res = sol2(dummy1.next)
acc = []
while res:
    acc.append(res.val)
    res = res.next
# print (acc)

# O(n)
