#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (79.28%)
# Likes:    900
# Dislikes: 0
# Total Accepted:    175.7K
# Total Submissions: 221.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    def subsets(self, nums):
        self.res = []
        self.track = []
        self.backtrack(nums, 0, self.track)

        return self.res

    def backtrack(self, nums, start, track):
        # 注意深拷贝
        self.res.append(list(self.track))
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 回溯
            self.backtrack(nums, i+1, self.track)
            # 撤销选择
            self.track.pop()
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
# @lc code=end

