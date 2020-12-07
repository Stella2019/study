# @before-stub-for-debug-begin
from python3problem904 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
# https://leetcode-cn.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.23%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 21.4K
# Testcase Example:  '[1,2,1]'
#
# 在一排树中，第 i 棵树产生 tree[i] 型的水果。
# 你可以从你选择的任何树开始，然后重复执行以下步骤：
# 
# 
# 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
# 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
# 
# 
# 请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
# 
# 你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
# 
# 用这个程序你能收集的水果树的最大总量是多少？
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,1]
# 输出：3
# 解释：我们可以收集 [1,2,1]。
# 
# 
# 示例 2：
# 
# 输入：[0,1,2,2]
# 输出：3
# 解释：我们可以收集 [1,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
# 
# 
# 示例 3：
# 
# 输入：[1,2,3,2,2]
# 输出：4
# 解释：我们可以收集 [2,3,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
# 
# 
# 示例 4：
# 
# 输入：[3,3,3,1,2,1,1,2,3,3,4]
# 输出：5
# 解释：我们可以收集 [1,2,1,1,2]
# 如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
# 
# 思路
#问题可以抽象为给定一个数组，求解最多选择两种数字的情况下，最大的连续子序列长度，其中数组和原题目一样，每一个数字代表一个水果。
# 我们可以使用滑动窗口来解决。 思路和 【1004. 最大连续 1 的个数 III】滑动窗口（Python3） 一样。

#复杂度分析
#时间复杂度：O(N)
#空间复杂度：O(N)

# @lc code=start
class Solution:
    def atMostK(self, nums, K):
        counter = collections.Counter()
        res = i = 0
        for j in range(len(nums)):
            if counter[nums[j]] == 0:
                K -= 1
            counter[nums[j]] += 1
            while K < 0:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    K += 1
                i += 1
            res = max(res, j - i + 1)
        return res

    def totalFruit(self, tree: List[int]) -> int:
        return self.atMostK(tree, 2)

 

        
# @lc code=end

