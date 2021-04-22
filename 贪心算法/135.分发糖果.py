#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        :type ratings: List[int]
        :rtype: int
        """
        #---------------------------------------------------------------#
        #    # 贪心算法解法
        #    如果两边一起考虑一定会顾此失彼
        #    1、将每个人得到的糖果都预设为1
        #    2、正向遍历，如果右边>左边 右边的输出值更新为左边输出值+1
        #    3、反向遍历，如果左边>右边 左边的输出值更新为 左边的原本输出值与右边输出值+1 较大的值
        #    4、对输出列表进行累加，返回累加的结果
        #---------------------------------------------------------------#

        lens = len(ratings)
        output = []
        for i in range(lens):
            output.append(1)
        i = 0
        while i + 1 < lens:
            if ratings[i] < ratings[i + 1]:
                output[i + 1] = output[i] + 1
            i = i + 1
        j = lens - 1
        while j - 1 > -1:
            if ratings[j - 1] > ratings[j]:
                output[j - 1] = max(output[j - 1], output[j] + 1)
            j = j - 1
        sum = 0
        for i in range(lens):
            sum = sum + output[i]

        return sum
# @lc code=end

