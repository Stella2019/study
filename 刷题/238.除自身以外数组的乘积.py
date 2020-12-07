#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (71.16%)
# Likes:    659
# Dislikes: 0
# Total Accepted:    88.5K
# Total Submissions: 124.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
# 
# 
# 
# 示例:
# 
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
# 
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#
思路
这道题的意思是给定一个数组，返回一个新的数组，这个数组每一项都是其他项的乘积。 符合直觉的思路是两层循环，时间复杂度是O(n^2),但是题目要求Please solve it without division and in O(n)。

因此我们需要换一种思路，由于输出的每一项都需要用到别的元素，因此一次遍历是绝对不行的。 考虑我们先进行一次遍历， 然后维护一个数组，第i项代表前i个元素（不包括i）的乘积。 然后我们反向遍历一次，然后维护另一个数组，同样是第i项代表前i个元素（不包括i）的乘积。


238.product-of-array-except-self
有意思的是第一个数组和第二个数组的反转（reverse）做乘法（有点像向量运算）就是我们想要的运算。

其实我们进一步观察，我们不需要真的创建第二个数组（第二个数组只是做中间运算使用），而是直接修改第一个数组即可。

关键点解析
两次遍历， 一次正向，一次反向。

维护一个数组，第i项代表前i个元素（不包括i）的乘积

 
复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# @lc code=end

