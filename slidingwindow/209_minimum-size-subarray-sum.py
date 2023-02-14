
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, counter, l  =0, float("inf"), 0
        for r in range(len(nums)):
            res += nums[r]
            while res >= target:
                counter = min(counter, r - l)
                l += 1
                res -= nums[l]

        return counter if counter != float("inf") else 0
