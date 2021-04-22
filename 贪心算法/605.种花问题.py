#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #---------------------------------------------------------------#
        #    数学归纳法
        #    统计连续的0的区间，分别有多少个连续的0即可。
        #    对于每一段0区间，都可以根据公式直接算出可以种几朵花。
        #    1）对于中间的0区间：
        #        1~2个0：可种0朵；
        #        3~4个：可种1朵；
        #        5~6个：可种2朵；
        #        ...  
        #        count个：可种 (count-1)/2 朵
        #    2)对于两头的0区间，由于左边、右边分别没有1的限制，可种花朵数稍有不同。
        #     为了代码流程的统一，可以在数组最左边、数组最右边分别补1个0，意味着花坛左边、右边没有花。
        #     这样公式就跟1）相同了。
        #---------------------------------------------------------------#
        flowerbed.insert(0, 0)
        l = len(flowerbed)
        flowerbed.insert(l, 0)
        # print(flowerbed)
        count = 0
        count_zero = 0
        for i in range(0, l+1):
            if flowerbed[i] == 0:
                count_zero += 1
            else:
                count += (count_zero - 1) // 2
                if count >= n:
                    return True
                count_zero = 0
        count += (count_zero - 1) // 2
        print(count)
        return count >= n

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         #---------------------------------------------------------------#
#         #    贪心算法解决 
#         #    考虑每个花坛及其左右是否为0 为0就种下花
#         #    考虑三种特殊情况
#         #     1、只有一个花坛
#         #     2、起始花坛
#         #     3、结束花坛
#         #---------------------------------------------------------------#
#         count = 0
#         l = len(flowerbed)
#         # 只有一个花坛时
#         if flowerbed == [1] and n >= 1:
#             return False
#         elif flowerbed == [0] and n <= 1:
#             return True
#         # 起始花坛 0
#         if flowerbed[0]==0 and flowerbed[1] == 0:
#             flowerbed[0] = 1
#             count += 1
#         # 正常判断 [1,l-2]
#         for i in range(1, l-1):
#             if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
#                 flowerbed[i] = 1
#                 count += 1
#         # 结束花坛 l-1
#         if flowerbed[l-1] == 0 and flowerbed[l-2] == 0:
#             flowerbed[i-1] = 1
#             count += 1
#         print(flowerbed, count)
#         if count >= n:
#             return True
#         else:
#             return False
# @lc code=end

