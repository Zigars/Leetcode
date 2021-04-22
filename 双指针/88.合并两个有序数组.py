#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #---------------------------------------------------------------#
        #   题解：
        #   逆双指针法，
        #   1、因为不能使用临时变量，所有需要第三个指针，指向数组1的尾部
        #   2、同时每个数组尾部各一个指针，
        #   谁的数大，就先把指针的数放到数组1的尾部，
        #   3、并更新全局指针和局部指针
        #   4、遍历结束后，全部指针的位置都指向-1
        #---------------------------------------------------------------#
        i, j = m-1, n-1
        l = m + n - 1
        while i >= 0 or j >= 0:
            if i == -1:
                nums1[l] = nums2[j]
                j-= 1
            elif j == -1:
                nums1[l] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                i -= 1
            else:
                nums1[l] = nums2[j]
                j -= 1
            l -= 1
# @lc code=end

