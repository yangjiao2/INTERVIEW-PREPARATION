# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#  
# Example 1:
# Input: intervals = [[2,6],[1,3],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

def sol1(intervals):
    intervals.sort(key= lambda x: x[0])

    if len(intervals) < 1:
        return []
    res = [intervals[0]]
    prev_end = intervals[0][1]
    for i, interval in enumerate(intervals[1:]):
        s, e = interval
        if s < prev_end:
            res[-1][1] = max(prev_end, e)
            prev_end = max(prev_end, e)
        else:
            res.append([s, e])
            prev_end = e

    return res

intervals = [[2,6],[1,3],[8,10],[15,18]]
print (sol1(intervals))
intervals = [[2,6],[1,3],[8,10],[9,18]]
print (sol1(intervals))
intervals = [[2,6],[11,13], [1,19]]
print (sol1(intervals))

# Time complexity: O(nlogn)
# Space complexity: O(n)
