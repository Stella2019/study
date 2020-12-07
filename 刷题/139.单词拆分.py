#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (48.57%)
# Likes:    771
# Dislikes: 0
# Total Accepted:    106.7K
# Total Submissions: 219.6K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#
动态规划
思路
这道题是给定一个字典和一个句子，判断该句子是否可以由字典里面的单词组出来，一个单词可以用多次。

暴力的方法是无解的，复杂度极其高。 我们考虑其是否可以拆分为小问题来解决。 对于问题(s, wordDict) 我们是否可以用(s', wordDict) 来解决。 其中 s' 是 s 的子序列， 当 s'变成寻常(长度为 0)的时候问题就解决了。 我们状态转移方程变成了这道题的难点。

我们可以建立一个数组 dp, dp[i]代表 字符串 s.substring(0, i) 能否由字典里面的单词组成， 值得注意的是，这里我们无法建立 dp[i] 和 dp[i - 1] 的关系， 我们可以建立的是 dp[i - word.length] 和 dp[i] 的关系。

我们用图来感受一下：

def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
# @lc code=end

