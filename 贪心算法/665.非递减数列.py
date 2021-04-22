#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #---------------------------------------------------------------#
        #    非递减数列，递增或者有重复数字
        #    遍历一次，使用一个flag记录后面数字比前面数字大的次数
        #    超过1则判断false，否则到循环结束判断正确
        #    这题有个坑，果断是跳了进去啊
        #    遇到nums[i] > nums[i+1]需要进行处理
        #    [3,4,2,3],此时如果只判断两个数之间的关系时
        #    是无法正确判断出是否调整一次就可以非递增
        #    因此除了考虑当前位置与后一位的关系
        #    还要考虑“后一位与前一位的关系”
        #    如果后一位是小于前一位的就把后一位更新为当前位置
        #    原因是当前位置一定是大于前一位的
        #---------------------------------------------------------------#
        flag = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                flag += 1
                if flag > 1:
                    return False
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
        
        return True
# @lc code=end

