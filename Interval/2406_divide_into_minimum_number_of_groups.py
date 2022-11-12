# Time:  O(nlogn)
# Space: O(n)


# heappop if no overlap, heappush on the end node  

import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
                        
        # Solution 1:
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq) #  O(log n)
            heappush(pq, right) #  O(log n)
        return len(pq)



# Time:  O(nlogn)
# Space: O(n)

import collections


# sort, line sweep
class Solution2(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = collections.Counter()
        for l, r in intervals:
            events[l] += 1
            events[r+1] -= 1
        print (events) # Counter({1: 2, 5: 1, 2: 1, 6: 0, 9: -1, 4: -1, 11: -2})
        result = curr = 0
        for t in sorted(events.keys()):
            curr += events[t]
            result = max(result, curr)
        return result


Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])