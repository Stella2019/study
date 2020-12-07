#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (55.92%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 109.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 
# 示例 1:
# 
# 输入: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# 输出: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# 示例 2:
# 
# 输入: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# 输出: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 进阶:
# 
# 
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
# 
# 
#状态压缩
思路
符合直觉的想法是，使用一个 m + n 的数组来表示每一行每一列是否”全部是 0“， 先遍历一遍去构建这样的 m + n 数组，然后根据这个 m + n 数组去修改 matrix 即可。
这样的时间复杂度 O(m * n), 空间复杂度 O(m + n).
但是这道题目还有一个 follow up， 要求使用 O(1)的时间复杂度。因此上述的方法就不行了。 但是我们要怎么去存取这些信息（哪一行哪一列应该全部为 0）呢？
一种思路是使用第一行第一列的数据来代替上述的 zeros 数组。 这样我们就不必借助额外的存储空间，空间复杂度自然就是 O(1)了。
由于我们不能先操作第一行和第一列， 因此我们需要记录下”第一行和第一列是否全是 0“这样的一个数据，最后根据这个信息去 修改第一行和第一列。
具体步骤如下：
记录下”第一行和第一列是否全是 0“这样的一个数据
遍历除了第一行和第一列之外的所有的数据，如果是 0，那就更新第一行第一列中对应的元素为 0
你可以把第一行第一列看成我们上面那种解法使用的 m + n 数组。
根据第一行第一列的数据，更新 matrix
最后根据我们最开始记录的”第一行和第一列是否全是 0“去更新第一行和第一列即可
关键点
使用第一行和第一列来替代我们 m + n 数组
先记录下”第一行和第一列是否全是 0“这样的一个数据，否则会因为后续对第一行第一列的更新造成数据丢失
最后更新第一行第一列
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setRowZeros(matrix: List[List[int]], i:int) -> None:
            C = len(matrix[0])
            matrix[i] = [0] * C

        def setColZeros(matrix: List[List[int]], j:int) -> None:
            R = len(matrix)
            for i in range(R):
                matrix[i][j] = 0

        isCol = False
        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1, C):
            if matrix[0][j] == 0:
                setColZeros(matrix, j)

        for i in range(R):
            if matrix[i][0] == 0:
                setRowZeros(matrix, i)

        if isCol:
            setColZeros(matrix, 0)

另一种方法是用一个特殊符合标记需要改变的结果，只要这个特殊标记不在我们的题目数据范围（0 和 1）即可，这里用 None。

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        这题要解决的问题是，必须有个地方记录判断结果，但又不能影响下一步的判断条件；
        直接改为0的话，会影响下一步的判断条件；
        因此，有一种思路是先改为None，最后再将None改为0；
        从条件上看，如果可以将第一行、第二行作为记录空间，那么，用None应该也不算违背题目条件；
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 遍历矩阵，用None记录要改的地方，注意如果是0则要保留，否则会影响下一步判断
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is not None and matrix[r][c] == 0:
                    # 改值
                    for i in range(rows):
                        matrix[i][c] = None if matrix[i][c] != 0 else 0
                    for j in range(cols):
                        matrix[r][j] = None if matrix[r][j] != 0 else 0
        # 再次遍历，将None改为0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is None:
                    matrix[r][c] = 0

时间复杂度：O(M * N)O(M∗N)​

空间复杂度：O(1)O(1)
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
# @lc code=end

