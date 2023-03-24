Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        price_gain = []

        for idx in range( len(prices)-1 ):

            if prices[idx] < prices[idx+1]:

                price_gain.append( prices[idx+1]- prices[idx])

        return sum( price_gain )
