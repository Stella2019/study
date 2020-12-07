#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.19%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    81.8K
# Total Submissions: 148.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
# 
# 
#
这道题可以借助队列实现，首先把root入队，然后入队一个特殊元素Null(来表示每层的结束)。
然后就是while(queue.length), 每次处理一个节点，都将其子节点（在这里是left和right）放到队列中。
然后不断的出队， 如果出队的是null，则表式这一层已经结束了，我们就继续push一个null。
关键点解析
队列
队列中用Null(一个特殊元素)来划分每层
树的基本操作- 遍历 - 层次遍历（BFS）
拓展
由于二叉树是递归结构，因此，可以采用递归的方式来处理。在递归时需要保留当前的层次信息（从0开始），作为参数传递给下一次递归调用。
描述
当前层次为偶数时，将当前节点放到当前层的结果数组尾部
当前层次为奇数时，将当前节点放到当前层的结果数组头部
递归对左子树进行之字形遍历，层数参数为当前层数+1
递归对右子树进行之字形遍历，层数参数为当前层数+1
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
# @lc code=end

