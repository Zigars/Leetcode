#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (39.86%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 32.4K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
# 
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# -10^5 
# 
# 
# 
# 
# 进阶：如果行数远大于列数，该如何设计解决方案？
# 
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        #---------------------------------------------------------------#
        #   
        #---------------------------------------------------------------#
# @lc code=end

