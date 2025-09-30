#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 用于记录中序遍历过程中的状态
        self.prev_node = None
        self.first_node = None
        self.second_node = None

        self._inorder_find_swapped(root)

        # 遍历结束后，交换两个错误节点的值
        if self.first_node and self.second_node:
            self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
    
    def _inorder_find_swapped(self, node: Optional[TreeNode]):
        if not node:
            return

        # 1. 遍历左子树
        self._inorder_find_swapped(node.left)

        # 2. 处理当前节点
        # self.prev_node 是中序遍历中 node 的前一个节点
        if self.prev_node and self.prev_node.val > node.val:
            # 发现了逆序对！
            if not self.first_node:
                # 这是第一次发现逆序对
                # 第一个错误节点是较大的那个 (prev_node)
                self.first_node = self.prev_node
                # 第二个错误节点暂时是较小的那个 (node)
                self.second_node = node
            else:
                # 这是第二次发现逆序对
                # 第二个错误节点更新为较小的那个 (node)
                self.second_node = node
        
        # 更新 prev_node，为下一个节点的比较做准备
        self.prev_node = node

        # 3. 遍历右子树
        self._inorder_find_swapped(node.right)
        
# @lc code=end

