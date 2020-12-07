#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.68%)
# Likes:    446
# Dislikes: 0
# Total Accepted:    68.5K
# Total Submissions: 132.6K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#
"""数学
回溯
factorial"""
思路
LeetCode 上关于排列的题目截止目前（2020-01-06）主要有三种类型：
生成全排列
生成下一个排列
生成第 k 个排列（我们的题目就是这种）
我们不可能求出所有的排列，然后找到第 k 个之后返回。因为排列的组合是 N！，要比 2^n 还要高很多，非常有可能超时。我们必须使用一些巧妙的方法。
我们以题目中的 n= 3 k = 3 为例：
"123"
"132"
"213"
"231"
"312"
"321"
可以看出 1xx，2xx 和 3xx 都有两个，如果你知道阶乘的话，实际上是 2！个。 我们想要找的是第 3 个。那么我们可以直接跳到 2 开头，我们排除了以 1 开头的排列，问题缩小了，我们将 2 加入到结果集，我们不断重复上述的逻辑，知道结果集的元素为 n 即可。
关键点解析
找规律
排列组合
时间复杂度：O(N^2)O(N 
2
 )​

空间复杂度：O(N)O(N)
# @lc code=start
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        candidates = [str(i) for i in range(1, n + 1)]

        while n != 0:
            facto = math.factorial(n - 1)
            # i 表示前面被我们排除的组数，也就是k所在的组的下标
            # k // facto 是不行的， 比如在 k % facto == 0的情况下就会有问题
            i = math.ceil(k / facto) - 1
            # 我们把candidates[i]加入到结果集，然后将其弹出candidates（不能重复使用元素）
            res += candidates[i]
            candidates.pop(i)
            # k 缩小了 facto *  i
            k -= facto * i
            # 每次迭代我们实际上就处理了一个元素，n 减去 1，当n == 0 说明全部处理完成，我们退出循环
            n -= 1
        return res
 # @lc code=end

