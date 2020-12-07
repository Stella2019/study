#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#
# https://leetcode-cn.com/problems/smallest-integer-divisible-by-k/description/
#
# algorithms
# Medium (33.64%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 11K
# Testcase Example:  '1'
#
# 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
# 
# 返回 N 的长度。如果不存在这样的 N，就返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入：1
# 输出：1
# 解释：最小的答案是 N = 1，其长度为 1。
# 
# 示例 2：
# 
# 输入：2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 N 。
# 
# 示例 3：
# 
# 输入：3
# 输出：3
# 解释：最小的答案是 N = 111，其长度为 3。
# 
# 
# 
# 提示：
# 
# 
# 1 <= K <= 10^5
# 
# 
#
前置知识
循环节
公司
暂无
思路
这道题是说给定一个 K 值，能否找到一个形如 1，11，111，1111 。。。 这样的数字 n 使得 n % K == 0。
首先容易想到的是如果 K 是 2，4，5， 6，8 结尾的话，一定是不行的。直观的解法是从 1，11，111，1111 。。。 这样一直除下去，直到碰到可以整除的，我们返回即可。 但是如果这个数字根本就无法整除怎么办？没错，我们会无限循环下去。我们应该在什么时刻跳出循环，返回 - 1 （表示不能整除）呢？
我们拿题目给出的不能整除的 2 来说。
1 // 2 等于 1
11 // 2 等于 1
111 // 2 等于 1
...
我们再来一个不能整除的例子 6:
1 // 6 等于 1
11 // 6 等于 5
111 // 6 等于 3
1111 // 6 等于 1
11111 // 6 等于 5
...
通过观察我们发现不断整除的过程，会陷入无限循环，对于 2 来说，其循环节就是 1。对于 6 来说，其循环节来说就是 153。而且由于我们的分母是 6，也就是说余数的可能性一共只有六种情况 0,1,2,3,4,5。
上面是感性的认识， 接下来我们从数学上予以证明。上面的算法用公式来表示就是mod = (10 \* mod + 1) % K。假如出现了相同的数，我们可以肯定之后会无限循环。比如 153 之后出现了 1，我们可以肯定之后一定是 35。。。 因为我们的 mod 只是和前一个 mod 有关，上面的公式是一个纯函数。
关键点解析
数学（无限循环与循环节）
代码
#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#

# @lc code=start


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 in [2, 4, 5, 6, 8]:
            return - 1
        seen = set()
        mod = 0
        for i in range(1, K + 1):
            mod = (mod * 10 + 1) % K
            if mod in seen:
                return -1
            if mod == 0:
                return ix
            seen.add(mod)

# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
# @lc code=end

