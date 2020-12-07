#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (53.34%)
# Likes:    1852
# Dislikes: 0
# Total Accepted:    171.6K
# Total Submissions: 321.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 0 
# 0 
# 
# 
#
前置知识
空间换时间
双指针
单调栈
 
双数组
思路
这是一道雨水收集的问题， 难度为hard. 如图所示，让我们求下过雨之后最多可以积攒多少的水。
如果采用暴力求解的话，思路应该是 height 数组依次求和，然后相加。
伪代码
for (let i = 0; i < height.length; i++) {
  area += (h[i] - height[i]) * 1; // h为下雨之后的水位
}
问题转化为求 h，那么 h[i]又等于左右两侧柱子的最大值中的较小值，即 h[i] = Math.min(左边柱子最大值, 右边柱子最大值)
如上图那么 h 为 [0, 1, 1, 2, 2, 2 ,2, 3, 2, 2, 2, 1]
问题的关键在于求解左边柱子最大值和右边柱子最大值, 我们其实可以用两个数组来表示leftMax, rightMax， 以 leftMax 为例，leftMax[i]代表 i 的左侧柱子的最大值，因此我们维护两个数组即可。
关键点解析
建模 h[i] = Math.min(左边柱子最大值, 右边柱子最大值)(h 为下雨之后的水位)
代码
代码支持: JS, Python3, C++:
 
Python Code:
class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(1, len(heights) + 1):
            l[i] = max(l[i - 1], heights[i - 1])
        for i in range(len(heights) - 1, 0, -1):
            r[i] = max(r[i + 1], heights[i])
        for i in range(len(heights)):
            ans += max(0, min(l[i + 1], r[i]) - heights[i])
        return ans
 
复杂度分析
时间复杂度：n
空间复杂度：n



双指针
思路
上面代码比较好理解，但是需要额外的 N 的空间。从上面解法可以看出，我们实际上只关心左右两侧较小的那一个，并不需要两者都计算出来。具体来说：
如果 l[i + 1] < r[i] 那么 最终积水的高度由 i 的左侧最大值决定。
如果 l[i + 1] >= r[i] 那么 最终积水的高度由 i 的右侧最大值决定。
因此我们不必维护完整的两个数组，而是可以只进行一次遍历，同时维护左侧最大值和右侧最大值，使用常数变量完成即可。这是一个典型的双指针问题，
具体算法：
维护两个指针 left 和 right，分别指向头尾。
初始化左侧和右侧最高的高度都为 0。
比较 height[left] 和 height[right]
3.1 如果 height[left] < height[right]
3.1.1 如果 height[left] >= left_max， 则当前格子积水面积为(left_max - height[left])
3.1.2 否则无法积水，即积水面积为 0
3.2 左指针右移一位
3.3 如果 height[left] >= height[right]
3.3.1 如果 height[right] >= right_max， 则当前格子积水面积为(right_max - height[right])
3.3.2 否则无法积水，即积水面积为 0
3.4 右指针左移一位
代码
代码支持: Python, C++, Go, PHP:
Python Code:
class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l_max = r_max = 0
        l, r = 0, n - 1
        ans = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] < l_max:
                    ans += l_max - heights[l]
                else:
                    l_max = heights[l]
                l += 1
            else:
                if heights[r] < r_max:
                    ans += r_max - heights[r]
                else:
                    r_max = heights[r]
                r -= 1
        return ans
 
复杂度分析
时间复杂度：n
空间复杂度：1
相关题目
84.largest-rectangle-in-histogram
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
# @lc code=end

