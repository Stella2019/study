#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.56%)
# Likes:    370
# Dislikes: 0
# Total Accepted:    76.1K
# Total Submissions: 117.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
# 
#
前置知识
队列
 
思路
这道题和 leetcode 102 号问题《102.binary-tree-level-order-traversal》很像
这道题可以借助队列实现，首先把 root 入队，然后入队一个特殊元素 Null(来表示每层的结束)。
然后就是 while(queue.length), 每次处理一个节点，都将其子节点（在这里是 left 和 right）放到队列中。
然后不断的出队， 如果出队的是 null，则表式这一层已经结束了，我们就继续 push 一个 null。
关键点解析
队列
队列中用 Null(一个特殊元素)来划分每层
树的基本操作- 遍历 - 层次遍历（BFS）
二叉树的右视图可以看作是层次遍历每次只取每一层的最右边的元素

假如题目变成求二叉树的左视图呢？
很简单我们只需要取 queue 的最后一个元素即可。 或者存的时候反着来也行
其实我们没必要存储 levelNodes，而是只存储每一层最右的元素，这样空间复杂度就不是 n 了， 就是 logn 了。
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
# @lc code=end

