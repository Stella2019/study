#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (24.96%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    76.8K
# Total Submissions: 307.6K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 题目数据保证答案肯定是一个 32 位的整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "0"
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：s = "1"
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：s = "2"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 只包含数字，并且可能包含前导零。
# 
# 
#
爬楼梯问题
动态规划
思路
这道题目和爬楼梯问题有异曲同工之妙。
这也是一道典型的动态规划题目。我们来思考：
对于一个数字来说[1,9]这九个数字能够被识别为一种编码方式
对于两个数字来说[10, 26]这几个数字能被识别为一种编码方式
我们考虑用 dp[i]来切分子问题， 那么 dp[i]表示的意思是当前字符串的以索引 i 结尾的子问题。 这样的话，我们最后只需要取 dp[s.length] 就可以解决问题了。
关于递归公式，让我们先局部后整体。对于局部，我们遍历到一个元素的时候， 我们有两种方式来组成编码方式，第一种是这个元素本身（需要自身是[1,9]）, 第二种是它和前一个元素组成[10, 26]。 用伪代码来表示的话就是： dp[i] = 以自身去编码（一位） + 以前面的元素和自身去编码（两位） .这显然是完备的， 这样我们通过层层推导就可以得到结果。
关键点解析
爬楼梯问题（我把这种题目统称为爬楼梯问题）
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  if (s == null || s.length == 0) {
    return 0;
  }
  const dp = Array(s.length + 1).fill(0);
  dp[0] = 1;
  dp[1] = s[0] !== "0" ? 1 : 0;
  for (let i = 2; i < s.length + 1; i++) {
    const one = +s.slice(i - 1, i);
    const two = +s.slice(i - 2, i);

    if (two >= 10 && two <= 26) {
      dp[i] = dp[i - 2];
    }

    if (one >= 1 && one <= 9) {
      dp[i] += dp[i - 1];
    }
  }

  return dp[dp.length - 1];
};
时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
# @lc code=end

