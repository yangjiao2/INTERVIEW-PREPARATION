#  https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/solutions/2560101/java-c-python-meeting-room/?orderBy=most_votes
    def minGroups(self, intervals):
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res
