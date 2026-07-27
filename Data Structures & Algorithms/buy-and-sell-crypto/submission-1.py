class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        if len(prices) == 1:
            return 0
        maxP = prices[r] - prices[l]
        while r < len(prices):
            maxP = max((prices[r]-prices[l], maxP))
            if prices[r] < prices[l]:
                l = r
            r += 1
        maxP = max(maxP, 0)
        return maxP