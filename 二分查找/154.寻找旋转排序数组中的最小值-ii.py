#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #---------------------------------------------------------------#
        #    二分查找法
        #    此题和153题同属于二分查找法,
        #    区别在于左右不一定会有有序数列，存在全为重复数字的情况。
        #    例如[2,2,2,0,2,2]这种特例
        #    解决方法是对这种特殊情况单独判断,
        #    将当前二分区间的左边界加一，右边界减一，即向中间靠拢，
        #    然后在新区间上继续二分查找。
        #---------------------------------------------------------------#
        left = 0
        right = len(nums) - 1
        while left < right:
            min =left + (right - left) // 2
            print(left, min, right)
            if nums[left] == nums[min] == nums[right] :
                left += 1
                right -= 1
            elif nums[min] > nums[right]:
                left = min + 1
            else:
                right = min
        return nums[left]
# @lc code=end

