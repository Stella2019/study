#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# https://leetcode-cn.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (40.13%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 13K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
# 
# 每个人都可能不喜欢其他人，那么他们不应该属于同一组。
# 
# 形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
# 
# 当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# dislikes[i].length == 2
# 1 
# dislikes[i][0] < dislikes[i][1]
# 对于 dislikes[i] == dislikes[j] 不存在 i != j
# 
# 
#
前置知识
图的遍历

DFS

公司
暂无

思路
这是一个图的问题。解决这种问题一般是要遍历图才行的，这也是图的套路。 那么遍历的话，你要有一个合适的数据结构。 比较常见的图存储方式是邻接矩阵和邻接表。

而我们这里为了操作方便（代码量），直接使用邻接矩阵。由于是互相不喜欢，不存在一个喜欢另一个，另一个不喜欢一个的情况，因此这是无向图。而无向图邻接矩阵实际上是会浪费空间，具体看我下方画的图。

而题目给我们的二维矩阵并不是现成的邻接矩阵形式，因此我们需要自己生成。

我们用 1 表示互相不喜欢（dislike each other）。

        graph = [[0] * N for i in range(N)]
        for a, b in dislikes:
            graph[a - 1][b - 1] = 1
            graph[b - 1][a - 1] = 1

image.png
同时可以用 hashmap 或者数组存储 N 个人的分组情况， 业界关于这种算法一般叫染色法，因此我们命名为 colors，其实对应的本题叫 groups 更合适。


image.png
我们用：

0 表示没有分组

1 表示分组 1

-1 表示分组 2

之所以用 0，1，-1，而不是 0，1，2 是因为我们会在不能分配某一组的时候尝试分另外一组，这个时候有其中一组转变为另外一组就可以直接乘以-1，而 0，1，2 这种就稍微麻烦一点而已。

具体算法：

遍历每一个人，尝试给他们进行分组，比如默认分配组 1.


image.png
然后遍历这个人讨厌的人，尝试给他们分另外一组，如果不可以分配另外一组，则返回 False

那问题的关键在于如何判断“不可以分配另外一组”呢？


image.png
实际上，我们已经用 colors 记录了分组信息，对于每一个人如果分组确定了，我们就更新 colors，那么对于一个人如果分配了一个组，并且他讨厌的人也被分组之后，分配的组和它只能是一组，那么“就是不可以分配另外一组”。

代码表示就是：

# 其中j 表示当前是第几个人，N表示总人数。 dfs的功能就是根据colors和graph分配组，true表示可以分，false表示不可以，具体代码见代码区。
if colors[j] == 0 and not self.dfs(graph, colors, j, -1 * color, N)
关键点
二分图

染色法

图的建立和遍历

colors 数组

代码
class Solution:
    def dfs(self, graph, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            # dislike eachother
            if graph[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(graph, colors, j, -1 * color, N):
                    return False
        return True
​
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[0] * N for i in range(N)]
        colors = [0] * N
        for a, b in dislikes:
            graph[a - 1][b - 1] = 1
            graph[b - 1][a - 1] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(graph, colors, i, 1, N):
                return False
        return True
复杂度分析

时间复杂度：O(N^2)O(N 
2
 )​

空间复杂度：O(N)O(N)
# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
# @lc code=end

