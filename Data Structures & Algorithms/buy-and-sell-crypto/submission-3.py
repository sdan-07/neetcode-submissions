class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in range(len(prices)-1):
            if buy > prices[i+1]:
                buy = prices[i+1]
            else:
                curProfit = prices[i+1] - buy
                max_profit = max(curProfit, max_profit)

        return max_profit