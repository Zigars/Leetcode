#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List
# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #---------------------------------------------------------------#
        #    贪心算法：
        #    1、第一次遍历，记录每个字母最后出现的位置
        #    2、第二次遍历，确定片段长度
        #    3、找到包含重复字母（最后一次出现-第一次出现）最大的片段
        #       保存这个片段的长度
        #    4、寻找下一个字母的最长片段，直到遍历结束
        #---------------------------------------------------------------#
        last = [0] * 26
        # 第一次遍历，记录每个字母最后出现的位置
        for i, ch in enumerate(S):
            # ord返回ASCII值
            last[ord(ch) - ord('a')] = i
        
        # 保存片段的长度
        partition = []
        start = end = 0
        # 第二次遍历，确定片段长度
        for i, ch in enumerate(S):
            # 重复字母最后出现的位置
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                # 保存片段长度
                partition.append(end - start + 1)
                start = end + 1
        return partition
# @lc code=end

