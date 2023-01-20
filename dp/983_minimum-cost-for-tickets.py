## Mono Queue

# https://leetcode.com/problems/minimum-cost-for-tickets/solutions/226659/two-dp-solutions-with-pictures/?orderBy=most_votes
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # (days, cost)

        last_7_cost, last_30_cost = collections.deque([]), collections.deque([])
        res = 0
        for day in days:
            while last_7_cost and day - 7 >= last_7_cost[0][0]:
                last_7_cost.pop()
            while last_30_cost and day - 30 >= last_30_cost[0][0]:
                last_30_cost.pop()
            last_7_cost.append(tuple(d, cost[1] + last_7_cost[-1][1]))
            last_30_cost.append(tuple(d, cost[2] +  last_30_cost[-1][1]))
            res= min(res + cost[0], last_7_cost[-1][1], last_30_cost[-1][1])
        return res

## DP

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp=[0 for i in range(days[-1]+1)]
        for i in range(days[-1]+1):
             if i not in days:
                dp[i]=dp[i-1]
             else:
                dp[i]=min(
                    dp[max(0,i-1)]+costs[0],
                    dp[max(0,i-7)]+costs[1],
                    dp[max(0,i-30)]+costs[2])
        return dp[-1]
