#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #---------------------------------------------------------------#
        #    动态规划：
        #    1、定义数组dp，其中dp[i]表示第i个丑数，第n个丑数即为dp[n]
        #    2、最小的丑数是1，因此dp[1] = 1
        #    3、定义三个指针p2, p3, p5，初始值设置三个指针都是指向位置1，
        #     表示"下一个丑数是当前指针指向的丑数乘以对应的质因数"
        #    4、当2 <= i <= n时，令dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        #    5、 分别比较dp[i]和dp[p2],dp[p3],dp[p5]是否相等
        #      如果相等则将对应的指针＋1
        #---------------------------------------------------------------#
        dp = [0] * (n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n+1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]

# @lc code=end

