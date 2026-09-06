class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        diff=0
        max_profit = 0

        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i] < prices[j]:
                    diff = prices[j] - prices[i]
                    max_profit = max(max_profit, diff)

        return max_profit