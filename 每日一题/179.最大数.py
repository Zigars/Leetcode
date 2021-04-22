#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from typing import List
import functools
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #---------------------------------------------------------------#
        #    解法：
        #    1、先将nums中的所有数字转字符串，形成字符串num_str
        #    2、比较两个字符串x，y拼接的结果x+y和y+x哪个更大，
        #       从而确定x和y谁排在前面；将nums_str降序排列
        #    3、返回整个数组排序的结果拼接成字符串，并返回
        #    4、坑：当输入的nums中只有零时，应该返回0而不是“000”，
        #       解决方法：提前判断nums[0]==0
        #---------------------------------------------------------------#
        nums_str = list(map(str, nums))
        compare = functools.cmp_to_key(lambda x, y: 1 if x + y < y + x else -1)
        nums_str.sort(key=compare)
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res
        
        # compare = functools.cmp_to_key(lambda s1, s2: -1 if s1+s2 > s2+s1 else 1)
        # res = ''.join(sorted(list(map(str, nums)), key=compare))
        # return res if res[0] != '0' else '0'
# @lc code=end

