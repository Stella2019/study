#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (56.95%)
# Likes:    721
# Dislikes: 0
# Total Accepted:    155.3K
# Total Submissions: 272.7K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 
# 
# 进阶：
# 
# 
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[0]
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
# n == nums.length
# 1 
# nums[i] 为 0、1 或 2
# 
# 
#
解法一 - 计数排序
遍历数组，统计红白蓝三色球（0，1，2）的个数
根据红白蓝三色球（0，1，2）的个数重排数组
这种思路的时间复杂度：，需要遍历数组两次（Two pass）。
解法二 - 挡板法
我们可以把数组分成三部分，前部（全部是 0），中部（全部是 1）和后部（全部是 2）三个部分。每一个元素（红白蓝分别对应 0、1、2）必属于其中之一。将前部和后部各排在数组的前边和后边，中部自然就排好了。
我们用三个指针，设置两个指针 begin 指向前部的末尾的下一个元素（刚开始默认前部无 0，所以指向第一个位置），end 指向后部开头的前一个位置（刚开始默认后部无 2，所以指向最后一个位置），然后设置一个遍历指针 current，从头开始进行遍历。
形象地来说地话就是有两个挡板，这两个挡板实现我们不知道，我们的目标就是移动挡板到合适位置，并且使得挡板每一部分都是合适的颜色。
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = cur = 0
        p2 = len(nums) - 1

        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
时间复杂度：O(N)O(N)​

空间复杂度：O(1)O(1)
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

