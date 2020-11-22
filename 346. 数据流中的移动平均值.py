"""
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

示例:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

方法一：数组或列表
我们可以用数组或列表来记录所有传入的值。然后从中取出对应的元素来计算平均值。
算法：

我们初始化 queue 来存储数据流的数据和移动窗口 n 的大小。
每次调用 next(val)，首先将 val 添加到 queue 中，然后我们从 queue 取最后 n 个元素计算平均值。
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)。其中 NN 是移动窗口的大小，每次调用 next(val)，我们需要从 queue 中检索 NN 个元素。
空间复杂度：\mathcal{O}(M)O(M)，是 queue 的大小。

"""


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)

"""
方法二：双端队列
我们可以比方法一使用更优的时间复杂度和空间复杂度。

我们会注意到并不需要存储数据流中的所有值，只需要数据流中的最后 n 个值。

根据移动窗口的定义，在每个步骤中，我们向窗口添加一个新元素，同时从窗口中删除第一个元素。这里，我们可以应用一种称为双端队列的数据结构（deque）来实现移动窗口，它在两端删除或添加元素将具有常数的时间复杂度（\mathcal{O}(1)O(1)）；使用双端队列，我们可以将空间复杂度降低到 \mathcal{O}(N)O(N)，其中 NN 是移动窗口的大小。
 
 其次，为了计算移动窗口元素的总和 sum，我们不需要遍历窗口的全部元素。

我们可以保留前一个移动窗口的总和 sum，然后为了得到新的移动窗口的总和，我们只需要 sum+=new_val,sum-=first_val，这样就可以得到新的总和，其中 new_val 为添加的值，first_val 为原移动窗口中的第一个值，这样可以将时间复杂度降低到常数。

 算法：
下面是 Python 中 deque 的定义。我们在其他编程语言（如 Java）中也有类似的 deque 实现。

Deques 是堆栈和队列的泛化（名称读作 deck，是双端队列的缩写）。Deques 支持线程安全，可以在两端在时间复杂度为 O(1)O(1) 进行添加和删除元素。

根据前面说的，我们用 deque 替换队列，并添加一个新的变量 window_sum，在常数时间内计算移动窗口的和。

时间复杂度：\mathcal{O}(1)O(1)。
空间复杂度：\mathcal{O}(N)O(N)，移动窗口的大小。 
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)


"""
方法三：基于数组的循环队列
除了 deque 之外，还可以应用另一种有趣的数据结构，称为循环队列 circular queue，它是一个环形的队列。
循环队列的主要优点是，通过向循环队列中添加新元素，它会自动丢弃最旧的元素。与 deque 不同，我们不需要显式地删除最旧的元素。

循环队列的另一个优点是，一个指针就足以跟踪队列的两端，不像 deque 那样，我们必须为每一端保留一个指针。

算法：

无需使用任何库，可以轻松实现具有固定大小数组的循环队列。关键是 head 和 tail 元素的关系，我们可以用以下公式：
tail=(head+1)modsize

换句话说，tail 元素就在 head 元素的旁边。一旦我们向前移动 head，我们将覆盖前面的 tail 元素。
时间复杂度：\mathcal{O}(1)O(1)。我们可以看到在 next(val) 函数中没有循环。
空间复杂度：\mathcal{O}(N)O(N)，循环队列使用的大小。
 
"""


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size  # 队列窗口长度
        self.queue = []  # 队列

    def next(self, val: int) -> float:
        size = self.size
        queue = self.queue
        queue.append(val)  # 尾入队
        if len(queue) > size:
            del queue[0]  # 头出队

        return sum(queue) / min(size, len(queue))  # 计算移动平均值



class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.currindex = 0
        self.nums = []
        self.sizedSum = 0
        self.length = 0

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.sizedSum += val
        self.length += 1
        if self.length <= self.size :
            return  self.sizedSum / self.length
        else :
            self.sizedSum = (self.sizedSum - self.nums[self.currindex])
            self.currindex += 1
            return self.sizedSum / self.size


