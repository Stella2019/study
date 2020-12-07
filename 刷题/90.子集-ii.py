#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.47%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    58.4K
# Total Submissions: 95K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsetsWithDup(self, nums: List[int], sorted: bool=False) -> List[List[int]]:
        """回溯法，通过排序参数避免重复排序"""
        if not nums:
            return [[]]
        elif len(nums) == 1:
            return [[], nums]
        else:
            # 先排序，以便去重
            # 注意，这道题排序花的时间比较多
            # 因此，增加一个参数，使后续过程不用重复排序，可以大幅提高时间效率
            if not sorted:
                nums.sort()
            # 回溯法
            pre_lists = self.subsetsWithDup(nums[:-1], sorted=True)
            all_lists = [i+[nums[-1]] for i in pre_lists] + pre_lists
            # 去重
            result = []
            for i in all_lists:
                if i not in result:
                    result.append(i)
            return result
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
# @lc code=end

