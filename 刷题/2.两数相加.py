#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (39.03%)
# Likes:    5337
# Dislikes: 0
# Total Accepted:    640.8K
# Total Submissions: 1.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 设立一个表示进位的变量 carried，建立一个新链表，把输入的两个链表从头往后同时处理，每两个相加，将结果加上 carried 后的值作为一个新节点到新链表后面，并更新 carried 值即可。
# 链表这种数据结构的特点和使用:用一个 carried 变量来实现进位的功能，每次相加之后计算 carried，并用于下一位的计算
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(0)
        head=res
        carry=0
        while l1 or l2 or carry!=0:
            sum=carry
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            # set value
            if sum<=9:
                res.val=sum
                carry=0
            else:
                res.val=sum%10
                carry=sum//10
            # creat new node
            if l1 or l2 or carry!=0:
                res.next=ListNode(0)
                res=res.next
        return head
        
        
# @lc code=end
#通过单链表的定义可以得知，单链表也是递归结构，因此，也可以使用递归的方式来进行 reverse 操作。算法
#将两个链表的第一个节点值相加，结果转为 0-10 之间的个位数，并设置进位信息
#将两个链表第一个节点以后的链表做带进位的递归相加
#将第一步得到的头节点的 next 指向第二步返回的链表
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if l1 == None and l2 == None and carry == 0:
            return None

        if l1 == None and l2 == None and carry == 1:
            return ListNode(1)

        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)

        l1.val, carry = (l1.val + l2.val + carry) % 10, (l1.val + l2.val + carry) // 10
        l1.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return l1



class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1, l2):
    return self.addTwoNumbersRecursive(l1, l2, 0)
    # return self.addTwoNumbersIterative(l1, l2)

  def addTwoNumbersRecursive(self, l1, l2, c):
    val = l1.val + l2.val + c
    c = val // 10
    ret = Node(val % 10)

    if l1.next != None or l2.next != None:
      if not l1.next:
        l1.next = Node(0)
      if not l2.next:
        l2.next = Node(0)
      ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
    elif c:
      ret.next = Node(c)
    return ret

  def addTwoNumbersIterative(self, l1, l2):
    a = l1
    b = l2
    c = 0
    ret = current = None

    while a or b:
      val = a.val + b.val + c
      c = val // 10
      if not current:
        ret = current = Node(val % 10)
      else:
        current.next = Node(val % 10)
        current = current.next

      if a.next or b.next:
        if not a.next:
          a.next = Node(0)
        if not b.next:
          b.next = Node(0)
      elif c:
        current.next = Node(c)
      a = a.next
      b = b.next
    return ret

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
  print(answer.val, end=' ')
  answer = answer.next
# 7 0 8

#我们发现，由于链表存储数字的顺序和常规的顺序相反，所以如果存在进位的情况，我们只需要在链表的结尾加上一个节点即可。通常的计算是从右往左，而在链表当中可以理解成从
#左往右，其实也就是按照链表遍历的顺序计算。这点想明白，并没有什么问题。
#我们做一个总结，难点大概有三个:
#1. 因为不是数组，所以我们无法拿到链表的长度。会出现两个链表长度不一致的情况 2. 返回结果也是一个链表，需要我们自己手动创建
#3. 计算产生的进位处理
#我们一个一个来分析，链表的长度未知很好处理，我们只需要判断当前节点的next节点是否 为空，就可以知道链表后面是否还有后继。如果没有，那么就说明链表已经遍历到头了。
#由于本题当中存在两个链表，我们需要同时判断它们是否结束:
 while(l1||l2){
if (l1) l1 = l1->next;
if (l2) l2 = l2->next;
}
#手动创建链表也并不复杂，我们首先创建一个链表的节点，然后依次往节点后方插入节点即 可。链表插入的方式也很简单，假设当前的节点是cur，待插入的节点是node，那么我们只 需要用cur.next指向node，然后将cur赋值成node即可，
1 cur->next=node; 2 cur=node;
#计算产生的进位问题就更简单了，由于我们是按位来计算加法，所以我们可以用一个变量标 记之前位是否发生进位。如果发生，那么当前的计算结果加一。因为加法计算，最多的结果 只能达到19(两位9再加上之前进位)，所以进位最多只会增加1。最后，再判断一下当前位 计算的结果是否产生进位即可。
intret=l1->val+l2->val; if(exceed)ret++; if(ret>9){
ret -= 10;
exceed = true; }elseexceed=false;