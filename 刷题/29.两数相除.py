#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (20.22%)
# Likes:    464
# Dislikes: 0
# Total Accepted:    70.9K
# Total Submissions: 350.4K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
# -2
# 
# 
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
# 
# 
# 
# 提示：
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#二分法
"""关键点解析
二分查找
正负数的判断中，这样判断更简单。
const isNegative = dividend > 0 !== divisor > 0;
或者利用异或：
const isNegative = dividend ^ divisor < 0;"""
# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        二分法
        :param int divisor
        :param int dividend
        :return int
        """
        # 错误处理
        if divisor == 0:
            raise ZeroDivisionError
        if abs(divisor) == 1:
            result = dividend if 1 == divisor else -dividend
            return min(2**31-1, max(-2**31, result))

        # 确定结果的符号
        sign = ((dividend >= 0) == (divisor >= 0))

        result = 0
        # abs也可以直接写在while条件中，不过可能会多计算几次
        _divisor = abs(divisor)
        _dividend = abs(dividend)

        while _divisor <= _dividend:
            r, _dividend = self._multi_divide(_divisor, _dividend)
            result += r

        result = result if sign else -result

        # 注意返回值不能超过32位有符号数的表示范围
        return min(2**31-1, max(-2**31, result))

    def _multi_divide(self, divisor, dividend):
        """
        翻倍除法，如果可以被除，则下一步除数翻倍，直至除数大于被除数，
        返回商加总的结果与被除数的剩余值；
        这里就不做异常处理了；
        :param int divisor
        :param int dividend
        :return tuple result, left_dividend
        """
        result = 0
        times_count = 1
        while divisor <= dividend:
            dividend -= divisor
            result += times_count
            times_count += times_count
            divisor += divisor
        return result, dividend
# @lc code=end

#时间复杂度：O(logN)O(logN)​

#空间复杂度：O(1)O(1)