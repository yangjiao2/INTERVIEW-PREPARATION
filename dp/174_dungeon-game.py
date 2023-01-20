# why I put 1 to two neibors of princess?
# To make this formula valid for princess cell: if we have negative number like -5 in this cell, we need 6 hp to survive, if we have non-negative number in this cell, we need 1 hp to survive.

class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)

        return dp[0][0]
