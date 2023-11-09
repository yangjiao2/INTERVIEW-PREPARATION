class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0

        dp = [0] * (len(nums) + 1)


        for i in range(1, len(nums) + 1):
            if i == 1:
                dp[i] = nums[0]
            elif i > 1:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        print (dp)
        return dp[-1]
            


class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now



class Solution(object):
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def simple_rob(nums, i, j):
            rob, not_rob = 0, 0
            for idx in range(i, j):
                num = nums[idx]
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(simple_rob(nums, 1, n), simple_rob(nums, 0, n-1))