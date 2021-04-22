#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (45.61%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 72.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
# '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 
# board[i][j] 是一个小写英文字母
# 1 
# 1 
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
# 
# 
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #---------------------------------------------------------------#
        #   前缀树+DFS：
        #   参考题解：https://leetcode-cn.com/problems/word-search-ii/solution/python3-dfs-by-trojanmaster-7zmx/
        #   1、通过words里面的单词，来构建Trie，Trie代表了所有单词
        #   2、通过DFS，一边遍历board，一边同时来看Trie
        #   3、优化主要体现在Trie，要一边找一边修改Trie
        #---------------------------------------------------------------#
        m, n = len(board), len(board[0])

        root = {}
        for w in words:
            p = root
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['end'] = w
        
        def dfs(start, p):
            i , j = start[0], start[1]
            c = board[i][j]

            last = p[c].pop('end', False)
            if last:
                res.append(last)

            board[i][j] = '#'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + x, j + y
                if 0<=ni<m and 0<=nj<n and board[ni][nj] in p[c]:
                    dfs((ni, nj), p[c])
            board[i][j] = c

            if not p[c]:
                p.pop(c)

        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs((i, j), root)
        return res



# @lc code=end

