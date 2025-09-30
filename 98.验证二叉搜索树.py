#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 用于记录中序遍历过程中的状态
        self.prev_node = None
        return self._inorder_find_swapped(root)

    def _inorder_find_swapped(self, node: Optional[TreeNode]):
        if not node:
            return True

        # 1. 遍历左子树
        left_bool = self._inorder_find_swapped(node.left)

        # 2. 处理当前节点
        # self.prev_node 是中序遍历中 node 的前一个节点
        if self.prev_node and self.prev_node.val >= node.val:
            # 发现了逆序对！
            return False
        
        # 更新 prev_node，为下一个节点的比较做准备
        self.prev_node = node

        # 3. 遍历右子树
        right_bool = self._inorder_find_swapped(node.right)

        return left_bool and right_bool
        
# @lc code=end

