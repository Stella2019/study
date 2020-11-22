"""
给出一个区间的集合，请合并所有重叠的区间。

 

示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x: x[0])
        #start sort

        i = 0
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if result:
                prev_start, prev_end = result[-1]
                hi = min(prev_end, cur_end)
                lo = max(prev_start, cur_start)
                #[1, 4][2, 3] hi = 3, lo = 2

                if lo <= hi:
                    if cur_end > prev_end:
                        result[-1][1] = cur_end
                    else:
                    #[1, 3][4, 6] hi = 2, lo = 4
                        result.append(intervals[i])
                    i += 1
        return result



def merge(intervals):
  results = []
  for start, end in sorted(intervals, key=lambda x: x[0]):
    if results and start <= results[-1][1]:
      prev_start, prev_end = results[-1]
      results[-1] = (prev_start, max(prev_end, end))
    else:
      results.append((start, end))

  return results


print(merge(([1, 3], [5, 8], [4, 10], [20, 25])))
# [(1, 3), (4, 10), (20, 25)]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1]<i[0]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])
        return res

再仔细看下题目，说了intervals是按区间端点进行排序的，因此，可以利用二分查找法查找该区间插入的位置。
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        ins = self.helper(intervals,newInterval[0])
        intervals.insert(ins,newInterval)
        for i in intervals:
            if not res or res[-1][1]<i[0]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])
        return res
    def helper(self,intervals,val):
        l=0
        r=len(intervals)-1
        if intervals[-1][0]<val:
            return r+1
        if intervals[0][0]>val:
            return l
        while l<r:
            mid=(l+r)//2
            if intervals[mid][0]>val:
                r=mid
            else:
                l=mid+1
        return l