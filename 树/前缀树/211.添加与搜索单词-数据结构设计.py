#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (47.95%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 47.1K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
# '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 
# 实现词典类 WordDictionary ：
# 
# 
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 50000 次 addWord 和 search
# 
# 
#

# @lc code=start
class WordDictionary:
    #---------------------------------------------------------------#
    #   前缀树：
    #   思路和208相同，不同点在于'.'要进行单独判断
    #   通过递归的方法查找
    #---------------------------------------------------------------#
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.root
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree['#'] = {}


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, tree):
            # word中没有字母，判断是否有#，若有表示含有该单词
            if not word:
                if '#' in tree:
                    return True
                return False
            # 如果遇到'.'字符，需要判断从当前节点开始，
            # 所有的后续节点是否符合剩余单词
            if word[0] == '.':
                for t in tree:
                   if helper(word[1:], tree[t]):
                       return True
            # 若是不含有'.'字符，则只递归当前字母的后续节点是否符合
            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            # 未找到字母
            return False
        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

