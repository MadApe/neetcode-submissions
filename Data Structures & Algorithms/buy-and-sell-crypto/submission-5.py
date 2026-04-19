class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        buy_day = 0
        sell_day = 0

        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                print(f"prices[i{i}]={prices[i]},prices[j{j}]={prices[j]},profit={prices[j] - prices[i]},prev_max_profit={max_profit}")
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit
