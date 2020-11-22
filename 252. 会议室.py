"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

示例 1:

输入: [[0,30],[5,10],[15,20]]
输出: false
示例 2:

输入: [[7,10],[2,4]]
输出: true

时间复杂度：O(NlogN)，N为数组长度，排序+遍历了一次数组
空间复杂度：O(1)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
"""
Done 1: 判断下一个会议开始时否小于上一个会议结束，从头判断
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sort_l = sorted(intervals, key=lambda x: x[0])
        for num, interval in enumerate(sort_l):
            try:
                if interval[1] > sort_l[num+1][0]:
                    return False
            except IndexError:
                return True
        return True
"""
Done 2：判断上一个会议结束小于当前会议开始，从尾判断
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        _index = len(sort_intervals) - 1

        while _index > 0:
            if sort_intervals[_index][0] < sort_intervals[_index - 1][1]:
                return False
            _index = _index - 1
        return True

"""
Done 3： 基于开始时间排序，取结束时间，基于结束时间排序，对比，有变化则说明有时间冲突
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        flat_intervals = [item for i in sort_intervals for item in i]
        sort_flat_intervals = sorted(flat_intervals)
        if flat_intervals == sort_flat_intervals:
            return True
        else:
            return False

""" 
Done 4：使用临时变量存储每个interval结束时间和下一个对比
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        tmp_date = 0
        for interval in sort_intervals:
            if interval[0] >= tmp_date:
                tmp_date = interval[1]
            else:
                return False
        return True




