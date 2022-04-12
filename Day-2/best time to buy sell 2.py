class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for I in range(len(prices)-1):
            if prices[I]<prices [I+1]:
                max_profit+=(prices [I+1]-prices[I])
                
                
        return max_profit 
        