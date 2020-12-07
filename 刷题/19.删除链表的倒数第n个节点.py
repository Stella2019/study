#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (40.59%)
# Likes:    1137
# Dislikes: 0
# Total Accepted:    291.4K
# Total Submissions: 717.9K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 链表
# 双指针
#
"""这里我们可以使用双指针算法，不妨设为指针 A 和 指针 B。指针 A 先移动 n 次， 指针 B 再开始移动。当 A 到达 null 的时候， 指针 B 的位置正好是倒数第 n。这个时候将 B 的指针指向 B 的下下个指针即可完成删除工作。
算法：
设置虚拟节点 dummyHead 指向 head（简化判断，使得头结点不需要特殊判断）
设定双指针 p 和 q，初始都指向虚拟节点 dummyHead
移动 q，直到 p 与 q 之间相隔的元素个数为 n
同时移动 p 与 q，直到 q 指向的为 NULL
将 p 的下一个节点指向下下个节点"""
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
# @lc code=end
#复杂度分析
#时间复杂度：O(N)O(N)​
#空间复杂度：O(1)O(1)

My first solution is “cheating” a little. Instead of really removing the nth node, I remove the nth value. I recursively determine the indexes (counting from back), then shift the values for all indexes larger than n, and then always drop the head.


class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

Index and Remove - AC in 56 ms

In this solution I recursively determine the indexes again, but this time my helper function removes the nth node. It returns two values. The index, as in my first solution, and the possibly changed head of the remaining list.


class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

n ahead - AC in 48 ms

The standard solution, but without a dummy extra node. Instead, I simply handle the special case of removing the head right after the fast cursor got its head start.


class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head