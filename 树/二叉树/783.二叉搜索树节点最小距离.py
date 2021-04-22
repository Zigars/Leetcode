#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
from typing import TreeNode, List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #---------------------------------------------------------------#
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

