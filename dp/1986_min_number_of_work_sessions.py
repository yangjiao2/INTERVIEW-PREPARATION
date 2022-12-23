# Input: tasks = [1,2,3], sessionTime = 3
# Output: 2
# Explanation: You can finish the tasks in two work sessions.
# - First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
# - Second work session: finish the third task in 3 hours.


# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution:
    def minSessions(self, A, T):
        A.sort(reverse = True)

        if sum(A) <= T:
            return 1
        if min(A) == T:
            return len(A)

        k_min = sum(A) // T
        k_max = len(A)

        for k in range(k_min, k_max):
            ks = [0] * k

            def can_partition(j):
                if j == len(A):
                    for i in range(k):
                        if ks[i] > T:
                            return False
                    return True
                for i in range(k):
                    if ks[i] + A[j] <= T:
                        ks[i] += A[j]
                        if can_partition(j + 1):
                            return True
                        ks[i] -= A[j]
                return False

            if can_partition(0):
                return k
        return len(A)

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks.sort(reverse=True)
        sessions = []
        self.result = [n]

        def dfs(index):
            if len(sessions) >  self.result: # prune 1
                return
            if index == n:
                 self.result = len(sessions)
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
        return  self.result



class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        subsets = []
        self.ans = len(tasks)

        def func(idx):
            if len(subsets) >= self.ans:
                return

            if idx == len(tasks):
                self.ans = min(self.ans, len(subsets))
                return

            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    func(idx + 1)
                    subsets[i] -= tasks[idx]

            subsets.append(tasks[idx])
            func(idx + 1)
            subsets.pop()

        func(0)
        return self.ans


#   bit mask is to use 1's to mark the sessions needs to be filled


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
