# https://leetcode.com/problems/sum-of-subarray-minimums/solutions/170776/python-simple-stack-o-n-solution-10-lines/?orderBy=most_votes

# The total sum is sum([n * |left_bounday - indexof(n)| * |right_bounday - indexof(n)| for n in array])
# After a number n pops out from an increasing stack, the current stack top is n's left_boundary, the number forcing n to pop is n's right_boundary.
# A tricky here is to add MIN_VALUE at the head and end.

class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10**9 + 7)
