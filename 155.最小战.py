思路：使用一个辅助栈 Min 记录最小值。每次 push 压栈时判断， 如果 Min 为空就要压一个元素进去， 小于等于Min的最后一个元素也入栈。出栈是判断是否是当前 Min的最后一个元素，是的话 Min才要pop


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._elems = []
        self._min = []  # 储存最小元素

    def push(self, x: int) -> None:
        self._elems.append(x)
        if not self._min or x <= self._min[-1]:
            self._min.append(x)

    def pop(self) -> None:
        tmp = self._elems.pop()
        if tmp == self._min[-1]:
            self._min.pop()
        return tmp

    def top(self) -> int:
        if self._elems:
            return self._elems[-1]

    def getMin(self) -> int:
        if self._min:
            return self._min[-1]
