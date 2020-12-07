#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (38.14%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 12.7K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
# 
# 
# 
# 示例：
# 
# 输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] 为 0 或 1
# 
# 思路
"""由于数组仅包含 0 和 1， 那么问题可以转化为给定一个0，1数组，你可以选择S个1和任意个0，你可以有多少选择？

而上述问题可以转化为给定一个0，1数组，你可以选择最多S个1和任意个0，你的选择数减去 给定一个0，1数组，你可以选择最多S - 1个1和任意个0，你的选择数。

最多xxxx 这种可以使用可变滑动窗口模板解决。

这里插播下可变滑动窗口的思路

可变窗口大小
对于可变窗口，我们同样固定初始化左右指针 l 和 r，分别表示的窗口的左右顶点。后面有所不同，我们需要保证：

l 和 r 都初始化为 0
r 指针移动一步
判断窗口内的连续元素是否满足题目限定的条件
4.1 如果满足，再判断是否需要更新最优解，如果需要则更新最优解。并尝试通过移动 l 指针缩小窗口大小。循环执行 4.1
4.2 如果不满足，则继续。
形象地来看的话，就是 r 指针不停向右移动，l 指针仅仅在窗口满足条件之后才会移动，起到窗口收缩的效果。
 """
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMostK(A, S):
            if S < 0:
                return 0
            i = res = 0

            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res
        return atMostK(A, S) - atMostK(A, S - 1)
 
        
# @lc code=end

