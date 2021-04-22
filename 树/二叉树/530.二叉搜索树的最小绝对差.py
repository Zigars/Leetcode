#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (61.10%)
# Likes:    245
# Dislikes: 0
# Total Accepted:    61.4K
# Total Submissions: 100.2K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
# 
# 
# 
# 示例：
# 
# 输入：
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# 输出：
# 1
# 
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
# 
# 
#
from typing import TreeNode, List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        #---------------------------------------------------------------#
        #    ctrl+c,ctrl+v from 783
        #    二叉搜索树:
        #    1、中序遍历的输出即为有序数组
        #    2、考虑每个节点与他最近的两个节点之间的最小距离
        #       超过两个节点之间的最小距离一定大于最近两个节点之间
        #    3、通过递归，迭代、莫里斯遍历三种方式遍历
        #    时间复杂度：O(n)
        #    空间复杂度：O(n)
        #---------------------------------------------------------------#
        # 表示正无穷大
        ans = float('inf')
        res = []
        pre = None
        # 莫里斯遍历
        while root:
            # 如果左节点不为空，就将当前节点连带右子树全部挂到
            # 左节点最右子树下面
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                # 将root指向root的left
                tmp = root
                root = root.left
                # 断开原始根节点和左节点的关系
                tmp.left = None
            # 左子树为空，则打印这个节点，并向右边遍历
            # 并保存已遍历的相邻两个节点的最小差值
            else:
                res.append(root.val)
                # print(res)
                root = root.right
                if len(res) > 1:
                    ans = min(ans, res[len(res)-1] - res[len(res)-2])
        return ans
# @lc code=end

