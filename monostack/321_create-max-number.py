# https://leetcode.com/problems/create-maximum-number/description/

# Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# Output: [9,8,6,5,3]

# The final result is the maximum possible merge of all left and right.

# So there're 3 steps:

# iterate i from 0 to k.
# find max number from num1, num2 by select i , k-i numbers, denotes as left, right
# find max merge of left, right


class Solution:
    def maxNumber(self, nums1, nums2, k):

        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):

            res =  [max(a, b).pop(0) for _ in a+b]
            print ('res', res)
            return res

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                for i in range(k+1)
                if i <= len(nums1) and k-i <= len(nums2))
