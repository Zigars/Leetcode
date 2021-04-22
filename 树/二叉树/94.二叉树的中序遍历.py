#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (75.21%)
# Likes:    916
# Dislikes: 0
# Total Accepted:    398.6K
# Total Submissions: 529.7K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # #---------------------------------------------------------------#
        # #    中序遍历：左 打印 右
        # #    递归：
        # #    终止条件：当前节点为空时
        # #    函数内：递归的调用左节点，打印当前节点，再递归调用右节点
        # #---------------------------------------------------------------#
        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     # 按照左-打印-右的方式遍历
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return res

        # #---------------------------------------------------------------#
        # #    迭代实现:
        # #    模仿操作系统或虚拟机实现的堆栈操作
        # #    用堆栈保存节点
        # #---------------------------------------------------------------#
        # res = []
        # stack = []
        # while stack or root:
        #     # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        #     # 模拟递归的调用
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     # 当前节点为空，说明左边已经到头，从栈中弹出节点并保存
        #     # 转向右边节点，继续上面整个过程
        #     else:
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         root = tmp.right
        # return res

        #---------------------------------------------------------------#
        #    莫里斯遍历
        #    1、优点：用递归和迭代的方式都使用了辅助的空间，
        #    而莫里斯遍历的优点是没有使用任何辅助空间。
        #    2、缺点：改变了整个树的结构，强行把一棵二叉树改成一段链表结构
        #---------------------------------------------------------------#
        res = []
        pre = None
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
            else:
                res.append(root.val)
                # print(res)
                root = root.right
        return res
# @lc code=end

