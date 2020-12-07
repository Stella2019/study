#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (68.60%)
# Likes:    755
# Dislikes: 0
# Total Accepted:    200.4K
# Total Submissions: 292K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 
# 
# 
#
"""设置一个 dummy 节点简化操作，dummy next 指向 head。
初始化 first 为第一个节点
初始化 second 为第二个节点
初始化 current 为 dummy
first.next = second.next
second.next = first
current.next = second
current 移动两格
重复"""
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        用递归实现链表相邻互换：
        第一个节点的 next 是第三、第四个节点交换的结果，第二个节点的 next 是第一个节点；
        第三个节点的 next 是第五、第六个节点交换的结果，第四个节点的 next 是第三个节点；
        以此类推
        :param ListNode head
        :return ListNode
        """
        # 如果为 None 或 next 为 None，则直接返回
        if not head or not head.next:
            return head

        _next = head.next
        head.next = self.swapPairs(_next.next)
        _next.next = head
        return _next
        
# @lc code=end
##复杂度分析
#时间复杂度：O(N)O(N)​
#空间复杂度：O(1)O(1)

Here, pre is the previous node. Since the head doesn’t have a previous node, I just use self instead. Again, a is the current node and b is the next node.
To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.


def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next
