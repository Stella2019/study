"""
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4

方法一：递归 + 线性搜索
最简单的方法就是构建中序序列，然后使用内置的 min 函数在升序数组中找到最接近的元素。

"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return min(inorder(root), key=lambda x: abs(target - x))

复杂度分析

时间复杂度：\mathcal{O}(N)O(N)，因为我们创建了中序序列和在数组中进行线性搜索。
空间复杂度：\mathcal{O}(N)O(N)，使用了一个数组存储中序序列

"""
方法二：迭代
如果最接近的元素的索引远小于树的高度，那么我们可以进行优化。

首先，我们可以一边遍历树一边搜索最接近的值。

第二，我们可以再找到了最接近的值以后立即停止遍历。若目标值位于两个有序数组元素之间 nums[i]<=target<nums[i+1]，则说明我们找到了最接近的元素。
算法：

初始化一个空栈和设 pred 为一个很小的数字。
当 root 不为空：
为了要迭代构建一个中序序列，我们要尽可能的左移并将节点添加到栈中。
弹出栈顶元素：root = stack.pop()。
若目标值在 pred 和 root.val 之间，则最接近的元素在这两个元素之间。
设置 pred = root.val，且向右走一步 root = root.right。
如果我们在循环过程中无法找到最接近的值，这意味着最接近的值是顺序遍历中的最后一个值，返回它。
 
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred <= target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(target - x))

            pred = root.val
            root = root.right

        return pred

复杂度分析

时间复杂度：平均情况下 \mathcal{O}(k)O(k)，最坏的情况下是 \mathcal{O}(H + k)O(H+k)，其中 kk 是最接近元素的索引。
空间复杂度：最坏的情况是树为非平衡树的情况，栈需要 \mathcal{O}(H)O(H) 的空间。


方法三：二分搜索
当我们最接近的元素索引 k 远小于树高 H 时，方法二比较好。

现在我们考虑另一种极限情况，并在 k 相对较大的情况下优化方法一。

使用二进制搜索：如股票目标值小于当前根值，则向左搜索，否则向右搜索。在每一个步骤中选择最接近的值。

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


复杂度分析

时间复杂度：O(H)
O(H)。
空间复杂度：O(1)
O(1)。

