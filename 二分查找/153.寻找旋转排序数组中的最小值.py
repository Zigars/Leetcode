#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #---------------------------------------------------------------#
        #    二分查找法：收缩边界
        #    包含三种情况：
        #    1、len=1时，left = right，返回唯一值
        #    2、nums[mid] < nums[right]，
        #    nums[mid]是最小值右侧的元素，即最小值在左侧，忽略右半部分
        #    3、nums[mid] > nums[right]，
        #    nums[mid]是最小值左侧的元素，即最小值在左侧，忽略左半部分
        #---------------------------------------------------------------#
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2   
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

# @lc code=end

