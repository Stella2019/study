#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
# https://leetcode-cn.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (53.25%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 53.4K
# Testcase Example:  '[8,1,5,2,6]'
#
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
# 
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
# 
# 返回一对观光景点能取得的最高分。
# 
# 
# 
# 示例：
# 
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# 
# 
#
前置知识
动态规划

公司
阿里

字节

思路
最简单的思路就是两两组合，找出最大的，妥妥超时，我们来看下代码：

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, A[i] + A[j] + i - j)
        return res
我们思考如何优化。 其实我们可以遍历一遍数组，对于数组的每一项A[j] - j 我们都去前面找最大的 A[i] + i （这样才能保证结果最大）。

我们考虑使用动态规划来解决, 我们使用 dp[i] 来表示 数组 A 前 i 项的A[i] + i的最大值。

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        dp = [float('-inf')] * (n + 1)
        res = 0
        for i in range(n):
            dp[i + 1] = max(dp[i], A[i] + i)
            res = max(res, dp[i] + A[i] - i)
        return res
如上其实我们发现，dp[i + 1] 只和 dp[i] 有关，这是一个空间优化的信号。我们其实可以使用一个变量来记录，而不必要使用一个数组，代码见下方。

关键点解析
空间换时间

dp 空间优化

代码
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        pre = A[0] + 0
        res = 0
        for i in range(1, n):
            res = max(res, pre + A[i] - i)
            pre = max(pre, A[i] + i)
        return res
小技巧
Python 的代码如果不使用 max，而是使用 if else 效率目测会更高，大家可以试一下。

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        pre = A[0] + 0
        res = 0
        for i in range(1, n):
            # res = max(res, pre + A[i] - i)
            # pre = max(pre, A[i] + i)
            res = res if res > pre + A[i] - i else pre + A[i] - i
            pre = pre if pre > A[i] + i else A[i] + i
        return res
复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
# @lc code=end

