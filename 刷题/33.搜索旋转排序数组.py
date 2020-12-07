#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.72%)
# Likes:    1086
# Dislikes: 0
# Total Accepted:    196.9K
# Total Submissions: 495.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 给你一个整数数组 nums ，和一个整数 target 。
# 
# 该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]
# ）。
# 
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4 
# 
# 
#二分法
"""
首先要知道，我们随便选择一个点，将数组分为前后两部分，其中一部分一定是有序的。
具体步骤：
我们可以先找出mid，然后根据mid来判断，mid是在有序的部分还是无序的部分
假如mid小于start，则mid一定在右边有序部分。 假如mid大于等于start， 则mid一定在左边有序部分。
注意等号的考虑
然后我们继续判断target在哪一部分， 我们就可以舍弃另一部分了
我们只需要比较target和有序部分的边界关系就行了。 比如mid在右侧有序部分，即[mid, end] 那么我们只需要判断 target >= mid && target <= end 就能知道target在右侧有序部分，我们就 可以舍弃左边部分了(start = mid + 1)， 反之亦然。"""

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """用二分法，先判断左右两边哪一边是有序的，再判断是否在有序的列表之内"""
        if len(nums) <= 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            # 如果中间的值大于最左边的值，说明左边有序
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    # 这里 +1，因为上面是 <= 符号
                    left = mid + 1
            # 否则右边有序
            else:
                # 注意：这里必须是 mid+1，因为根据我们的比较方式，mid属于左边的序列
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return left if nums[left] == target else -1
# @lc code=end

#复杂度分析

#时间复杂度：O(logN)O(logN)​

#空间复杂度：O(1)O(1)