#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (54.53%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 87.7K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#
前置知识
哈希表
数组
二分查找
动态规划
 
思路
关于这个类型， 我专门写了一个专题《你的衣服我扒了 - 《最长公共子序列》》，里面讲了三道题，其中就有这个。
这就是最经典的最长公共子序列问题。一般这种求解两个数组或者字符串求最大或者最小的题目都可以考虑动态规划，并且通常都定义 dp[i][j] 为 以 A[i], B[j] 结尾的 xxx。这道题就是：以 A[i], B[j] 结尾的两个数组中公共的、长度最长的子数组的长度。 算法很简单：
双层循环找出所有的 i, j 组合，时间复杂度 ，其中 m 和 n 分别为 A 和 B 的 长度。
如果 A[i] == B[j]，dp[i][j] = dp[i - 1][j - 1] + 1
否则，dp[i][j] = 0
循环过程记录最大值即可。
关键点解析
dp 建模套路
代码
代码支持：Python
Python Code:
class Solution:
    def findLength(self, A, B):
        m, n = len(A), len(B)
        ans = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
复杂度分析
时间复杂度：mn，其中 m 和 n 分别为 A 和 B 的 长度。
空间复杂度：mn，其中 m 和 n 分别为 A 和 B 的 长度。

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
# @lc code=end

