#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
# https://leetcode-cn.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.59%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 68.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
# 
# 数学表达式如下:
# 
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5]
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: [5,4,3,2,1]
# 输出: false
# 
#
思路
这道题是求解顺序数字是否有三个递增的排列， 注意这里没有要求连续的，因此诸如滑动窗口的思路是不可以的。 题目要求O(n)的时间复杂度和O(1)的空间复杂度，因此暴力的做法就不用考虑了。
我们的目标就是依次找到三个数字，其顺序是递增的。因此我们的做法可以是依次遍历， 然后维护三个变量，分别记录最小值，第二小值，第三小值。只要我们能够填满这三个变量就返回true，否则返回false。
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
# @lc code=end

