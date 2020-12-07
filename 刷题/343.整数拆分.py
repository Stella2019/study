#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (58.91%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    68.4K
# Total Submissions: 116.1K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#
递归
动态规划
抽象
首先看到这道题，自然而然地先对问题进行抽象，这种抽象能力是必须的。LeetCode 实际上有很多这种穿着华丽外表的题，当你把这个衣服扒开的时候，会发现都是差不多的，甚至两个是一样的，这样的例子实际上有很多。 就本题来说，就有一个剑指 Offer 的原题《剪绳子》和其本质一样，只是换了描述方式。类似的有力扣 137 和 645 等等，大家可以自己去归纳总结。
137 和 645 我贴个之前写的题解 https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-3/
培养自己抽象问题的能力，不管是在算法上还是工程上。 务必记住这句话！
数学是一门非常抽象的学科，同时也很方便我们抽象问题。为了显得我的题解比较高级，引入一些你们看不懂的数学符号也是很有必要的（开玩笑，没有什么高级数学符号啦）。
实际上这道题可以用纯数学角度来解，但是我相信大多数人并不想看。即使你看了，大多人的感受也是“好 nb，然而并没有什么用”。
这道题抽象一下就是：
令：  （图 1） 求：  （图 2）
第一直觉
经过上面的抽象，我的第一直觉这可能是一个数学题，我回想了下数学知识，然后用数学法 AC 了。 数学就是这么简单平凡且枯燥。
然而如果没有数学的加持的情况下，我继续思考怎么做。我想是否可以枚举所有的情况（如图 1），然后对其求最大值（如图 2）。
问题转化为如何枚举所有的情况。经过了几秒钟的思考，我发现这是一个很明显的递归问题。 具体思考过程如下：
我们将原问题抽象为 f(n)
那么 f(n) 等价于 max(1 * fn(n - 1), 2 * f(n - 2), ..., (n - 1) * f(1))。
用数学公式表示就是：
 （图 3）
截止目前，是一点点数学 + 一点点递归，我们继续往下看。现在问题是不是就很简单啦？直接翻译图三为代码即可，我们来看下这个时候的代码：
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i),i * (n - i)))
        return res
毫无疑问，超时了。原因很简单，就是算法中包含了太多的重复计算。如果经常看我的题解的话，这句话应该不陌生。我随便截一个我之前讲过这个知识点的图。
 (图 4)
原文链接：https://github.com/azl397985856/leetcode/blob/master/thinkings/dynamic-programming.md
大家可以尝试自己画图理解一下。
看到这里，有没有种殊途同归的感觉呢？

考虑优化
如上，我们可以考虑使用记忆化递归的方式来解决。只是用一个 hashtable 存储计算过的值即可。
class Solution:
    @lru_cache()
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i),i * (n - i)))
        return res
为了简单起见（偷懒起见），我直接用了 lru_cache 注解， 上面的代码是可以 AC 的。

动态规划
看到这里的同学应该发现了，这个套路是不是很熟悉？下一步就是将其改造成动态规划了。
如图 4，我们的思考方式是从顶向下，这符合人们思考问题的方式。将其改造成如下图的自底向上方式就是动态规划。
 (图 5)
现在再来看下文章开头的代码：
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
        return dp[n]
dp table 存储的是图 3 中 f(n)的值。一个自然的想法是令 dp[i] 等价于 f(i)。而由于上面分析了原问题等价于 f(n)，那么很自然的原问题也等价于 dp[n]。
而 dp[i]等价于 f(i)，那么上面针对 f(i) 写的递归公式对 dp[i] 也是适用的，我们拿来试试。
// 关键语句
res = max(res, max(i * self.integerBreak(n - i),i * (n - i)))

翻译过来就是：
dp[i] = max(dp[i], max(i * dp(n - i),i * (n - i)))
而这里的 n 是什么呢？我们说了dp是自底向下的思考方式，那么在达到 n 之前是看不到整体的n 的。因此这里的 n 实际上是 1,2,3,4... n。
自然地，我们用一层循环来生成上面一系列的 n 值。接着我们还要生成一系列的 i 值，注意到 n - i 是要大于 0 的，因此 i 只需要循环到 n - 1 即可。
思考到这里，我相信上面的代码真的是不难得出了。
关键点
数学抽象
递归分析
记忆化递归
动态规划
代码
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
        return dp[n]



# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        
# @lc code=end

