# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.


(i + m - 1) / m = ceil(i / m)

class Solution:
    def minimizedMaximum(self, n, Q):
        start, end = 0, max(Q)

        while start + 1 < end:
            mid = (start + end)//2
            if sum(ceil(i/mid) for i in Q) <= n:
                end = mid
            else:
                start = mid

        return end
