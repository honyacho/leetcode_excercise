from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [(0,0,0)]*len(prices)
        for i in range(1, len(prices)):
            kaeru = prices[i] - prices[i-1]
            dp[i] = (max(kaeru + dp[i-1][0], kaeru + dp[i-1][1]), max(dp[i-1][2], dp[i-1][1]), dp[i-1][0])
        return max(*dp[len(prices)-1])
