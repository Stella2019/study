#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (60.67%)
# Likes:    660
# Dislikes: 0
# Total Accepted:    76.5K
# Total Submissions: 126K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
# 
# 示例 1:
# 
# 输入: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 
# 示例 2:
# 
# 输入: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
# 
# 
#
前置知识
二叉树
动态规划
 
思路
和 198.house-robber 类似，这道题也是相同的思路。 只不过数据结构从数组换成了树。
我们仍然是对每一项进行决策：如果我抢的话，所得到的最大价值是多少。如果我不抢的话，所得到的最大价值是多少。
遍历二叉树，都每一个节点我们都需要判断抢还是不抢。
如果抢了的话， 那么我们不能继续抢其左右子节点
如果不抢的话，那么我们可以继续抢左右子节点，当然也可以不抢。抢不抢取决于哪个价值更大。
抢不抢取决于哪个价值更大。
这是一个明显的递归问题，我们使用递归来解决。由于没有重复子问题，因此没有必要 cache ，也没有必要动态规划。
关键点
对每一个节点都分析，是抢还是不抢
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            [l_rob, l_not_rob] = dfs(node.left)
            [r_rob, r_not_rob] = dfs(node.right)
            return [node.val + l_not_rob + r_not_rob, max([l_rob, l_not_rob]) +  max([r_rob, r_not_rob])]
        return max(dfs(root))

复杂度分析
时间复杂度：n，其中 N 为树的节点个数。
空间复杂度：h，其中 h 为树的高度。
# @lc code=end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
# @lc code=end

