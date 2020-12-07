#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.85%)
# Likes:    850
# Dislikes: 0
# Total Accepted:    197K
# Total Submissions: 599.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
# 
#
中序遍历
这道题是让你验证一棵树是否为二叉查找树（BST）。 由于中序遍历的性质如果一个树遍历的结果是有序数组，那么他也是一个二叉查找树(BST), 我们只需要中序遍历，然后两两判断是否有逆序的元素对即可，如果有，则不是 BST，否则即为一个 BST。
定义法
根据定义，一个结点若是在根的左子树上，那它应该小于根结点的值而大于左子树最小值；若是在根的右子树上，那它应该大于根结点的值而小于右子树最大值。也就是说，每一个结点必须落在某个取值范围：
根结点的取值范围为（考虑某个结点为最大或最小整数的情况）：(long_min, long_max)
左子树的取值范围为：(current_min, root.value)
右子树的取值范围为：(root.value, current_max)
关键点解析
二叉树的基本操作（遍历）
中序遍历一个二叉查找树（BST）的结果是一个有序数组
如果一个树遍历的结果是有序数组，那么他也是一个二叉查找树(BST)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, area: tuple=(-float('inf'), float('inf'))) -> bool:
        """思路如上面的分析，用Python表达会非常直白
        :param root TreeNode 节点
        :param area tuple 取值区间
        """
        if root is None:
            return True

        is_valid_left = root.left is None or\
                   (root.left.val < root.val and area[0] < root.left.val < area[1])
        is_valid_right = root.right is None or\
                   (root.right.val > root.val and area[0] < root.right.val < area[1])

        # 左右节点都符合，说明本节点符合要求
        is_valid = is_valid_left and is_valid_right

        # 递归下去
        return is_valid\
            and self.isValidBST(root.left, (area[0], root.val))\
            and self.isValidBST(root.right, (root.val, area[1]))


​复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)

 

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
# @lc code=end

