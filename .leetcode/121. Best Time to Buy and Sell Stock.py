class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for price in prices[1:]:
            if price < buy:
                buy = price
            
            if profit < price - buy:
                profit = price - buy
        
        return profit
