#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (34.12%)
# Likes:    1097
# Dislikes: 0
# Total Accepted:    114.8K
# Total Submissions: 336.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#
前置知识
动态规划
暴力（超时）
 
思路
符合直觉的做法是：分别计算以 i 开头的 最长有效括号（i 从 0 到 n - 1·），从中取出最大的即可。
代码
代码支持： Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0

        def validCnt(start):
            # cnt 为 ) 的数量减去 ( 的数量
            cnt = 0
            ans = 0
            for i in range(start, n):
                if s[i] == '(':
                    cnt += 1
                if s[i] == ')':
                    cnt -= 1
                if cnt < 0:
                    return i - start
                if cnt == 0:
                    ans = max(ans, i - start + 1)
            return ans
        for i in range(n):
            ans = max(ans, validCnt(i))

        return ans
复杂度分析
时间复杂度：n
空间复杂度：n

栈
思路
主要思路和常规的括号解法一样，遇到'('入栈，遇到')'出栈，并计算两个括号之间的长度。 因为这个题存在非法括号对的情况且求是合法括号对的最大长度 所以有两个注意点是:
栈中存的是符号的下标
当栈为空时且当前扫描到的符号是')'时，需要将这个符号入栈作为分割符
栈中初始化一个 -1，作为分割符
代码
 
Python Code:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
复杂度分析
时间复杂度：n
空间复杂度：n


O(1) 空间
思路
我们可以采用解法一中的计数方法。
从左到右遍历一次，并分别记录左右括号的数量 left 和 right。
如果 right > left ，说明截止上次可以匹配的点到当前点这一段无法匹配，重置 left 和 right 为 0
如果 right == left, 此时可以匹配，此时有效括号长度为 left + right，我们获得一个局部最优解。如果其比全局最优解大，我们更新全局最优解
值得注意的是，对形如 (((() 这样的，更新全局最优解的逻辑永远无法执行。一种方式是再从右往左遍历一次即可，具体看代码。
类似的思想有哨兵元素，虚拟节点。只不过本题无法采用这种方法。
代码
代码支持：Java，Python
 
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = l = r = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if r > l:
                l = r = 0
        l = r = 0
        for c in s[::-1]:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if r < l:
                l = r = 0

        return ans


动态规划
思路
所有的动态规划问题, 首先需要解决的就是如何寻找合适的子问题. 该题需要我们找到最长的有效括号对, 我们首先想到的就是定义dp[i]为前 i 个字符串的最长有效括号对长度, 但是随后我们会发现, 这样的定义, 我们无法找到 dp[i]和 dp[i-1]的任何关系. 所以, 我们需要重新找一个新的定义: 定义dp[i]为以第 i 个字符结尾的最长有效括号对长度. 然后, 我们通过下面这个例子找一下 dp[i]和 dp[i-1]之间的关系.
s = '(())())'
从上面的例子我们可以观察出一下几点结论(描述中 i 为图中的 dp 数组的下标, 对应 s 的下标应为 i-1, 第 i 个字符的 i 从 1 开始).
base case: 空字符串的最长有效括号对长度肯定为 0, 即: dp[0] = 0;
s 的第1个字符结尾的最长有效括号对长度为 0, s 的第2个字符结尾的最长有效括号对长度也为 0, 这个时候我们可以得出结论: 最长有效括号对不可能以'('结尾, 即: dp[1] = d[2] = 0;
当 i 等于 3 时, 我们可以看出 dp[2]=0, dp[3]=2, 因为第 2 个字符(s[1])和第 3 个字符(s[2])是配对的;
当 i 等于 4 时, 我们可以看出 dp[3]=2, dp[4]=4, 因为我们配对的是第 1 个字符(s[0])和第 4 个字符(s[3]);
因此, 我们可以得出结论: 如果第i个字符和第i-1-dp[i-1]个字符是配对的, 则 dp[i] = dp[i-1] + 2, 其中: i-1-dp[i-1] >= 1, 因为第 0 个字符没有任何意义;
根据第 3 条规则来计算的话, 我们发现 dp[5]=0, dp[6]=2, 但是显然, dp[6]应该为 6 才对, 但是我们发现可以将"(())"和"()"进行拼接, 即: dp[i] += dp[i-dp[i]], 即: dp[6] = 2 + dp[6-2] = 2 + dp[4] = 6
根据以上规则, 我们求解 dp 数组的结果为: [0, 0, 0, 2, 4, 0, 6, 0], 其中最长有效括号对的长度为 6. 以下为图解: 
代码
Python Code:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mlen = 0
        slen = len(s)
        dp = [0] * (slen + 1)
        for i in range(1, len(s) + 1):
            # 有效的括号对不可能会以'('结尾的
            if s[i - 1] == '(':
                continue

            left_paren = i - 2 - dp[i - 1]
            if left_paren >= 0 and s[left_paren] == '(':
                dp[i] = dp[i - 1] + 2

                # 拼接有效括号对
                if dp[i - dp[i]]:
                    dp[i] += dp[i - dp[i]]

                # 更新最大有效扩对长度
                if dp[i] > mlen:
                    mlen = dp[i]

        return mlen
复杂度分析
时间复杂度：n
空间复杂度：n
关键点解析
第 3 点特征, 需要检查的字符是 s[i-1]和 s[i-2-dp[i-1]], 根据定义可知: i-1 >= dp[i-1], 但是 i-2 不一定大于 dp[i-1], 因此, 需要检查越界;
第 4 点特征最容易遗漏, 还有就是不需要检查越界, 因为根据定义可知: i >= dp[i], 所以 dp[i-dp[i]]的边界情况是 dp[0];
相关题目
20.valid-parentheses
扩展
如果判断的不仅仅只有'('和')', 还有'[', ']', '{'和'}', 该怎么办?
如果输出的不是长度, 而是任意一个最长有效括号对的字符串, 该怎么办?
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
# @lc code=end

