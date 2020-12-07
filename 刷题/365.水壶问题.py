#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (35.30%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 78.7K
# Testcase Example:  '3\n5\n4'
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
# 
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
# 
# 你允许：
# 
# 
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 
# 
# 示例 1: (From the famous "Die Hard" example)
# 
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 
# 
# 示例 2:
# 
# 输入: x = 2, y = 6, z = 5
# 输出: False
# 
# 
#
前置知识
BFS
最大公约数
公司
阿里
百度
字节
思路
两个水壶的水我们考虑成状态，然后我们不断进行倒的操作，改变状态。那么初始状态就是（0 0） 目标状态就是 （any, z）或者 (z, any)，其中any 指的是任意升水。
已题目的例子，其过程示意图，其中括号表示其是由哪个状态转移过来的：
0 0 3 5(0 0) 3 0 (0 0 )0 5(0 0) 3 2(0 5) 0 3(0 0) 0 2(3 2) 2 0(0 2) 2 5(2 0) 3 4(2 5) bingo
代码
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        queue = [(0, 0)]
        seen = set((0, 0))

        while(len(queue) > 0):
            a, b = queue.pop(0)
            if a ==z or b == z or a + b == z:
                return True
            states = set()

            states.add((x, b))
            states.add((a, y))
            states.add((0, b))
            states.add((a, 0)) 
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) 
            states.add((0 if a + b < y else a - (y - b), min(b + a, y)))
            for state in states:
                if state in seen:
                    continue;
                queue.append(state)
                seen.add(state)
        return False
复杂度分析
时间复杂度：由于状态最多有 种，因此总的时间复杂度为O(x∗y)。
空间复杂度：O(x∗y)
我们使用了队列来存储状态，set 存储已经访问的元素，空间复杂度和状态数目一致，因此空间复杂度是。
上面的思路很直观，但是很遗憾这个算法在 LeetCode 的表现是 TLE(Time Limit Exceeded)。不过如果你能在真实面试中写出这样的算法，我相信大多数情况是可以过关的。
我们来看一下有没有别的解法。实际上，上面的算法就是一个标准的 BFS。如果从更深层次去看这道题，会发现这道题其实是一道纯数学问题，类似的纯数学问题在 LeetCode 中也会有一些，不过大多数这种题目，我们仍然可以采取其他方式 AC。那么让我们来看一下如何用数学的方式来解这个题。
数学法 - 最大公约数
思路
这是一道关于数论的题目，确切地说是关于裴蜀定理（英语：Bézout's identity）的题目。
摘自wiki的定义：
对任意两个整数 a、b，设 d是它们的最大公约数。那么关于未知数  x和  y的线性丢番图方程（称为裴蜀等式）：

ax+by=m

有整数解  (x,y) 当且仅当  m是  d的整数倍。裴蜀等式有解时必然有无穷多个解。
因此这道题可以完全转化为裴蜀定理。还是以题目给的例子x = 3, y = 5, z = 4，我们其实可以表示成3 * 3 - 1 * 5 = 4, 即3 * x - 1 * y = z。我们用a和b分别表示3 升的水壶和5升的水壶。那么我们可以：
倒满a（1）
将a倒到b
再次倒满a（2）
再次将a倒到b（a这个时候还剩下1升）
倒空b（-1）
将剩下的1升倒到b
将a倒满（3）
将a倒到b
b此时正好是4升
上面的过程就是3 * x - 1 * y = z的具体过程解释。
也就是说我们只需要求出x和y的最大公约数d，并判断z是否是d的整数倍即可。
代码
 
Python Code：
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        if (z == 0):
            return True

        if (x == 0):
            return y == z

        if (y == 0):
            return x == z

        def GCD(a, b):
            smaller = min(a, b)
            while smaller:
                if a % smaller == 0 and b % smaller == 0:
                    return smaller
                smaller -= 1

        return z % GCD(x, y) == 0
 
实际上求最大公约数还有更好的方式，比如辗转相除法：
def GCD(a, b):
    if b == 0: return a
    return GCD(b, a % b)
复杂度分析
时间复杂度：O(log(max(a,b)))
空间复杂度：空间复杂度取决于递归的深度，因此空间复杂度为 O(log(max(a,b)))
关键点分析
数论
裴蜀定理
# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
# @lc code=end

