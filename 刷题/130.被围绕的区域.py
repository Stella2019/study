#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.23%)
# Likes:    428
# Dislikes: 0
# Total Accepted:    80.4K
# Total Submissions: 190.4K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#
思路
我们需要将所有被X包围的O变成X，并且题目明确说了边缘的所有O都是不可以变成X的。

其实我们观察会发现，我们除了边缘的O以及和边缘O连通的O是不需要变成X的，其他都要变成X。
经过上面的思考，问题转化为连通区域问题。 这里我们需要标记一下边缘的O以及和边缘O连通的O。 我们当然可以用额外的空间去存，但是对于这道题目而言，我们完全可以mutate。这样就空间复杂度会好一点。
整个过程如图所示：
我将边缘的O以及和边缘O连通的O 标记为了 "A"

关键点解析
二维数组DFS解题模板
转化问题为连通区域问题
直接mutate原数组，节省空间
复杂度分析

时间复杂度：O(row * col)O(row∗col)​

空间复杂度：O(row * col)O(row∗col)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        row, col = len(board), len(board[0])

        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)

        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)

        # 最后完成替换
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
# @lc code=end

