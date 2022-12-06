# Time:  O(m * n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range (m)]
        r, c, d_index = 0, 0, 0
        direction_lst = [(0,1), (1, 0), (0, -1), (-1, 0)]
        direction = direction_lst[d_index]
        while (head.next != None):
            res[r][c] = head.val
            head = head.next
            if (r+ direction[0] < 0 or  r+ direction[0] >= m or c + direction[1] < 0 or c + direction[1] >= n  or  res[r+ direction[0]][c + direction[1]] != -1):
                d_index = (d_index + 1)%4
                direction = direction_lst[d_index]
            r, c = r+direction[0] , c+direction[1]
        res[r][c] = head.val 
        return res