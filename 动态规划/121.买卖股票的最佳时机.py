#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         #---------------------------------------------------------------#
#         #    暴力破解（超时）
#         #    找到每一天买入后，后面每一天卖出的的利润最大值
#         #    通俗点，今天买入了，看看后面几天哪一天卖出最赚钱
#         #    限定条件只能买卖一次
#         #---------------------------------------------------------------#
#         ant = 0
#         l = len(prices)
#         for i in range(l):
#             for j in range(i+1, l):
#                 ant = max(ant, prices[j] - prices[i])
#         return ant

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #---------------------------------------------------------------#
        #    官方解法：
        #    遍历一遍数组，计算每次
        #    “到当天为止” 
        #    的最小股票价格和最大利润。
        #    一定注意是到当天为止，
        #    至于之后出现最小的价格，需要重新计算利润，
        #    只要还小于最大利润，就不更新。
        #---------------------------------------------------------------#
        l = len(prices)
        minprice = prices[0] 
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(price, minprice)
            
        return maxprofit

# 此题还可以用动态规划，之后再专题练习
# @lc code=end

