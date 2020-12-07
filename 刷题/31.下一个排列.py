#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (36.19%)
# Likes:    859
# Dislikes: 0
# Total Accepted:    123.5K
# Total Submissions: 340.7K
# Testcase Example:  '[1,2,3]'
#
# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须 原地 修改，只允许使用额外常数空间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 回溯法
# 
#
"""符合直觉的方法是按顺序求出所有的排列，如果当前排列等于 nums，那么我直接取下一个但是这种做法不符合 constant space 要求（题目要求直接修改原数组）,时间复杂度也太高，为 O(n!),肯定不是合适的解。
这种题目比较抽象，写几个例子通常会帮助理解问题的规律。我找了几个例子，其中蓝色背景表示的是当前数字找下一个更大排列的时候需要改变的元素.
我们不难发现，蓝色的数字都是从后往前第一个不递增的元素，并且我们的下一个更大的排列 只需要改变蓝色的以及之后部分即可，前面的不需要变。

那么怎么改变蓝色的以及后面部分呢？为了使增量最小， 由于前面我们观察发现，其实剩下的元素从左到右是递减的，而我们想要变成递增的，我们只需要不断交换首尾元素即可。

另外我们也可以以回溯的角度来思考这个问题，让我们先回溯一次：

"""
# @lc code=start
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :param list nums
        """
        # 第一步，从后往前，找到下降点
        down_index = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                down_index = i
                break
        # 如果没有下降点，重新排列
        if down_index is None:
            nums.reverse()
        # 如果有下降点
        else:
            # 第二步，从后往前，找到比下降点大的数，对换位置
            for i in range(len(nums)-1, i, -1):
                if nums[down_index] < nums[i]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            # 第三步，重新排列下降点之后的数
            i, j = down_index+1, len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
# @lc code=end

