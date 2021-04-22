#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #---------------------------------------------------------------#
        #    贪心算法
        #    计算相隔两天的利润
        #    利润为正就sum++
        #    利润不加或减就忽略
        #---------------------------------------------------------------#
        sum = 0 # 钱数
        l = len(prices) # 交易天数
        for i in range(l-1):
            if prices[i+1] > prices[i]:
                sum += prices[i+1] - prices[i]
        return sum

# @lc code=end

