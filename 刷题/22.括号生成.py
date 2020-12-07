#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.50%)
# Likes:    1454
# Dislikes: 0
# Total Accepted:    204.9K
# Total Submissions: 267.8K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#DFS
#回溯法
"""本题是 20. 有效括号 的升级版。
由于我们需要求解所有的可能， 因此回溯就不难想到。回溯的思路和写法相对比较固定，并且回溯的优化手段大多是剪枝。
不难想到， 如果左括号的数目小于右括号，我们可以提前退出，这就是这道题的剪枝。 比如 ())....，后面就不用看了，直接退出即可。回溯的退出条件也不难想到，那就是：
左括号数目等于右括号数目
左括号数目 + 右括号数目 = 2 * n
由于我们需要剪枝， 因此必须从左开始遍历。（WHY？）
因此这道题我们可以使用深度优先搜索(回溯思想)，从空字符串开始构造，做加法， 即 dfs(左括号数, 右括号数目, 路径)， 我们从 dfs(0, 0, '') 开始。"""

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l, r, s):
            if l > n or r > n: return
            if (l == r == n): res.append(s)
            if l < r: return
            # 加一个左括号
            dfs(l + 1, r, s + '(')
            # 加一个右括号
            dfs(l, r + 1, s + ')')
        dfs(0, 0, '')
        return res
# @lc code=end
#时间复杂度：O(2^N)
#空间复杂度：O(2^N)
p is the parenthesis-string built so far, left and right tell the number of left and right parentheses still to add, and parens collects the parentheses.

Solution 1

I used a few “tricks”… how many can you find? :-)


def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)

Solution 2

Here I wrote an actual Python generator. I allow myself to put the yield q at the end of the line because it’s not that bad and because in “real life” I use Python 3 where I just say yield from generate(...).


def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))

Solution 3

Improved version of this. Parameter open tells the number of “already opened” parentheses, and I continue the recursion as long as I still have to open parentheses (n > 0) and I haven’t made a mistake yet (open >= 0).


def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)