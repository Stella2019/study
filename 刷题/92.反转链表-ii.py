#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.81%)
# Likes:    594
# Dislikes: 0
# Total Accepted:    88.7K
# Total Submissions: 171.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#
思路（四点法）
这道题和206.reverse-linked-list 有点类似，并且这道题是 206 的升级版。 让我们反转某一个区间，而不是整个链表，我们可以将 206 看作本题的特殊情况（special case）。
核心在于取出需要反转的这一小段链表，反转完后再插入到原先的链表中。
以本题为例：
反转的是 2,3,4 这三个点，那么我们可以先取出 2，用 cur 指针指向 2，然后当取出 3 的时候，我们将 3 指向 2 的，把 cur 指针前移到 3，依次类推，到 4 后停止，这样我们得到一个新链表 4->3->2, cur 指针指向 4。
对于原链表来说，有两个点的位置很重要，需要用指针记录下来，分别是 1 和 5，把新链表插入的时候需要这两个点的位置。用 pre 指针记录 1 的位置当 4 结点被取走后，5 的位置需要记下来
这样我们就可以把反转后的那一小段链表加入到原链表中

(图片来自网络)
首先我们直接返回 head 是不行的。 当 m 不等于 1 的时候是没有问题的，但只要 m 为 1，就会有问题。
其次如果链表商都小于 4 的时候，p1，p2，p3，p4 就有可能为空。为了防止 NPE，我们也要充分地判空。
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        cur = head
        i = 0
        p1 = p2 = p3 = p4 = None
        # 一坨逻辑
        if p1:
            p1.next = p3
        else:
            dummy.next = p3
        if p2:
            p2.next = p4
        return head
如上代码是不可以的，我们考虑使用 dummy 节点。
class Solution:
   def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
       pre = None
       cur = head
       i = 0
       p1 = p2 = p3 = p4 = None
       dummy = ListNode(0)
       dummy.next = head
       # 一坨逻辑
       if p1:
           p1.next = p3
       else:
           dummy.next = p3
       if p2:
           p2.next = p4

       return dummy.next
关于链表反转部分, 顺序比较重要，我们需要：
先 cur.next = pre
再 更新 p2 和 p2.next(其中要设置 p2.next = None，否则会互相应用，造成无限循环)
最后更新 pre 和 cur
上述的顺序不能错，不然会有问题。原因就在于p2.next = None，如果这个放在最后，那么我们的 cur 会提前断开。
    while cur:
           i += 1
           if i == m - 1:
               p1 = cur
           next = cur.next
           if m < i <= n:
               cur.next = pre

           if i == m:
               p2 = cur
               p2.next = None

           if i == n:
               p3 = cur

           if i == n + 1:
               p4 = cur

           pre = cur
           cur = next
关键点解析
四点法
链表的基本操作
考虑特殊情况 m 是 1 或者 n 是链表长度的情况，我们可以采用虚拟节点 dummy 简化操作
用四个变量记录特殊节点， 然后操作这四个节点使之按照一定方式连接即可。
注意更新 current 和 pre 的位置， 否则有可能出现溢出

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head.next or n == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = None
        cur = head
        i = 0
        p1 = p2 = p3 = p4 = None
        while cur:
            i += 1
            next = cur.next
            if m < i <= n:
                cur.next = pre
            if i == m - 1:
                p1 = cur
            if i == m:
                p2 = cur
            if i == n:
                p3 = cur
            if i == n + 1:
                p4 = cur
            pre = cur
            cur = next
        if not p1:
            dummy.next = p3
        else:
            p1.next = p3
        p2.next = p4
        return dummy.next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
# @lc code=end

复杂度分析

时间复杂度：O(N)O(N)​

空间复杂度：O(1)O(1)