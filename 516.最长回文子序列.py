#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (58.47%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    33.4K
# Total Submissions: 57K
# Testcase Example:  '"bbbab"'
#
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
# 
# 
# 
# 示例 1:
# 输入:
# 
# "bbbab"
# 
# 
# 输出:
# 
# 4
# 
# 
# 一个可能的最长回文子序列为 "bbbb"。
# 
# 示例 2:
# 输入:
# 
# "cbbd"
# 
# 
# 输出:
# 
# 2
# 
# 
# 一个可能的最长回文子序列为 "bb"。
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 只包含小写英文字母
# 
# 
#

思路
这是一道最长回文的题目，要我们求出给定字符串的最大回文子序列。

解决这类问题的核心思想就是两个字“延伸”，具体来说
如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串，因此回文长度增加2
如果一个字符串不是回文串，或者在回文串左右分别加不同的字符，得到的一定不是回文串,因此回文长度不变，我们取[i][j-1]和[i+1][j]的较大值

事实上，上面的分析已经建立了大问题和小问题之间的关联， 基于此，我们可以建立动态规划模型。
我们可以用 dp[i][j] 表示 s 中从 i 到 j（包括 i 和 j）的回文序列长度， 状态转移方程只是将上面的描述转化为代码即可：
if (s[i] === s[j]) {
  dp[i][j] = dp[i + 1][j - 1] + 2;
} else {
  dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j]);
}
base case 就是一个字符（轴对称点是本身）

关键点
”延伸“（extend）
 
复杂度分析
时间复杂度：n2
空间复杂度：n2


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
# @lc code=end

