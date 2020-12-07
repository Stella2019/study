#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.15%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    51.9K
# Total Submissions: 63.2K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
# N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
# 
# 
#
前置知识
回溯
深度优先遍历
公司
阿里
百度
字节
思路
使用深度优先搜索配合位运算，二进制为 1 代表不可放置，0 相反
利用如下位运算公式：
x & -x ：得到最低位的 1  代表除最后一位 1 保留，其他位全部为 0
x & (x-1)：清零最低位的 1  代表将最后一位 1 变成 0       
x & ((1 << n) - 1)：将 x 最高位至第 n 位(含)清零
关键点
位运算
DFS（深度优先搜索）
代码
语言支持：JS
/**
 * @param {number} n
 * @return {number}
 * @param row 当前层
 * @param cols 列
 * @param pie 左斜线
 * @param na 右斜线
 */
const totalNQueens = function (n) {
    let res = 0;
    const dfs = (n, row, cols, pie, na) => {
        if (row >= n) {
            res++;
            return;
        }
        // 将所有能放置 Q 的位置由 0 变成 1，以便进行后续的位遍历
        // 也就是得到当前所有的空位
        let bits = (~(cols | pie | na)) & ((1 << n) - 1);
        while (bits) {
            // 取最低位的1
            let p = bits & -bits;
            // 把P位置上放入皇后
            bits = bits & (bits - 1);
            // row + 1 搜索下一行可能的位置
            // cols ｜ p 目前所有放置皇后的列
            // (pie | p) << 1 和 (na | p) >> 1) 与已放置过皇后的位置 位于一条斜线上的位置
            dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1);
        }
    }
    dfs(n, 0, 0, 0, 0);
    return res;
};
复杂度分析
时间复杂度：O(N!)
空间复杂度：O(N)

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
# @lc code=end

