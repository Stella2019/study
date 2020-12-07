#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.93%)
# Likes:    4659
# Dislikes: 0
# Total Accepted:    746.5K
# Total Submissions: 2.1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 示例 4:
# 
# 
# 输入: s = ""
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 由英文字母、数字、符号和空格组成
# 
# 思路
#用一个 hashmap 来建立字符和其出现位置之间的映射。维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
#（1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
#（2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
#（3）重复（1）（2），直到左边索引无法再移动；
#（4）维护一个结果 res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。

#关键点
#用一个 mapper 记录出现过并且没有被删除的字符
#用一个滑动窗口记录当前 index 开始的最大的不重复的字符序列
#用 res 去记录目前位置最大的长度，每次滑动窗口更新就去决定是否需要更新 res
#

# @lc code=start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        l = 0
        ans = 0
        counter = defaultdict(lambda: 0)

        for r in range(len(s)):
            while counter.get(s[r], 0) != 0:
                counter[s[l]] = counter.get(s[l], 0) - 1
                l += 1
            counter[s[r]] += 1
            ans = max(ans, r - l + 1)

        return ans

 
# @lc code=end

