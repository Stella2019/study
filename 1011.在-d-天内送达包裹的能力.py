#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (54.81%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 24.6K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
# 
# 
# 
# 示例 1：
# 
# 输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10
# 
# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9),
# (10) 是不允许的。 
# 
# 
# 示例 2：
# 
# 输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
# 
# 
# 示例 3：
# 
# 输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500
# 
# 
#
前置知识
二分法
公司
阿里
思路
这道题和猴子吃香蕉 简直一摸一样，没有看过的建议看一下那道题。
像这种题如何你能发现本质的考点，那么 AC 是瞬间的事情。 这道题本质上就是从 1，2，3，4，。。。total（其中 toal 是总的货物重量）的有限离散数据中查找给定的数。这里我们不是直接查找 target，而是查找恰好能够在 D 天运完的载货量。
容量是 1 可以运完么？
容量是 2 可以运完么？
容量是 3 可以运完么？
。。。
容量是 total 可以运完么？（当然可以，因为 D 大于等于 1）
上面不断询问的过程如果回答是 yes 我们直接 return 即可。如果回答是 no，我们继续往下询问。
这是一个典型的二分问题，只不过我们的判断条件略有不同，大概是：
def canShip(opacity):
    # 指定船的容量是否可以在D天运完
    lo = 0
    hi = total
    while lo < hi:
        mid = (lo + hi) // 2
        if canShip(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo
关键点解析
能够识别出是给定的有限序列查找一个数字（二分查找），要求你对二分查找以及变体十分熟悉
代码
语言支持：JS，Python
Python Code:
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = 0
        hi = 0

        def canShip(opacity):
            days = 1
            remain = opacity
            for weight in weights:
                if weight > opacity:
                    return False
                remain -= weight
                if remain < 0:
                    days += 1
                    remain = opacity - weight
            return days <= D

        for weight in weights:
            hi += weight
        while lo < hi:
            mid = (lo + hi) // 2
            if canShip(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
时间复杂度：O(logN)O(logN)​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
# @lc code=end

