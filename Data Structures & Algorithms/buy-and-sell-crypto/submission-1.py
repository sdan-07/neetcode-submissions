class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit = cur_profit = 0
        buy = prices[0]

        for i in range(n-1):
            if buy > prices[i+1]:
                buy = prices[i+1]
            else:
                cur_profit = prices[i+1] - buy
                max_profit = max(max_profit, cur_profit)
        return max_profit