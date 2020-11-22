"""
（这是一个交互题）

我们称只包含元素 0 或 1 的矩阵为二进制矩阵。矩阵中每个单独的行都按非递减顺序排序。

给定一个这样的二进制矩阵，返回至少包含一个 1 的最左端列的索引（从 0 开始）。如果这样的列不存在，返回 -1。

您不能直接访问该二进制矩阵。你只可以通过 BinaryMatrix 接口来访问。

BinaryMatrix.get(row, col) 返回位于索引 (row, col) （从 0 开始）的元素。
BinaryMatrix.dimensions() 返回含有 2 个元素的列表 [rows, cols]，表示这是一个 rows * cols的矩阵。
如果提交的答案调用 BinaryMatrix.get 超过 1000 次，则该答案会被判定为错误答案。提交任何试图规避判定机制的答案将会被取消资格。

下列示例中， mat 为给定的二进制矩阵。您不能直接访问该矩阵。

1. (Binary Search) For each row do a binary search to find the leftmost one
on that row and update the answer.
2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner.
p can only move left or down.
If the value at p is 0, move down.
If the value at p is 1, move left.
Try to figure out the correctness and time complexity of this algorithm.
"""


#二分

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        res = float('inf')

        for r in range(row):
            left, right = 0, col - 1
            while left < right:
                mid = (left + right) >> 1
                if binaryMatrix.get(r, mid):
                    right = mid
                else:
                    left = mid + 1
            if not binaryMatrix.get(r, left):
                continue
            else:
                res = min(res, left)

        return res if res != float('inf') else -1


"""python get()方法用法理解

list.get(k,d)
get相当于一条if...else...语句,参数k在字典中，字典将返回list[k];如果参数k不在字典中则返回参数d,如果K在字典中则返回k对应的value值；
例子：
l = {5:2,3:4}
print l.get(3,0)返回的值是4；
Print l.get（1,0）返回值是0；
"""

#Python 从右上角开始找, 非二分 O(N)复杂度
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        i, j = 0, col - 1
        while -1 < i < row and -1 < j < col:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        if j == col - 1:  #判断-1条件
            return -1
        else:
            return j + 1



#错误答案；
class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row, col = binaryMatrix.dimensions()
        i, j = 0, col-1
        while -1 < i < row and -1 < j < col:
            if binaryMatrix.get(i,j) == 1:
                j -= 1
            else:
                i += 1
        return j + 1


