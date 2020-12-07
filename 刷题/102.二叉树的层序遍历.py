#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.75%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    224.5K
# Total Submissions: 352K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
队列
思路
这是一个典型的二叉树遍历问题， 关于二叉树遍历，我总结了一个专题，大家可以先去看下那个，然后再来刷这道题。
这道题可以借助队列实现，首先把root入队，然后入队一个特殊元素Null(来表示每层的结束)。
然后就是while(queue.length), 每次处理一个节点，都将其子节点（在这里是left和right）放到队列中。
然后不断的出队， 如果出队的是null，则表式这一层已经结束了，我们就继续push一个null。
如果不入队特殊元素Null来表示每层的结束，则在while循环开始时保存当前队列的长度，以保证每次只遍历一层（参考下面的C++ Code）。
如果采用递归方式，则需要将当前节点，当前所在的level以及结果数组传递给递归函数。在递归函数中，取出节点的值，添加到level参数对应结果数组元素中（参考下面的C++ Code 或 Python Code）。
关键点解析
队列
队列中用Null(一个特殊元素)来划分每层
树的基本操作- 遍历 - 层次遍历（BFS）
注意塞入null的时候，判断一下当前队列是否为空，不然会无限循环
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """递归法"""
        if root is None:
            return []

        result = []

        def add_to_result(level, node):
            """递归函数
            :param level int 当前在二叉树的层次
            :param node TreeNode 当前节点
            """
            if level > len(result) - 1:
                result.append([])

            result[level].append(node.val)
            if node.left:
                add_to_result(level+1, node.left)
            if node.right:
                add_to_result(level+1, node.right)

        add_to_result(0, root)
        return result
复杂度分析
时间复杂度：n，其中N为树中节点总数。
空间复杂度：n，其中N为树中节点总数。
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
# @lc code=end

