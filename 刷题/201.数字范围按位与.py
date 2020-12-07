#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (51.35%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    37.6K
# Total Submissions: 73.2K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
# 
# 示例 1: 
# 
# 输入: [5,7]
# 输出: 4
# 
# 示例 2:
# 
# 输入: [0,1]
# 输出: 0
# 
#
思路
一个显而易见的解法是， 从m到n依次进行求与的操作。
    let res = m;
    for (let i = m + 1; i <= n; i++) {
      res = res & i;
    }
    return res;
但是， 如果你把这个solution提交的话，很显然不会通过， 会超时。
我们依旧还是用trick来简化操作。 我们利用的性质是， n个连续数字求与的时候，前m位都是1.
举题目给的例子：[5,7] 共 5， 6，7三个数字， 用二进制表示 101, 110,111, 这三个数字特点是第一位都是1，后面几位求与一定是0.
再来一个明显的例子：[20, 24], 共 20， 21， 22， 23，24五个数字，二进制表示就是
0001 0100
0001 0101
0001 0110
0001 0111
0001 1000
这五个数字特点是第四位都是1，后面几位求与一定是0.
因此我们的思路就是， 求出这个数字区间的数字前多少位都是1了，那么他们求与的结果一定是前几位数字，然后后面都是0.
关键点解析
n个连续数字求与的时候，前m位都是1
可以用递归实现， 个人认为比较难想到
bit 运算
代码：
(n > m) ? (rangeBitwiseAnd(m/2, n/2) << 1) : m;
每次问题规模缩小一半， 这是二分法吗？

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m != n:
            m >>= 1
            n >>= 1
            cnt += 1

        return m << cnt
复杂度分析

时间复杂度：最坏的情况我们需要循环N次，最好的情况是一次都不需要， 因此时间复杂度取决于我们移动的位数，具体移动的次数取决于我们的输入，平均来说时间复杂度为 O(N)O(N)，其中N为M和N的二进制表示的位数。

空间复杂度：O(1)O(1)
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
# @lc code=end

