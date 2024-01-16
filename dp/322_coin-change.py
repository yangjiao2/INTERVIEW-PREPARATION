## DFS

## TLE

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.result = float('inf')
        self.coins = sorted(coins, reverse=True)
        self.dfs(self.coins, [], amount, [])
        return self.result  if self.result != float('inf') else -1

    def dfs(self, nums:List[int], path: List[int], target: int, lst: List[int]):
        if target <= 0:
            if target == 0:
                lst.append(path)
                self.result = min(self.result, len(path))
            return
        for i, num in enumerate(nums):
            self.dfs(nums[i: ], path + [num], target - num, lst)



    ## DP by coin (Bottom up)

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for remaining in range(coin, amount + 1):
                dp[remaining] = min(dp[remaining - coin] + 1, dp[remaining])

        return dp[amount] if dp[amount] != math.inf else -1



    # DP (top-down)
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0

            ans = math.inf
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, dp(amount - coin) + 1)
            return ans

        ans = dp(amount)
        return ans if ans != math.inf else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for amnt in range(1, amount+1):
            for coin in coins:
                if amnt >= coin:
                    dp[amnt] = min(dp[amnt], dp[amnt-coin] + 1)
                else:
                    break  # optimize a bit
                    
        return dp[amount] if dp[amount] != math.inf else -1