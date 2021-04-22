#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #---------------------------------------------------------------#
        #    # 贪心算法解法，先满足最小胃口的孩子，且分配最小且合适的饼干，直到没有满足条件的饼干为止
        #    1、对孩子列表和饼干列表进行从小到大排序
        #    2、遍历两个列表，如果孩子的胃口值小于饼干的尺寸child+1，直到cookie没有
        #    3、返回child
        #---------------------------------------------------------------#
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while (child < len(g) and cookie < len(s)):
            if (g[child] <= s[cookie]):
                child = child + 1
            cookie = cookie + 1
        return child
# @lc code=end

