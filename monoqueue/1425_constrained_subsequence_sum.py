
# https://leetcode.com/problems/constrained-subsequence-sum/description/
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dec_q = collections.deque() ## index
        sum_dp = nums[:] ## local max
        res = 0
        for i, ele in enumerate(nums):
            print i
            print( 'sum_dp', sum_dp)
            print ('dec_q', dec_q)
            if dec_q:
                print ('sum_dp[dec_q[0]]', sum_dp[dec_q[0]])
                sum_dp[i] += sum_dp[dec_q[0]]
            res = max(res, sum_dp[i])
            if dec_q and i - k >= dec_q[0]:
                dec_q.popleft()
            print ('dec_q 2', dec_q)
            print( 'sum_dp 2', sum_dp)
            while (dec_q and sum_dp[i] >= sum_dp[dec_q[-1]]):
                dec_q.pop()

            # if (sum_dp[i] > 0):
            dec_q.append(i)

        return max(sum_dp)


        # dp = nums[:1]
        # print ('-', dp)
        # decrease = collections.deque(dp)
        # for i, x in enumerate(nums[1:], 1):
        #     if i > k and decrease[0] == dp[i - k - 1]:
        #         decrease.popleft()
        #     sum_at_x = max(x, decrease[0] + x)
        #     dp += sum_at_x,
        #     print (dp)
        #     while decrease and decrease[-1] < sum_at_x:
        #         print ('pop', decrease)
        #         decrease.pop()
        #     decrease += sum_at_x,
        # return max(dp)
