
# For each K, we will greedily remove the largest-length course until the total duration start is <= end
# To select these largest-length courses, we will use a max heap.

# Time complexity is O(n*log n), space is O(n).

class Solution:
    def scheduleCourse(self, courses):
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)
