

class Solution():
    def combinationSum(candidates, target):
        lst = []

        self.dfs(candidates, target, [], lst)
        return self.result

    def dfs(candidates, target, path, lst):
        if target = 0:
            self.result.append(lst)
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            self.dfs(candidates[index:], target - candidates[i], lst +  candidates[i], lst)
