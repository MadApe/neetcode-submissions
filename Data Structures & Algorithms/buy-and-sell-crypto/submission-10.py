class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pointers
        left = 0  # buy pointer
        right = 1 # sell pointer
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                # the value on the right is lower than the left value, so it is a new low to buy at
                # therefore move the buy pointer to where the right pointer currently resides
                left = right
            else:
                # the sell price (R ptr) is higher than the buy price (L ptr) so determine if
                # there is a new max profit
                max_profit = max(max_profit, prices[right] - prices[left])

            right += 1  # always move the sell price to the right
        
        return max_profit
        