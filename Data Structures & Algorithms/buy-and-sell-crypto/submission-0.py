class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            # Slicing creates a new list copy each iteration: O(N) space/time penalty
            newl = prices[i+1 : len(prices)] 
            for j in range(0, len(newl)):
                # Fixed: Tracking actual dollar profit instead of index j
                if newl[j] - prices[i] > max_profit: 
                    max_profit = newl[j] - prices[i]

        return max_profit