#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (57.93%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] +
# D[l] = 0。
# 
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1
# 之间，最终结果不会超过 2^31 - 1 。
# 
# 例如:
# 
# 
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
#
前置知识
hashTable
 
思路
如果按照常规思路去完成查找需要四层遍历，时间复杂是O(n^4), 显然是行不通的。 因此我们有必要想一种更加高效的算法。

我一个思路就是我们将四个数组分成两组，两两结合。 然后我们分别计算两两结合能够算出的和有哪些，以及其对应的个数。

如图：


454.4-sum-ii
这个时候我们得到了两个hashTable， 我们只需要进行简单的数学运算就可以得到结果。

关键点解析
空间换时间

两两分组，求出两两结合能够得出的可能数，然后合并即可。

 
 
Python3:

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mapper = {}
        res = 0
        for i in A:
            for j in B:
                mapper[i + j] = mapper.get(i + j, 0) + 1
​
        for i in C:
            for j in D:
                res += mapper.get(-1 * (i + j), 0)
        return res
复杂度分析

时间复杂度：O(N^2)O(N 
2
 )​

空间复杂度：O(N^2)O(N 
2
 )
# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
# @lc code=end

