# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1

        def partition(lst, l, r, index):
            if r == l:
                return lst[l]


            # choose random pivot
            pivot_index = random.randint(l, r)

            # move pivot to beginning of list
            lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

            # partition
            i = l
            for j in xrange(l+1, r+1):
                if lst[j] < lst[l]:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]


            # move pivot to correct location
            lst[i], lst[l] = lst[l], lst[i]

            # recursively partition one side only
            if index == i:
                return lst[i]
            elif index < i:
                return partition(lst, l, i-1, index)
            else:
                return partition(lst, i+1, r, index)

        median = partition(nums, 0, len(nums) - 1,  len(nums) / 2)
        return sum([abs(i - median) for i in nums])



        # ------------------
        # Approach 1: find median
        # Approach 2: for x = median, (x - nums[i]) + (nums[n-1-i] - x) = nums[n-1-i] - nums[i] is the total steps

        # ------------------
        # Use quick select to select the median
        # Time complexity: O(n) average case (read this Guide for Quick Select)
        # Space complexity: O(logn)

        # ------------------

        # incorrect : need to find median

        # print ( str(sum(nums))+' / ' +  str(len(nums)) )
        # middle_point = sum(nums) / len(nums)
        # return sum([abs(i - middle_point) for i in nums])
