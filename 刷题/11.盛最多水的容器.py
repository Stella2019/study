#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (64.49%)
# Likes:    2026
# Dislikes: 0
# Total Accepted:    328.9K
# Total Submissions: 509.9K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 示例 2：
# 
# 
# 输入：height = [1,1]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：height = [4,3,2,1,4]
# 输出：16
# 
# 
# 示例 4：
# 
# 
# 输入：height = [1,2,1]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# n = height.length
# 2 
# 0 


# 双指针

# 题目中说找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 ，因此符合直觉的解法就是固定两个端点，计算可以承载的水量， 然后不断更新最大值，最后返回最大值即可。这种算法，需要两层循环，时间复杂度是 。
#比如我们计算 n 面积的时候，假如左侧的线段高度比右侧的高度低，那么我们通过左移右指针来将长度缩短为 n - 1 的做法是没有意义的，因为新形成的面积变成了(n-1) * heightOfLeft， 这个面积一定比刚才的长度为 n 的面积 （n * heightOfLeft） 小。
#也就是说最大面积一定是当前的面积或者通过移动短的端点得到。
#复杂度分析
#时间复杂度：由于左右指针移动的次数加起来正好是 n， 因此时间复杂度为 n。
#空间复杂度：1。

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r =  0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return ans
# @lc code=end

