#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (31.94%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 18K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
# 
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
# 
# 返回 A 中好子数组的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
# [1,2,1,2].
# 
# 
# 示例 2：
# 
# 输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
# 时间复杂度：O(N)O(N)
#空间复杂度：O(1)O(1)
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1

 
        
# @lc code=end

