#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (60.23%)
# Likes:    282
# Dislikes: 0
# Total Accepted:    60.8K
# Total Submissions: 100.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例:
# 
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
# 
# 
#
思路
设定两个虚拟节点，dummyHead1 用来保存小于该值的链表，dummyHead2 来保存大于等于该值的链表
遍历整个原始链表，将小于该值的放于 dummyHead1 中，其余的放置在 dummyHead2 中
遍历结束后，将 dummyHead2 插入到 dummyHead1 后面
关键点解析
链表的基本操作（遍历）
虚拟节点 dummy 简化操作
遍历完成之后记得currentL1.next = null;否则会内存溢出
如果单纯的遍历是不需要上面操作的，但是我们的遍历会导致 currentL1.next 和 currentL2.next 中有且仅有一个不是 null， 如果不这么操作的话会导致两个链表成环，造成溢出。
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """在原链表操作，思路基本一致，只是通过指针进行区分而已"""
        # 在链表最前面设定一个初始node作为锚点，方便返回最后的结果
        first_node = ListNode(0)
        first_node.next = head
        # 设计三个指针，一个指向小于x的最后一个节点，即前后分离点
        # 一个指向当前遍历节点的前一个节点
        # 一个指向当前遍历的节点
        sep_node = first_node
        pre_node = first_node
        current_node = head

        while current_node is not None:
            if current_node.val < x:
                # 注意有可能出现前一个节点就是分离节点的情况
                if pre_node is sep_node:
                    pre_node = current_node
                    sep_node = current_node
                    current_node = current_node.next
                else:
                    # 这段次序比较烧脑
                    pre_node.next = current_node.next
                    current_node.next = sep_node.next
                    sep_node.next = current_node
                    sep_node = current_node
                    current_node = pre_node.next
            else:
                pre_node = current_node
                current_node = pre_node.next

        return first_node.next
时间复杂度：O(N)O(N)​

空间复杂度：O(1)O(1)
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
# @lc code=end

