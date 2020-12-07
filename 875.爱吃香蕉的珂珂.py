#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
# https://leetcode-cn.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (45.50%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 49.4K
# Testcase Example:  '[3,6,7,11]\r\n8\r'
#
# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
# 
# 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K
# 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
# 
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 
# 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入: piles = [3,6,7,11], H = 8
# 输出: 4
# 
# 
# 示例 2：
# 
# 输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
# 
# 
# 示例 3：
# 
# 输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#
前置知识
二分查找
公司
字节
思路
符合直觉的做法是，选择最大的堆的香蕉数，然后试一下能不能行，如果不行则直接返回上次计算的结果，如果行，我们减少 1 个香蕉，试试行不行，依次类推。计算出刚好不行的即可。这种解法的时间复杂度比较高，为 ，其中 N 为 piles 长度， M 为 Piles 中最大的数。。
这道题如果能看出来是二分法解决，那么其实很简单。为什么它是二分问题呢？我这里画了个图，我相信你看了就明白了。

香蕉堆的香蕉个数上限是 10^9， 珂珂这也太能吃了吧？
关键点解析
二分查找模板
代码
代码支持：Python，JavaScript
Python Code:
class Solution:
    def canEatAllBananas(self, piles, H, K):
        t = 0
        for pile in piles:
            t += math.ceil(pile / K)
        return t <= H
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        # [l, r) ， 左闭右开的好处是如果能找到，那么返回 l 和 r 都是一样的，因为最终 l 等于 r。
        while l < r:
            mid = (l + r) >> 1
            if self.canEatAllBananas(piles, H, mid):
                r = mid
            else:
                l = mid + 1
        return l
复杂度分析

时间复杂度：O(max(N, N * logM))O(max(N,N∗logM))，其中 N 为 piles 长度， M 为 Piles 中最大的数。

空间复杂度：O(1)O(1)
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
# @lc code=end

