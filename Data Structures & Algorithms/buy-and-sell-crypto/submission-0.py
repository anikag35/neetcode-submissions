class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            left = i
            right = i+1
            while (right != len(prices)):
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
                right += 1
        return maxProfit