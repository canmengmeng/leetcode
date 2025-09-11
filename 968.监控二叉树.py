#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera = 0
        
        def dfs(node):
            # 定义三种状态
            # 0: 该节点未被覆盖 (Uncovered)
            # 1: 该节点已被覆盖，但无相机 (Covered, No Camera)
            # 2: 该节点自身有相机 (Has Camera)
            if node is None:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.camera += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0
        
        if dfs(root) == 0:
            self.camera += 1
        return self.camera
        
# @lc code=end

