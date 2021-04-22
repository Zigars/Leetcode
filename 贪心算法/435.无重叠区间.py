#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #---------------------------------------------------------------#
        #    # 贪心算法解法,选择的区间结尾越小，余留给其它区间的空间就越大
        #    1、如果输如为空返回零
        #    2、按照结尾的大小进行增序排序
        #    3、设定起始的位置为最小序列的end，res为0
        #    4、从第二个序列循环，如果循环内序列的begin<设置的end，res+1（表示发现重叠的序列）；
        #    否则更新为新序列的end，代表已留下的最大右边界（表示未发现重叠的序列）
        #    5、循环结束后输出res
        #---------------------------------------------------------------#
        if not intervals:
            return 0
        intervals.sort(key=lambda value: value[1])
        cur_location = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_location:
                res += 1
            else:
                cur_location = intervals[i][1]
        return res
# @lc code=end

