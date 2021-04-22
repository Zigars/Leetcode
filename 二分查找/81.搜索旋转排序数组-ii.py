#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #---------------------------------------------------------------#
        #    二分查找法
        #    此题和33题同属于二分查找法,
        #    区别在于左右不一定会有有序数列，存在全为重复数字的情况,
        #    例如[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] 2,
        #    解决方法是对这种特殊情况单独判断,
        #    将当前二分区间的左边界加一，右边界减一，即向中间靠拢，
        #    然后在新区间上继续二分查找。
        #    使用左中位数的方法？
        #---------------------------------------------------------------#
        left = 0
        right = len(nums) - 1
        # while中无等于判断
        while left < right:
            # 选取右中位数
            mid = left + (right - left + 1) // 2
            print(left, mid, right)
            # 特殊情况边界和中位数都相等
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # 右半部分有序
            elif nums[mid] < nums[left]:
                if nums[mid] <= target <= nums[right]:
                    # 下一轮搜索区间为[mid, right]
                    left = mid
                else:
                    # 下一轮搜索区间为[left, mid -1]
                    right = mid -1   
            # 左半部分有序                 
            else:
                if nums[left] <= target < nums[mid]:
                    # 下一轮搜索区域[left, mid - 1]
                    right = mid - 1
                else:
                    # 下一轮搜索区间为[mid, right]
                    left = mid
        return True if nums[left] == target else False
# @lc code=end

