#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         #---------------------------------------------------------------#
#         #    二分查找法（右中位数）
#         #    左右必会有一部分为有序，先找到有序部分，
#         #    只需要判断target是否在有序部分，
#         #    不在的话就进行设置mid为新的边界，去无序部分继续查找。
#         #---------------------------------------------------------------#
#         left = 0
#         right = len(nums) - 1
#         # while中无等于判断
#         while left < right:
#             # 选取右中位数
#             mid = left + (right - left + 1) // 2
#             print(left, mid, right)
#             # 右半部分有序
#             if nums[mid] < nums[left]:
#                 if nums[mid] <= target <= nums[right]:
#                     # 下一轮搜索区间为[mid, right]
#                     left = mid
#                 else:
#                     # 下一轮搜索区间为[left, mid -1]
#                     right = mid -1   
#             # 左半部有序                 
#             else:
#                 if nums[left] <= target < nums[mid]:
#                     # 下一轮搜索区域[left, mid - 1]
#                     right = mid - 1
#                 else:
#                     # 下一轮搜索区间为[mid, right]
#                     left = mid
#         return left if nums[left] == target else -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #---------------------------------------------------------------#
        #    二分查找法（左中位数）,收缩边界到left
        #    左右必会有一部分为有序，先找到有序部分，
        #    只需要判断target是否在有序部分，
        #    不在的话就进行设置mid为新的边界，去无序部分继续查找。
        #---------------------------------------------------------------#
        left = 0
        right = len(nums) - 1
        # while中无等于判断
        while left < right:
            # 选取左中位数
            mid = left + (right - left) // 2
            print(left, mid, right)
            # 左半部分有序
            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    # 下一轮搜索区间为[left, mid]
                    right = mid
                else:
                    # 下一轮搜索区间为[mid + 1, right]
                    left = mid + 1   
            # 右半部有序                 
            else:
                if nums[mid] < target <= nums[right]:
                    # 下一轮搜索区域[mid + 1, right]
                    left = mid + 1
                else:
                    # 下一轮搜索区间为[left, mid]
                    right = mid
        return left if nums[left] == target else -1
# @lc code=end

