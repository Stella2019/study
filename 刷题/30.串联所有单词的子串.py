#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (32.86%)
# Likes:    392
# Dislikes: 0
# Total Accepted:    51.2K
# Total Submissions: 154.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
# 
# 
# 
# 示例 1：
# 
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
# 
# 示例 2：
# 
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
# 
# 
#
前置知识
字符串

数组

哈希表

 
思路
本题是要我们找出 words 中所有单词按照任意顺序串联形成的单词中恰好出现在 s 中的索引，因此顺序是不重要的。换句话说，我们只要统计每一个单词的出现情况即可。以题目中 s = "barfoothefoobarman", words = ["foo","bar"] 为例。 我们只需要统计 foo 出现了一次，bar 出现了一次即可。我们只需要在 s 中找到同样包含一次 foo 和一次 bar 的子串即可。由于 words 中的字符串都是等长的，因此编码上也会比较简单。

我们的目标状态是 Counter(words)，即对 words 进行一次计数。

我们只需从头开始遍历一次数组，每次截取 word 长度的字符，一共截取 words 长度次即可。

如果我们截取的 Counter 和 Counter(words)一致，则加入到 res

否则我们继续一个指针，继续执行步骤二

重复执行这个逻辑直到达到数组尾部

关键点解析
Counter

代码
语言支持：Python3

from collections import Counter
​
​
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        res = []
        n = len(words)
        word_len = len(words[0])
        window_len = word_len * n
        target = Counter(words)
        i = 0
        while i < len(s) - window_len + 1:
            sliced = []
            start = i
            for _ in range(n):
                sliced.append(s[start:start + word_len])
                start += word_len
            if Counter(sliced) == target:
                res.append(i)
            i += 1
        return res
复杂度分析

其中 N 为 words 中的总字符数。

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
# @lc code=end

