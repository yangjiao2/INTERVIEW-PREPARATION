
1. dfs (backtrack)

Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
Space complexity: O(M/min_cand)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       # try out each possible cases
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans

class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)


2. dp

# loop through candidates and remaining items

# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]
