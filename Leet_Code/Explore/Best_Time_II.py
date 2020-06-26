""" Best Time to Buy and Sell Stock II

Question:

    Say you have an array prices for which the ith eleent is the price of a
    given stock on day i.

    Design an algorithm to find the max profit, given that you may complete as
    many transactions as you would like - buy/sell one share of stock multiple
    times.

+++

Solution:

    The question appears to ask us design a complex algorithm to simulate the
    how to find the max profit. However, once you visualize this in the graph
    form, the problem becomes much simpler. In fact, all the max profit that can
    be had is the sum of all the positive gains to be made from one value from
    another. So long as the values increase, we add that difference to our total
    profit. Thus, we only require O(n) time to complete the task.

"""

class Solution:
    def findMaxProfit(self, prices):
        total = 0
        for i, price in enumerate(prices):
            if i > 0 and prices[i-1] < price:
                total += price - prices[i-1]
        return total
