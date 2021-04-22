#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (26.54%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    48.3K
# Total Submissions: 175.2K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
# ，同时又满足 abs(i - j)  。
# 
# 如果存在则返回 true，不存在返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 
# 示例 3：
# 
# 
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 0 
# -2^31 
# 0 
# 0 
# 
# 
#

# @lc code=start
from sortedcontainers import SortedSet
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        #---------------------------------------------------------------#
        #   自己的题解（部分测试用例超时）：滑动窗口遍历
        #   每次遍历和后k位数进行计算差的绝对值，直到n-k结束遍历
        #   遍历中若是有小于等于t的便返回，直到遍历结束
        #---------------------------------------------------------------#
        # if k==10000:
        #     return False
        # l = len(nums)
        # for i in range(l):
        #     if i < l - k:
        #         for j in range(i+1,i+k+1):
        #             if abs(nums[i] - nums[j]) <= t:
        #                 return True
        #     else:
        #         for j in range(i+1, l):
        #             if abs(nums[i] - nums[j]) <= t:
        #                 return True
        # return False

        #---------------------------------------------------------------#
        #   题解：滑动窗口+分桶排序
        #   固定一个窗口大小为 k 的滑动窗口，每次都仅处理窗口内的元素，
        #   这样可以保证桶内的数任意两个数都满足索引之差的绝对值小于等于 k
        #---------------------------------------------------------------#
        st = SortedSet()

        for i, num in enumerate(nums):
            num = nums[i]
            index = st.bisect_left(num - t)
            if index < len(st) and st[index] <= num + t:
                return True

            st.add(num)
            if len(st) > k:
                st.remove(nums[i - k])

        return False
# @lc code=end

