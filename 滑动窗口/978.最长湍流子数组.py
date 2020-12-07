#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#
# https://leetcode-cn.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (42.39%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 27K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
# 
# 
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 
# 
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
# 
# 返回 A 的最大湍流子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
# 
# 
# 示例 2：
# 
# 输入：[4,8,12,16]
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：[100]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
# 思路
"""我们先尝试从题目给的例子打开思路。
对于 A 为 [9,4,2,10,7,8,8,1,9] 来说，我用这样的一个数组 arr 来表示 [-, -, +, -, +, 0, -, +]。其含义是 arr[i] 表示 A[i] - A[i - 1]的符号，其中：+ 表示正号，- 表示 负号，0 表示 A[i] 和 A[i - 1]相同的情况，那么显然 arr 的长度始终为 A 的长度 - 1。
那么不难得出，题目给出的剩下两个例子的 arr 为：[+, +, +] 和 []。
通过观察不难发现， 实际题目要求的就是正负相间的最大长度。如上的三个例子分别为：
我用粗体表示答案部分

[-, -, +, -, +, 0, -, +]，答案是 4 + 1
[+, +, +]，答案是 1 + 1
[]，答案是 0 + 1
于是使用滑动窗口求解就不难想到了，实际上题目求的是连续xxxx，你应该有滑动窗口的想法才对，对不对另说，想到是最起码的。

由于 0 是始终不可以出现在答案中的，因此这算是一个临界条件，大家需要注意特殊判断一下，具体参考代码部分"""
#代码中使用了一个小技巧，就是 a ^ b >= 0 说明其符号相同，这样比相乘判断符号的好处是可以避免大数溢出。

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        i = 0
        for j in range(2, len(arr)):
            if (arr[j] == arr[j - 1]):
                i = j
            elif (arr[j] - arr[j - 1]) ^ (arr[j - 1] - arr[j - 2]) >= 0:
                i = j - 1
            ans = max(ans, j - i + 1)
        return ans
# @lc code=end

"""A subarray is turbulent if the comparison sign alternates between consecutive elements (ex. nums[0] < nums[1] > nums[2] < nums[3] > ... ). Looking at the structure of the array, this means every element of a turbulent subarray must belong to either a peak (A[i-2] < A[i-1] > A[i]) or a valley (A[i-2] > A[i-1] < A[i]) structure.

The algorithm works as follows. Keep track of the length of the longest run ending at index i. This is tracked in a variable named clen. If the last three elements form a peak or a valley, we can extend the previous run length by 1 (meaning clen += 1). Otherwise, we can no longer extend this run and need to reset clen to the length of the longest run ending at index i. This run length will be 1 if the previous and current elements are the same (Ex: [2,2,2]), or 2 if the previous and current elements differ (Ex: [2,4,6]). The answer is the length of the best run found.
"""
 
"""def maxTurbulenceSize(self, A):
    best = clen = 0

    for i in range(len(A)):
        if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
            clen += 1
        elif i >= 1 and A[i-1] != A[i]:
            clen = 2
        else:
            clen = 1
        best = max(best, clen)
    return best
"""