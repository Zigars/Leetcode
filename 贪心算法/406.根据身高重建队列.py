#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #---------------------------------------------------------------#
        #    贪心算法
        #    此题和135分发糖果有着相同的思想
        #    遇到两个维度权衡的时候，一定要先确定一个维度，再确定另一个维度。
        #    如果同时考虑身高和排序，就一定会顾此失彼
        #    先按身高排序降序之后，再按位置k升序排序(减少操作次数，保证相同身高时的正确性)， 
        #    优先按身高高的人的位置k来插，
        #    后续插入的人不会影响到前面已经插好的节点，
        #    最终按照身高k的规则完成了队列
        #    所以在按照身高从大到小排序后：
        #    局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性
        #    全局最优：最后都做完插入操作，整个队列满足题目队列属性
        #---------------------------------------------------------------#
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            if len(output) <= p[1]:
                output.append(p)
            elif len(output) > p[1]:
                output.insert(p[1], p)
        return output
# @lc code=end

