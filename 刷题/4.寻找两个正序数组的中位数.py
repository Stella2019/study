#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.22%)
# Likes:    3464
# Dislikes: 0
# Total Accepted:    297.8K
# Total Submissions: 759.3K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
# 
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 
# 
# 示例 3：
# 
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 
# 
# 示例 4：
# 
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 
# 
# 示例 5：
# 
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#
前置知识
中位数
分治法
二分查找
 
思路
首先了解一下 Median 的概念，一个数组中 median 就是把数组分成左右等分的中位数。
如下图： 
这道题，很容易想到暴力解法，时间复杂度和空间复杂度都是O(m+n), 不符合题中给出O(log(m+n))时间复杂度的要求。 我们可以从简单的解法入手，试了一下，暴力解法也是可以被 Leetcode Accept 的. 分析中会给出两种解法，暴力求解和二分解法。

解法一 - 暴力 （Brute Force）
暴力解主要是要 merge 两个排序的数组（A，B）成一个排序的数组。
用两个pointer（i，j），i 从数组A起始位置开始，即i=0开始，j 从数组B起始位置， 即j=0开始. 一一比较 A[i] 和 B[j],
如果A[i] <= B[j], 则把A[i] 放入新的数组中，i 往后移一位，即 i+1.
如果A[i] > B[j], 则把B[j] 放入新的数组中，j 往后移一位，即 j+1.
重复步骤#1 和 #2，直到i移到A最后，或者j移到B最后。
如果j移动到B数组最后，那么直接把剩下的所有A依次放入新的数组中.
如果i移动到A数组最后，那么直接把剩下的所有B依次放入新的数组中.
Merge 的过程如下图。 
时间复杂度： O(m+n) - m is length of A, n is length of B
空间复杂度： O(m+n)

解法二 - 二分查找 （Binary Search）
由于题中给出的数组都是排好序的，在排好序的数组中查找很容易想到可以用二分查找（Binary Search), 这里对数组长度小的做二分， 保证数组 A 和 数组 B 做 partition 之后
len(Aleft)+len(Bleft)=(m+n+1)/2 - m是数组A的长度， n是数组B的长度
对数组 A 的做 partition 的位置是区间[0,m]
如图： 
下图给出几种不同情况的例子（注意但左边或者右边没有元素的时候，左边用INF_MIN，右边用INF_MAX表示左右的元素： 
下图给出具体做的 partition 解题的例子步骤， 
时间复杂度： O(log(min(m, n)) - m is length of A, n is length of B
空间复杂度： O(1) - 这里没有用额外的空间
关键点分析
暴力求解，在线性时间内 merge 两个排好序的数组成一个数组。
二分查找，关键点在于
要 partition 两个排好序的数组成左右两等份，partition 需要满足len(Aleft)+len(Bleft)=(m+n+1)/2 - m是数组A的长度， n是数组B的长度
并且 partition 后 A 左边最大(maxLeftA), A 右边最小（minRightA), B 左边最大（maxLeftB), B 右边最小（minRightB) 满足 (maxLeftA <= minRightB && maxLeftB <= minRightA)
有了这两个条件，那么 median 就在这四个数中，根据奇数或者是偶数，
奇数：
median = max(maxLeftA, maxLeftB)
偶数：
median = (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
代码
 
def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]
    
    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
   

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# @lc code=end

