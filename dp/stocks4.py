class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)

        if n == 0:

            ## Base case:
            # Price sequence is empty, we can do nothing : )
            return 0


        ## General case:

        # DP[ k ][ d ] = max profit on k, d
        # where k stands for k-th transaction, d stands for d-th trading day.
        dp = [ [ 0 for _ in range(n)] for _ in range(k+1) ]


        # Update by each transction as well as each trading day
        for trans_k in range(1, k+1):

            # Balance before 1st transaction must be zero
            # Buy stock on first day means -prices[0]
            cur_balance_with_buy = 0 - prices[0]

            for day_d in range(1, n):

                # Either we have finished all k transactions before, or just sell out stock and finished k-th transaction today
                dp[trans_k][day_d] = max( dp[trans_k][day_d-1], cur_balance_with_buy + prices[day_d] )
                # Either keep holding the stock we bought before, or just buy in today
                cur_balance_with_buy = max(cur_balance_with_buy, dp[trans_k-1][day_d-1] - prices[day_d] )
                print(day_d, cur_balance_with_buy, dp[trans_k-1][day_d-1] , prices[day_d])
            print(dp)

        return dp[k][n-1]
