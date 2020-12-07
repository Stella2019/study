#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Medium (34.46%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 39.3K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
# 
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
# 
# 
# 
# 示例 1：
# 
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
# 
# 
# 示例 2：
# 
# 输入：a = "a", b = "aa"
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：a = "a", b = "a"
# 输出：1
# 
# 
# 示例 4：
# 
# 输入：a = "abc", b = "wxyz"
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a 和 b 由小写英文字母组成
# 
# 
#
前置知识
set
公司
暂无
思路
首先，一个容易发现的点是如果 b 中包含有 a 中没有的字符， 那么一定需要返回 - 1。因此使用集合存储 a 和 b 的所有字符，并比较 b 是否是 a 的子集，如果不是，则直接返回 - 1。
接着我们逐个尝试：
两个 a 是否可以？
三个 a 是否可以？
。。。
n 个 a 是否可以？
如果可以，则直接返回 n 即可。关于是否可以的判断， 我们可以使用任何语言自带的 indexof 算法，Python 中 可以使用 b in a 判读 b 时候是 a 的子串。
代码:
cnt = 1
while True:
    if b in a * cnt:
        return cnt
    cnt += 1
return -1
上面的代码有 BUG，会在一些情况无限循环。比如：
 a = "abcabcabcabc"
 b = "abac"
因此我们必须设计出口，并返回 -1。问题的我们的上界是什么呢？
这里有个概念叫解空间。这是一个很重要的概念。 我举个简单的例子。 你要在一个数组 A 中找某一个数的索引，题目保证这个数字一定在数组中存在。那么这道题的解空间就是[0, n -1]，其中 n 为数组长度。你的解不可能在这个范围外。
回到本题，如果 a 经过 n 次可以匹配成功， 那么最终 a 的长度范围是 [len(b), 2 * len(a) + len(b)]，下界是 len(b) 容易理解， 关键是上界。
还是以上面的例子来说。
 a = "abcabcabcabc"
 b = "abac"
abac 如果可以在其中匹配到，一定是以下几种情况：


临界情况就是：


因此最终 a 的长度的临界值就是 2 * len(a) + len(b)。超过这个范围再多次的叠加也没有意义。
关键点解析
答案是有限的， 搞清楚解空间是关键
代码
代码支持: Python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not set(b).issubset(set(a)):
            return -1
        cnt = 1
        while len(a * cnt) < 2 * len(a) + len(b):
            if b in a * cnt:
                return cnt
            cnt += 1
        return -1
复杂度分析
时间复杂度：b in a 的时间复杂度为 M + N（取决于内部算法），因此总的时间复杂度为 O((M+N) 
2
 )，其中 M 和 N 为 a 和 b 的长度。
空间复杂度：由于使用了 set，因此空间复杂度为(M+N ，其中 M 和 N 为 a 和 b 的长度。
# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
# @lc code=end

