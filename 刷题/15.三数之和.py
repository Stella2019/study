# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (30.16%)
# Likes:    2802
# Dislikes: 0
# Total Accepted:    375.5K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 回溯
# 笛卡尔积
#
"""采用分治的思想找出三个数相加等于 0，我们可以数组依次遍历，每一项 a[i]我们都认为它是最终能够用组成 0 中的一个数字，那么我们的目标就是找到剩下的元素（除 a[i]）两个相加等于-a[i].
通过上面的思路，我们的问题转化为了给定一个数组，找出其中两个相加等于给定值，我们成功将问题转换为了另外一道力扣的简单题目1. 两数之和。这个问题是比较简单的， 我们只需要对数组进行排序，然后双指针解决即可。 加上需要外层遍历依次数组，因此总的时间复杂度应该是 O(N^2)
在这里之所以要排序解决是因为， 我们算法的瓶颈在这里不在于排序，而在于 O(N^2)，如果我们瓶颈是排序，就可以考虑别的方式了。"""
# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        
        if not digits:
            return []
        # 0-9
        self.d = [" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.res = []
        self.dfs(digits, 0, "")
        return self.res

    def dfs(self, digits, index, s):
        # 递归的终止条件,用index记录每次遍历到字符串的位置
        if index == len(digits):
            self.res.append(s)
            return
        # 获取当前数字
        c = digits[index]
        # print(c, int(c))
        # 获取数字对应字母
        letters = self.d[int(c)]
        # 遍历字符串
        for l in letters:
            # 调用下一层
            self.dfs(digits, index+1, s+l)
# @lc code=end
##复杂度分析
#N + M 是输入数字的总数
#时间复杂度：O(2^N)，其中 N 为 digits 对于的所有可能的字母的和。
#空间复杂度：O(2^N)，其中 N 为 digits 对于的所有可能的字母的和。

"""笛卡尔积
思路
不难发现， 题目要求的是一个笛卡尔积。
比如 digits = 'ab'，其实就是 a 对应的集合 {'a', 'b', 'c'} 和 b 对应的集合 {'d', 'e', 'f'} 笛卡尔积。
简单回忆一下笛卡尔积的内容。对于两个集合 A 和 B，A×B = {(x,y)|x∈A∧y∈B}。
例如，A={a,b}, B={0,1,2}，则：
A×B={(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}
B×A={(0, a), (0, b), (1, a), (1, b), (2, a), (2, b)}
实际上，力扣关于笛卡尔积优化的题目并不少。 比如：
140. 单词拆分 II
95. 不同的二叉搜索树 II
96.unique-binary-search-trees
等等
知道了这一点之后，就不难写出如下代码。
由于我们使用了笛卡尔积优化， 因此可以改造成纯函数，进而使用记忆化递归，进一步降低时间复杂度， 这是一个常见的优化技巧。
关键点
笛卡尔积
记忆化递归"""
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = [" ", " ", "abc", "def", "ghi",
                  "jkl", "mno", "pqrs", "tuv", "wxyz"]
            @lru_cache(None)
        def backtrack(digits, start):
            if start >= len(digits):
                return ['']
            ans = []
            for i in range(start, len(digits)):
                for c in mapper[int(digits[i])]:
                    # 笛卡尔积
                    for p in backtrack(digits, i + 1):
                        # 需要过滤诸如  "d", "e", "f" 等长度不符合的数据
                        if start == 0:
                            if len(c + p) == len(digits):
                                ans.append(c + p)
                        else:
                            ans.append(c + p)
            return ans
        if not digits:
            return []
        return backtrack(digits, 0)

"""复杂度分析
N + M 是输入数字的总数
时间复杂度：O(N^2)，其中 N 为 digits 对于的所有可能的字母的和。
空间复杂度：O(N^2)，其中 N 为 digits 对于的所有可能的字母的和。"""

def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res