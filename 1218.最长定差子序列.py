#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
#
# algorithms
# Medium (40.45%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 14.6K
# Testcase Example:  '[1,2,3,4]\n1'
#
# 给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于
# difference 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,2,3,4], difference = 1
# 输出：4
# 解释：最长的等差子序列是 [1,2,3,4]。
# 
# 示例 2：
# 
# 
# 输入：arr = [1,3,5,7], difference = 1
# 输出：1
# 解释：最长的等差子序列是任意单个元素。
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
# 输出：4
# 解释：最长的等差子序列是 [7,5,3,1]。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 
# 
#
思路
最直观的思路是双层循环，我们暴力的枚举出以每一个元素为开始元素，以最后元素结尾的的所有情况。很明显这是所有的情况，这就是暴力法的精髓， 很明显这种解法会 TLE（超时），不过我们先来看一下代码，顺着这个思维继续思考。
暴力法
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        res = 1
        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if arr[i] + difference * count == arr[j]:
                    count += 1

                if count > res:
                    res = count

        return res
复杂度分析
时间复杂度：O(N 
2
 )
空间复杂度：n


动态规划
上面的时间复杂度是 O(n^2)， 有没有办法降低到 O(n)呢？很容易想到的是空间换时间的解决方案。
我的想法是将以每一个元素结尾的最长等差子序列的长度统统存起来，即dp[num] = maxLen 这样我们遍历到一个新的元素的时候，就去之前的存储中去找dp[num - difference], 如果找到了，就更新当前的dp[num] = dp[num - difference] + 1, 否则就是不进行操作（还是默认值 1）。
这种空间换时间的做法的时间和空间复杂度都是 O(n)。
关键点解析
将以每一个元素结尾的最长等差子序列的长度统统存起来
代码
 


class Solution:

    # 动态规划
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        res = 1
        dp = {}
        for num in arr:
            dp[num] = 1
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1

        return max(dp.values())

 
复杂度分析
时间复杂度：n
空间复杂度：n

# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
# @lc code=end

