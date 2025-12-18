class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        max_diff = 0

        while r < len(prices) :
            if prices[l] < prices[r]:
                curr_diff = prices[r] - prices[l]
                max_diff = max(max_diff,curr_diff)
            else:
                l = r
            r += 1
            
        return max_diff

        