#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (74.27%)
# Likes:    794
# Dislikes: 0
# Total Accepted:    310K
# Total Submissions: 417.3K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
思路
递归的方式相对简单，非递归的方式借助栈这种数据结构实现起来会相对轻松。
如果采用非递归，可以用栈(Stack)的思路来处理问题。
中序遍历的顺序为左-根-右，具体算法为：
从根节点开始，先将根节点压入栈
然后再将其所有左子结点压入栈，取出栈顶节点，保存节点值
再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中， 重复上步骤

关键点解析
二叉树的基本操作（遍历）
不同的遍历算法差异还是蛮大的
如果非递归的话利用栈来简化操作
如果数据规模不大的话，建议使用递归
递归的问题需要注意两点，一个是终止条件，一个如何缩小规模
终止条件，自然是当前这个元素是 null（链表也是一样）
由于二叉树本身就是一个递归结构， 每次处理一个子树其实就是缩小了规模， 难点在于如何合并结果，这里的合并结果其实就是left.concat(mid).concat(right), mid 是一个具体的节点，left 和 right递归求出即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        1. 递归法可以一行代码完成，无需讨论；
        2. 迭代法一般需要通过一个栈保存节点顺序，我们这里直接使用列表
          - 首先，我要按照中序遍历的顺序存入栈，这边用的逆序，方便从尾部开始处理
          - 在存入栈时加入一个是否需要深化的参数
          - 在回头取值时，这个参数应该是否，即直接取值
          - 简单调整顺序，即可实现前序和后序遍历
        """
        # 递归法
        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)\
        #     + [root.val]\
        #     + self.inorderTraversal(root.right)
        # 迭代法
        result = []
        stack = [(1, root)]
        while stack:
            go_deeper, node = stack.pop()
            if node is None:
                continue
            if go_deeper:
                # 左右节点还需继续深化，并且入栈是先右后左
                stack.append((1, node.right))
                # 节点自身已遍历，回头可以直接取值
                stack.append((0, node))
                stack.append((1, node.left))
            else:
                result.append(node.val)
        return result
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
# @lc code=end

