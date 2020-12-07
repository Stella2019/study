#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.29%)
# Likes:    537
# Dislikes: 0
# Total Accepted:    124K
# Total Submissions: 199.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """与46题一样，当然也可以直接调用itertools的函数，然后去重"""
        return list(set(itertools.permutations(nums)))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """自己写回溯法，与46题相比，需要去重"""
        # 排序是为了去重
        nums.sort()
        res = []
        def _backtrace(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in range(len(nums)):
                    # 如果是同样的数字，则之前一定已经生成了对应可能
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    p_list = pre_list.copy()
                    p_list.append(nums[i])
                    left_nums = nums.copy()
                    left_nums.pop(i)
                    _backtrace(left_nums, p_list)
        _backtrace(nums, [])
        return res
# @lc code=end

