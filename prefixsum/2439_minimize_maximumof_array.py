
# Input: nums = [3,7,1,6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
# Therefore, we return 5.

# Idea:

# We actully move the value of A[i] to A[i - 1] by 1,
# the sum won't change.

# If A[i] < A[i + 1],
# then we can repeatly do the operations,
# until A[i] >= A[i+1].
# So finally the array A will become decrescent order.


# We calculate the prefix sum arrray and their average.
# The average is the lower bound of the result

# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/java-c-python-prefix-sum-average-o-n/

# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2836579/easy-to-understand-o-n-time-and-o-1-space-solution-with-detailed-explanation/


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum_sum = maximum = 0

        for i, num in enumerate(nums, start=1):
            cum_sum += num
            print (num, cum_sum)
			# At each step, we can try to minimize the element by evenly placing
			# the excess between the previous elements.
            maximum = max(ceil(cum_sum / i), maximum)

        return maximum
