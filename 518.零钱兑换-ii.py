#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (55.84%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    34.8K
# Total Submissions: 62.2K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#
前置知识
​动态规划​

背包问题

 

思路
这个题目和 coin-change 的思路比较类似。

我们还是按照 coin-change 的思路来， 如果将问题画出来大概是这样：


进一步我们可以对问题进行空间复杂度上的优化（这种写法比较难以理解，但是相对更省空间）


这里用动图会更好理解， 有时间的话我会做一个动图出来， 现在大家脑补一下吧

关键点解析
动态规划

子问题

用 dp[i] 来表示组成 i 块钱，需要最少的硬币数，那么

第 j 个硬币我可以选择不拿 这个时候， 组成数 = dp[i]

第 j 个硬币我可以选择拿 这个时候， 组成数 = dp[i - coins[j]] + dp[i]

和 01 背包问题不同， 硬币是可以拿任意个，属于完全背包问题

对于每一个 dp[i] 我们都选择遍历一遍 coin， 不断更新 dp[i]

eg:

if (amount === 0) return 1;
​
const dp = [Array(amount + 1).fill(1)];
​
for (let i = 1; i < amount + 1; i++) {
  dp[i] = Array(coins.length + 1).fill(0);
  for (let j = 1; j < coins.length + 1; j++) {
    // 从1开始可以简化运算
    if (i - coins[j - 1] >= 0) {
      // 注意这里是coins[j -1]而不是coins[j]
      dp[i][j] = dp[i][j - 1] + dp[i - coins[j - 1]][j]; // 由于可以重复使用硬币所以这里是j不是j-1
    } else {
      dp[i][j] = dp[i][j - 1];
    }
  }
}
​
return dp[dp.length - 1][coins.length];
当我们选择一维数组去解的时候，内外循环将会对结果造成影响


eg:

// 这种答案是不对的。
// 原因在于比如amount = 5, coins = [1,2,5]
// 这种算法会将[1,2,2] [2,1,2] [2, 2, 1] 算成不同的
​
if (amount === 0) return 1;
​
const dp = [1].concat(Array(amount).fill(0));
​
for (let i = 1; i < amount + 1; i++) {
  for (let j = 0; j < coins.length; j++) {
    if (i - coins[j] >= 0) {
      dp[i] = dp[i] + dp[i - coins[j]];
    }
  }
}
​
return dp[dp.length - 1];
​
// 正确的写法应该是内外循环调换一下, 具体可以看下方代码区
代码
 
Python Code:

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
​
        for j in range(len(coins)):
            for i in range(1, amount + 1):
                if i >= coins[j]:
                    dp[i] += dp[i - coins[j]]
​
        return dp[-1]
复杂度分析

时间复杂度：O(amount)O(amount)​

空间复杂度：O(amount * len(coins))O(amount∗len(coins))​

扩展
这是一道很简单描述的题目， 因此很多时候会被用到大公司的电面中。

相似问题:

​322.coin-change​

附录
Python 二维解法（不推荐，但是可以帮助理解）：

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        for j in range(len(coins) + 1):
            dp[0][j] = 1
​
        for i in range(amount + 1):
            for j in range(1, len(coins) + 1):
                if i >= coins[j - 1]:
                    dp[i][j] = dp[i - coins[j - 1]][j] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
复杂度分析

时间复杂度：O(amount * len(coins))O(amount∗len(coins))​

空间复杂度：O(amount * len(coins))O(amount∗len(coins))
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
# @lc code=end

