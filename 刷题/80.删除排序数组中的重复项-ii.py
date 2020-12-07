#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (56.64%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    68K
# Total Submissions: 119.9K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# 给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 
# 
# 
# 说明：
# 
# 为什么返回数值是整数，但输出的答案是数组呢？
# 
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 
# 你可以想象内部操作如下：
# 
# 
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1,2,2,3]
# 输出：5, nums = [1,1,2,2,3]
# 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,1,1,1,1,2,3,3]
# 输出：7, nums = [0,0,1,1,2,3,3]
# 解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^4 
# nums 按递增顺序排列
# 
# 
#双指针
思路
”删除排序“类题目截止到现在（2020-1-15）一共有四道题：
26,80,82,83
这道题是26.remove-duplicates-from-sorted-array 的进阶版本，唯一的不同是不再是全部元素唯一，而是全部元素不超过 2 次。实际上这种问题可以更抽象一步，即“删除排序数组中的重复项，使得相同数字最多出现 k 次” 。 那么这道题 k 就是 2， 26.remove-duplicates-from-sorted-array 的 k 就是 1。
上一题我们使用了快慢指针来实现，这道题也是一样，只不过逻辑稍有不同。 其实快慢指针本质是读写指针，在这里我们的快指针实际上就是读指针，而慢指针恰好相当于写指针。”快慢指针的说法“便于描述和记忆，“读写指针”的说法更便于理解本质。本文中，以下内容均描述为快慢指针。
初始化快慢指针 slow ， fast ，全部指向索引为 0 的元素。
fast 每次移动一格
慢指针选择性移动，即只有写入数据之后才移动。是否写入数据取决于 slow - 2 对应的数字和 fast 对应的数字是否一致。
如果一致，我们不应该写。 否则我们就得到了三个相同的数字，不符合题意
如果不一致，我们需要将 fast 指针的数据写入到 slow 指针。
重复这个过程，直到 fast 走到头，说明我们已无数字可写。
图解（红色的两个数字，表示我们需要比较的两个数字）：


关键点分析
快慢指针
读写指针
删除排序问题

时间复杂度：O(N)O(N)​

空间复杂度：O(1)O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 写指针
        i = 0
        K = 2
        for num in nums:
            if i < K or num != nums[i-K]:
                nums[i] = num
                i += 1
        return i
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# @lc code=end

