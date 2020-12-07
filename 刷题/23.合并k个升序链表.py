#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (53.71%)
# Likes:    1031
# Dislikes: 0
# Total Accepted:    192.7K
# Total Submissions: 358.6K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#
前置知识
链表
归并排序
 
思路
这道题目是合并 k 个已排序的链表，号称 leetcode 目前最难的链表题。 和之前我们解决的88.merge-sorted-array很像。 他们有两点区别：
这道题的数据结构是链表，那道是数组。这个其实不复杂，毕竟都是线性的数据结构。
这道题需要合并 k 个元素，那道则只需要合并两个。这个是两题的关键差别，也是这道题难度为hard的原因。
因此我们可以看出，这道题目是88.merge-sorted-array的进阶版本。其实思路也有点像，我们来具体分析下第二条。 如果你熟悉合并排序的话，你会发现它就是合并排序的一部分。
具体我们可以来看一个动画

（动画来自 https://zhuanlan.zhihu.com/p/61796021 ）
关键点解析
分治
归并排序(merge sort)
代码
 
Python3 Code：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        # basic cases
        if lenth == 0: return None
        if lenth == 1: return lists[0]
        if lenth == 2: return self.mergeTwoLists(lists[0], lists[1])

        # divide and conqure if not basic cases
        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:n]))


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        c1, c2, c3 = l1, l2, res
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                c3 = c3.next
            elif c1:
                c3.next = c1
                break
            else:
                c3.next = c2
                break

        return res.next
复杂度分析
时间复杂度：
空间复杂度：
相关题目
88.merge-sorted-array

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
# @lc code=end

