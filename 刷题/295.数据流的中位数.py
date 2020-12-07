#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (49.23%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 52.4K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#
思路
这道题目是求动态数据的中位数，在 leetcode 难度为hard. 如果这道题是求静态数据的中位数，我们用数组去存储， 空间复杂度 O(1), 时间复杂度 O(1)
空间复杂度指的是除了存储数据之外额外开辟的用于计算等任务的内存空间
代码也比较简单
function findMedian(a) {
  return a.length % 2 === 0
    ? (a[a.length >> 1] + a[a.length >> (1 + 1)]) / 2
    : a[a.length >> 1];
}
但是题目要求是动态数据， 那么是否可以每次添加数据的时候，都去排一次序呢？ 假如我们每次插入都用快速排序进行排序的话，那么时间复杂度是 O(nlogn) + O(1)
O(nlogn) 是排序的时间复杂度 O(1)是查询中位数的时间复杂度
如果你用这种思路进行的话， 恐怕 leetcode 会超时。
那么如何优化呢？ 答案是使用堆， Java， C++等语言都有优先级队列中这种数据结构， 优先级队列本质上就是一个堆。 关于堆和优先级队列的关系，我会放在《数据结构和算法》部分讲解。这里不赘述
如果借助堆这种数据结构， 就可以轻易实现了。
具体的做法是，建立两个堆，这两个堆需要满足:
大顶堆元素都比小顶堆小（由于堆的特点其实只要比较堆顶即可）
大顶堆元素不小于小顶堆，且最多比小顶堆多一个元素
满足上面两个条件的话，如果想要找到中位数，就比较简单了
如果两个堆数量相等（本质是总数为偶数）, 就两个堆顶元素的平均数
如果两个堆数量不相等（本质是总数为奇数）， 就取大顶堆的堆顶元素
比如对于[1,2,3] 求中位数：

再比如对于[1,2,3, 4] 求中位数：

关键点解析
用两个堆（一个大顶堆，一个小顶堆）来简化时间复杂度
用优先级队列简化操作
JavaScript 不像 Java， C++等语言都有优先级队列中这种数据结构， 因此大家可以使用社区的实现 个人认为没有非要纠结于优先级队列怎么实现， 至少这道题不是考这个的 优先级队列的实现个人认为已经超过了这道题想考察的范畴
from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

