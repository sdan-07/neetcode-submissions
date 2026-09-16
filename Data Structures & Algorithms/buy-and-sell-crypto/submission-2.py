class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy = prices[0]
        maxProfit = curProfit = 0

        for i in range(n-1):
            if buy > prices[i+1]:
                buy = prices[i+1]
            else:
                diff = prices[i+1] - buy
                curProfit = diff
                maxProfit = max(maxProfit, curProfit)

        return maxProfit