class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        max_profit = 0
        while r < n:
            if prices[l] > prices[r]:
                l = r
                r +=1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        return max_profit
