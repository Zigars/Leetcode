#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #---------------------------------------------------------------#
        #    双指针法：
        #    定义双指针分别在在首部和尾部，相加与target比较
        #    如果等于则返回两个指针；
        #    如果小于target则首指针后移
        #    如果大于target则尾指针前移
        #---------------------------------------------------------------#
        first = 0
        last = len(numbers) - 1
        while first <= last:
            if numbers[first] + numbers[last] == target:
                return [first + 1, last + 1]
            if numbers[first] + numbers[last] < target:
                first += 1
            else:
                last -= 1
# @lc code=end

