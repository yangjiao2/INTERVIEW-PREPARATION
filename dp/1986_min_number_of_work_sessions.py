# Input: tasks = [1,2,3], sessionTime = 3
# Output: 2
# Explanation: You can finish the tasks in two work sessions.
# - First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
# - Second work session: finish the third task in 3 hours.


# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks.sort(reverse=True)
        sessions = []
        result = [n]
        
        def dfs(index): 
            if len(sessions) > result[0]: # prune 1
                return
            if index == n:
                result[0] = len(sessions) 
                return
            for i in range(len(sessions)):
                if sessions[i] + tasks[index] <= sessionTime:  # prune 2
                    sessions[i] += tasks[index]
                    dfs(index + 1)
                    sessions[i] -= tasks[index]
            sessions.append(tasks[index])
            dfs(index + 1)
            sessions.pop()
        
        dfs(0)
        return result[0]







class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        def clearBit(x, k):
            return ~(1 << k) & x

        @lru_cache(None)
        def dp(mask, remainTime):
            if mask == 0: return 0

            ans = n  # There is up to N work sessions
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = clearBit(mask, i)
                    if tasks[i] <= remainTime:
                        ans = min(ans, dp(newMask, remainTime - tasks[i]))  # Consume current session
                    else:
                        ans = min(ans, dp(newMask, sessionTime - tasks[i]) + 1)  # Create new session

            return ans

        return dp((1 << n) - 1, 0)