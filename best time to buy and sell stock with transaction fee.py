class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]    # profit when holding a stock
        cash = 0             # profit when not holding a stock
        
        for price in prices[1:]:
            hold = max(hold, cash - price)        # buy or keep holding
            cash = max(cash, hold + price - fee)  # sell or stay without stock
        
        return cash
