#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Medium (48.38%)
# Likes:    1379
# Dislikes: 0
# Total Accepted:    272.8K
# Total Submissions: 561.4K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2：
# 
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #---------------------------------------------------------------#
        #   动态规划：
        #   1、两种特殊情况，只有一间房屋就偷该间，只有两间房屋时投金额大的
        #   2、偷窃第k间房屋，那么就不能偷窃第k-1间房屋，
        #      偷窃总金额为前k−2间房屋的最高总金额与第k间房屋的金额之和。
        #   3、不偷窃第k间房屋，偷窃总金额为前k−1间房屋的最高总金额。
        #   4、用dp[i]表示前i间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：
        #     dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        #   5、对应特殊情况的的边界条件dp[0]=num[0] , dp[1] = max(dp[0], dp[1])
        #---------------------------------------------------------------#
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]
# @lc code=end

