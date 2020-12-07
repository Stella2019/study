#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (71.86%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 34.7K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
# 
# 示例 1:
# 
# 
# 输入:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# 输出:
# 1
# 
# 
# 
# 
# 示例 2: 
# 
# 
# 输入:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# 输出:
# 7
# 
# 
# 
# 
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
# 
#
BFS
思路
其实问题本身就告诉你怎么做了
在树的最后一行找到最左边的值。
问题再分解一下
找到树的最后一行
找到那一行的第一个节点
不用层序遍历简直对不起这个问题，这里贴一下层序遍历的流程
令curLevel为第一层节点也就是root节点
定义nextLevel为下层节点
遍历node in curLevel,
  nextLevel.push(node.left)
  nextLevel.push(node.right)
令curLevel = nextLevel, 重复以上流程直到curLevel为空
 
Python Code:
class Solution(object):
    def findBottomLeftValue(self, root):
        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            res = queue[0].val
            for _ in range(length):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
 
 
复杂度分析
时间复杂度：n，其中 N 为树的节点数。
空间复杂度：q，其中 Q 为队列长度，最坏的情况是满二叉树，此时和 N 同阶，其中 N 为树的节点总数
DFS
思路
树的最后一行找到最左边的值，转化一下就是找第一个出现的深度最大的节点，这里用先序遍历去做，其实中序遍历也可以，只需要保证左节点在右节点前被处理即可。 具体算法为，先序遍历 root，维护一个最大深度的变量，记录每个节点的深度，如果当前节点深度比最大深度要大，则更新最大深度和结果项。
 
Python Code:
class Solution(object):

    def __init__(self):
        self.res = 0
        self.max_level = 0

    def findBottomLeftValue(self, root):
        self.res = root.val
        def dfs(root, level):
            if not root:
                return
            if level > self.max_level:
                self.res = root.val
                self.max_level = level
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)

        return self.res
 
 
复杂度分析
时间复杂度：n，其中 N 为树的节点总数。
空间复杂度：h，其中 h 为树的高度。
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
# @lc code=end

