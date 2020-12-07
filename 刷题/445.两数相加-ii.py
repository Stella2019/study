#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.09%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 97.3K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#
前置知识
链表

栈

 

思路
由于需要从低位开始加，然后进位。 因此可以采用栈来简化操作。 依次将两个链表的值分别入栈 stack1 和 stack2，然后相加入栈 stack，进位操作用一个变量 carried 记录即可。

最后根据 stack 生成最终的链表即可。

也可以先将两个链表逆置，然后相加，最后将结果再次逆置。

关键点解析
栈的基本操作

carried 变量记录进位

循环的终止条件设置成stack.length > 0 可以简化操作

注意特殊情况， 比如 1 + 99 = 100

 
 
Python Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def listToStack(l: ListNode) -> list:
            stack, c = [], l
            while c:
                stack.append(c.val)
                c = c.next
            return stack
​
        # transfer l1 and l2 into stacks
        stack1, stack2 = listToStack(l1), listToStack(l2)
​
        # add stack1 and stack2
        diff = abs(len(stack1) - len(stack2))
        stack1 = ([0]*diff + stack1 if len(stack1) < len(stack2) else stack1)
        stack2 = ([0]*diff + stack2 if len(stack2) < len(stack1) else stack2)
        stack3 = [x + y for x, y in zip(stack1, stack2)]
​
        # calculate carry for each item in stack3 and add one to the item before it
        carry = 0
        for i, val in enumerate(stack3[::-1]):
            index = len(stack3) - i - 1
            carry, stack3[index] = divmod(val + carry, 10)
            if carry and index == 0: 
                stack3 = [1] + stack3
            elif carry:
                stack3[index - 1] += 1
​
        # transfer stack3 to a linkedList
        result = ListNode(0)
        c = result
        for item in stack3:
            c.next = ListNode(item)
            c = c.next
​
        return result.next
复杂度分析

其中 M 和 N 分别为两个链表的长度。

时间复杂度：O(M + N)O(M+N)​

空间复杂度：O(M + N)O(M+N)
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
# @lc code=end

