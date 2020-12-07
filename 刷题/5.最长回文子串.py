#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.45%)
# Likes:    2970
# Dislikes: 0
# Total Accepted:    431.2K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 我们可以用 dp[i][j] 表示 s 中从 i 到 j（包括 i 和 j）是否可以形成回文， 状态转移方程只是将上面的描述转化为代码即可：
#if (s[i] === s[j] && dp[i + 1][j - 1]) {dp[i][j] = true;}
#复杂度分析
#时间复杂度：O(N^2)O(N 2)​

#空间复杂度：O(N^2)O(N 2)

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = s[0]
        def extend(i, j, s):
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1:j]

        for i in range(n - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res
# @lc code=end

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：动态规划， d[i,j] = s[i] == s[j] , if j-i<=1;
        #               d[i,j] = s[i] == s[j] and d[i+1,j-1], if j-i > 1
        # 时间复杂度为O(N^2)，空间复杂度为O(N^2)
        res = ""
        sub_length = 0
        d = [[0] * len(s) for _ in range(len(s))]
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        d[i][j] = 1
                else:
                    if s[i] == s[j] and d[i + 1][j - 1]:
                        d[i][j] = 1
                # 更新最长回文子串
                if d[i][j] and j - i + 1 > sub_length:
                    sub_length = j - i + 1
                    res = s[i:j + 1]
        return res






def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
