# Time:  O(n)
# Space: O(1)


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit=0
        # for i in range(len(prices)-1):
        #     profit+=max(0,prices[i+1]-prices[i])
        # return profit
        profit = 0
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1]-prices)
        return profit
