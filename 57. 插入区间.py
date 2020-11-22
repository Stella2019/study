"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
 

注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。

跟LeetCode-Python-56. 合并区间类似，暴力解就是直接把新的区间插进去然后调用56的合并函数就好了。

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # tmp = Interval(newInterval[0], newInterval[1])
        intervals.append(newInterval)
        # intervals[-1] = newInterval
        # print type(intervals[0]), type(tmp)
        return self.merge(intervals)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for item in intervals:
            if item[0] <= right:
                right = max(right, item[1])
            else:
                res.append([left, right])
                left = item[0]
                right = item[1]
        res.append([left, right])

        return res

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        l = len(intervals)
        res = []
        intervals = sorted(intervals, key = lambda intervals:intervals.start)
        low = intervals[0].start
        high = intervals[0].end
        for i in range(1, l):
            if intervals[i].start <= high:
                high = max(high, intervals[i].end)
            else:
                res.append([low, high])
                low = intervals[i].start
                high = intervals[i].end
        res.append([low, high])
        return res