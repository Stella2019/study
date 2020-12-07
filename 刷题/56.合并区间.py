#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (43.56%)
# Likes:    719
# Dislikes: 0
# Total Accepted:    169.9K
# Total Submissions: 389.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
# 
# 
# 
# 提示：
# 
# 
# intervals[i][0] <= intervals[i][1]
# 
# 
#
"""思路
先对数组进行排序，排序的依据就是每一项的第一个元素的大小。
然后我们对数组进行遍历，遍历的时候两两运算（具体运算逻辑见下）
判断是否相交，如果不相交，则跳过
如果相交，则合并两项
关键点解析
对数组进行排序简化操作
如果不排序，需要借助一些 hack,这里不介绍了"""
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """先排序，后合并"""
        if len(intervals) <= 1:
            return intervals

        # 排序
        def get_first(a_list):
            return a_list[0]
        intervals.sort(key=get_first)

        # 合并
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])

        return res
# @lc code=end

#时间复杂度：由于采用了排序，因此复杂度大概为 O(NlogN)O(NlogN)​
#空间复杂度：O(N)O(N