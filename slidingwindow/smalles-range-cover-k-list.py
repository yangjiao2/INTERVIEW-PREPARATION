# When doing that, we bind the list-id with each number.
# For example, if the nums is [[3,5], [6,7], [9]],
# the concentrated list is [[3,0], [5,0], [6,1], [7,1], [9,2]].
# Now the original problem becomes a sliding window problem.

# Our task is find the shortest subarray (the start point and end point)
# which contains exactly K=len(nums) kinds of elements.

# We update left pointer by left++ only when the current window contains K kinds of list-id
# (In this case we need to make the window shorter since it already contains K kinds of list-id).
# And let right pointer be the current number index we are visiting.

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        d = []
        K = len(nums)
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            for n in num:
                d.append([n, i])
        d.sort(key=lambda x: x[0])
        #print d
        res = []
        left = 0
        for right, n in enumerate(d):
            count[n[1]] += 1
            while len(count)==K:
                if not res or d[right][0]-d[left][0]<res[1]-res[0]:
                    res = [d[left][0], d[right][0]]
                count[d[left][1]] -= 1
                if count[d[left][1]]==0:
                    count.pop(d[left][1])
                left += 1
        return res
