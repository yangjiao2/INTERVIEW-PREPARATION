
    def PredictTheWinner(self, nums):
        n = len(nums)
        memo = [[-1 for x in range(n)] for y in range(n)]
        scoreFirst = self.PredictTheWinnerInSituation(nums, 0, n - 1, memo)
        scoreTotal = sum(nums)
        return scoreFirst >= scoreTotal - scoreFirst

    def PredictTheWinnerInSituation(self, nums, i, j, memo):
        # Base case.
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if memo[i][j] != -1:
            return memo[i][j]
        # Recursive case.
        curScore = max(nums[i] + min(self.PredictTheWinnerInSituation(nums, i+2, j, memo), self.PredictTheWinnerInSituation(nums, i+1, j-1, memo)),
                       nums[j] + min(self.PredictTheWinnerInSituation(nums, i, j-2, memo), self.PredictTheWinnerInSituation(nums, i+1, j-1, memo)))
        memo[i][j] = curScore
        return curScore
