#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #---------------------------------------------------------------#
        #    贪心算法（局部最优解-->全局最优解）方法和435类似
        #    首先对气球按end位置进行排序
        #    尝试随机射出一支箭，最多能引爆多少个气球，
        #    调整箭的位置到最前面的气球位置的最右，此时达到了同一支箭能引爆气球的最优解
        #    以前面的气球最右边为边界，查看后面气球的左边是否在这个边界以内
        #    如果在说明这个气球可以被这支箭引爆（因为后面的气球排序后，右端end一定大于这个边界）
        #    直到这个箭不能引爆一个气球，更新新的箭的边界为这个气球的右端，继续循环，count++
        #    循环结束后输出箭的数量即为最小箭矢
        #---------------------------------------------------------------#

        if not points:
            return 0
        # 排序
        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1
        return ans
# @lc code=end

