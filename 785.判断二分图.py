#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (50.00%)
# Likes:    200
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 58.6K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# 给定一个无向图graph，当这个图为二分图时返回true。
# 
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
# 
# 
# graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边：
# graph[i] 中不存在i，并且graph[i]中没有重复的值。
# 
# 
# 
# 示例 1:
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释: 
# 无向图如下:
# 0----1
# |    |
# |    |
# 3----2
# 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
# 
# 
# 
# 
# 示例 2:
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释: 
# 无向图如下:
# 0----1
# | \  |
# |  \ |
# 3----2
# 我们不能将节点分割成两个独立的子集。
# 
# 
# 注意:
# 
# 
# graph 的长度范围为 [1, 100]。
# graph[i] 中的元素的范围为 [0, graph.length - 1]。
# graph[i] 不会包含 i 或者有重复的值。
# 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
# 
# 
#
前置知识
图的遍历
DFS
公司
暂无
思路
和 886 思路一样。 我甚至直接拿过来 dfs 函数一行代码没改就 AC 了。
唯一需要调整的地方是 graph 。 我将其转换了一下，具体可以看代码，非常简单易懂。
具体算法：
设置一个长度为 N 的数组 colors，colors[i] 表示 节点 i 的颜色，0 表示无颜色， 1 表示一种颜色， - 1 表示另一种颜色。
初始化 colors 全部为 0
构图（这里有邻接矩阵） 使得 grid[i][j] 表示 i 和 j 是否有连接（这里用 0 表示无， 1 表示有）
遍历图。
如果当前节点未染色，则染色，不妨染为颜色 1
递归遍历其邻居
如果邻居没有染色， 则染为另一种颜色。即 color * - 1，其中 color 为当前节点的颜色
否则，判断当前节点和邻居的颜色是否一致，不一致则返回 False，否则返回 True
强烈建议两道题一起练习一下。
关键点
图的建立和遍历
colors 数组
代码
class Solution:
    def dfs(self, grid, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            if grid[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(grid, colors, j, -1 * color, N):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        grid = [[0] * N for _ in range(N)]
        colors = [0] * N
        for i in range(N):
            for j in graph[i]:
                grid[i][j] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(grid, colors, i, 1, N):
                return False
        return True
复杂度分析
时间复杂度：O(N 
2
 )
空间复杂度：O(N 
 )

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
# @lc code=end

