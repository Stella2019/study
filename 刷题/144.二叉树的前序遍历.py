#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (68.65%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    233.9K
# Total Submissions: 340.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
# 输出：[1,2]
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
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#
前置知识
递归
栈
 
这道题目是前序遍历，这个和之前的leetcode 94 号问题 - 中序遍历完全不一回事。
前序遍历是根左右的顺序，注意是根开始，那么就很简单。直接先将根节点入栈，然后 看有没有右节点，有则入栈，再看有没有左节点，有则入栈。 然后出栈一个元素，重复即可。
其他树的非递归遍历可没这么简单

（迭代 VS 递归）
关键点解析
二叉树的基本操作（遍历）
不同的遍历算法差异还是蛮大的
如果非递归的话利用栈来简化操作
如果数据规模不大的话，建议使用递归
递归的问题需要注意两点，一个是终止条件，一个如何缩小规模
终止条件，自然是当前这个元素是 null（链表也是一样）
由于二叉树本身就是一个递归结构， 每次处理一个子树其实就是缩小了规模， 难点在于如何合并结果，这里的合并结果其实就是mid.concat(left).concat(right), mid 是一个具体的节点，left 和 right递归求出即可
复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(N)O(N)

def preorderTraversal(self, root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ret.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ret
    
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
# @lc code=end

