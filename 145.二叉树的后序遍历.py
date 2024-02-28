#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 使用两个栈完成二叉树后序遍历
        # ans = []
        # if root is None:
        #     return ans
        # stack = []
        # stack.append(root)
        # while len(stack) > 0:
        #     tmp = stack.pop()
        #     ans.append(tmp.val)
        #     if tmp.left is not None:
        #         stack.append(tmp.left)
        #     if tmp.right is not None:
        #         stack.append(tmp.right)
        # return ans[::-1]
        
        # 使用一个栈完成二叉树后序遍历
        ans = []
        if root is None:
            return ans
        stack = []
        stack.append(root)
        pre = root
        while len(stack) > 0:
            tmp = stack[-1]
            if tmp.left is not None and tmp.left != pre and tmp.right != pre:
                stack.append(tmp.left)
            elif tmp.right is not None and tmp.right != pre:
                stack.append(tmp.right)
            else:
                tmp = stack.pop()
                pre = tmp
                ans.append(tmp.val)
        return ans
# @lc code=end

