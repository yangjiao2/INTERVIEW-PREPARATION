
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        reminders, res = defaultdict(int), 0
        for ele in time:

            res += reminders[ - ele % 60 ]
            reminders[ ele % 60] += 1
        return res
