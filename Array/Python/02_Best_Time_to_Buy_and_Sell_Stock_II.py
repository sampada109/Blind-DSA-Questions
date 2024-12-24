# Best Time to Buy and Sell Stock II
# Question Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = 0
        maxi = 0
        profit = 0
        
        i = 1
        
        while(i < len(prices)):
            
            if(mini > maxi):
                maxi = mini
            
            mini = min(prices[i], prices[i-1])
            maxi = max(maxi, prices[i]-mini)
            profit += prices[i]-mini
            
            i += 1
            
        return profit
