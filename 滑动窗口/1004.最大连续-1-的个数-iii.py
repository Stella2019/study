#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# https://leetcode-cn.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (54.82%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 31.2K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 
# 返回仅包含 1 的最长（连续）子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 
# 示例 2：
# 
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1 
# 我们继续回到刚才的思路。这道题和通用套路不同的是，我们只需要记录下加入窗口的是0还是1：

#如果是1，我们什么都不用做
#如果是0，我们将K减1
#相应地，我们需要记录移除窗口的是0还是1:
#如果是1，我们什么都不做
#如果是0，说明加进来的时候就是1，加进来的时候我们K 减去了1，这个时候我们再加1。
#复杂度分析
#时间复杂度：O(N)
#空间复杂度：O(1)

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0

        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
        
# @lc code=end

