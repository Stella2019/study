#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
# https://leetcode-cn.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (49.13%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 20.7K
# Testcase Example:  '[2,2,3,4]'
#
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
# 
# 示例 1:
# 
# 
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 
# 
# 注意:
# 
# 
# 数组长度不超过1000。
# 数组里整数的范围为 [0, 1000]。
# 
# 
#
前置知识
排序
双指针
二分法
三角形边的关系
 
暴力法（超时）
思路
首先要有一个数学前提： 如果三条线段中任意两条的和都大于第三边，那么这三条线段可以组成一个三角形。即给定三个线段 a，b，c，如果满足 a + b > c and a + c > b and b + c > a，则线段 a，b，c 可以构成三角形，否则不可以。
力扣中有一些题目是需要一些数学前提的，不过这些数学前提都比较简单，一般不会超过高中数学知识，并且也不会特别复杂。一般都是小学初中知识即可。
如果你在面试中碰到不知道的数学前提，可以寻求面试官提示试试。
关键点解析
三角形边的关系
三层循环确定三个线段
代码
代码支持: Python
class Solution:
    def is_triangle(self, a, b, c):
        if a == 0 or b == 0 or c == 0: return False
        if a + b > c and a + c > b and b + c > a: return True
        return False
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if self.is_triangle(nums[i], nums[j], nums[k]): ans += 1

        return ans
复杂度分析
时间复杂度：，其中 N 为 数组长度。
空间复杂度：
优化的暴力法
思路
暴力法的时间复杂度为 ， 其中 $N$ 最大为 1000。一般来说，  的算法在数据量 <= 500 是可以 AC 的。1000 的数量级则需要考虑  或者更好的解法。
OK，到这里了。我给大家一个干货。 应该是其他博主不太会提的。原因可能是他们不知道， 也可能是他们觉得太小儿科不需要说。
由于前面我根据数据规模推测到到了解法的复杂度区间是 $N ^ 2$, $N ^ 2 * logN$，不可能是 $N$ （WHY？）。
降低时间复杂度的方法主要有： 空间换时间 和 排序换时间（我们一般都是使用基于比较的排序方法）。而排序换时间仅仅在总体复杂度大于  才适用（原因不用多说了吧？）。
这里由于总体的时间复杂度是 ，因此我自然想到了排序换时间。当我们对 nums 进行一次排序之后，我发现：
is_triangle 函数有一些判断是无效的
    def is_triangle(self, a, b, c):
        if a == 0 or b == 0 or c == 0: return False
        # a + c > b 和  b + c > a 是无效的判断，因为恒成立
        if a + b > c and a + c > b and b + c > a: return True
        return False
因此我们的目标变为找到a + b > c即可，因此第三层循环是可以提前退出的。
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = j + 1
        while k < n and num[i] + nums[j] > nums[k]:
            k += 1
        ans += k - j - 1
这也仅仅是减枝而已，复杂度没有变化。通过进一步观察，发现 k 没有必要每次都从 j + 1 开始。而是从上次找到的 k 值开始就行。原因很简单， 当 nums[i] + nums[j] > nums[k] 时，我们想要找到下一个满足 nums[i] + nums[j] > nums[k] 的 新的 k 值，由于进行了排序，因此这个 k 肯定比之前的大（单调递增性），因此上一个 k 值之前的数都是无效的，可以跳过。
for i in range(n - 2):
    k = i + 2
    for j in range(i + 1, n - 1):
        while k < n and nums[i] + nums[j] > nums[k]:
            k += 1
        ans += k - j - 1
由于 K 不会后退，因此最内层循环总共最多执行 N 次，因此总的时间复杂度为 。
这个复杂度分析有点像单调栈，大家可以结合起来理解。
关键点分析
排序
代码
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
        return ans
复杂度分析
时间复杂度：O(N ^ 2)O(N 
2
 )
空间复杂度：取决于排序算法

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
# @lc code=end

