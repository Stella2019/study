#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (66.30%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    76.7K
# Total Submissions: 115.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
# 
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
# 
# 计算从根到叶子节点生成的所有数字之和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
# 
# 示例 2:
# 
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
# 
#
递归
这是一道非常适合训练递归的题目。虽然题目不难，但是要想一次写正确，并且代码要足够优雅却不是很容易。
这里我们的思路是定一个递归的helper函数，用来帮助我们完成递归操作。 递归函数的功能是将它的左右子树相加，注意这里不包括这个节点本身，否则会多加， 我们其实关注的就是叶子节点的值，然后通过层层回溯到root，返回即可。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def helper(node, cur_val):
            if not node: return 0
            next_val = cur_val * 10 + node.val

            if not (node.left or node.right):
                return next_val

            left_val = helper(node.left, next_val)
            right_val = helper(node.right, next_val)

            return left_val + right_val

        return helper(root, 0)
复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)

拓展
通常来说，可以利用队列、栈等数据结构将递归算法转为递推算法。
描述
使用两个队列： 1. 当前和队列：保存上一层每个结点的当前和（比如49和40） 2. 结点队列：保存当前层所有的非空结点
每次循环按层处理结点队列。处理步骤： 1. 从结点队列取出一个结点 2. 从当前和队列将上一层对应的当前和取出来 3. 若左子树非空，则将该值乘以10加上左子树的值，并添加到当前和队列中 4. 若右子树非空，则将该值乘以10加上右子树的值，并添加到当前和队列中 5. 若左右子树均为空时，将该节点的当前和加到返回值中

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        result = 0
        node_queue, sum_queue = [root], [root.val]
        while node_queue:
            for i in node_queue:
                cur_node = node_queue.pop(0)
                cur_val = sum_queue.pop(0)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                    sum_queue.append(cur_val * 10 + cur_node.left.val)
                if cur_node.right:
                    node_queue.append(cur_node.right)
                    sum_queue.append(cur_val * 10 + cur_node.right.val)
                if not (cur_node.left or cur_node.right):
                    result += cur_val
        return result
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
# @lc code=end

