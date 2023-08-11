#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ''' Solution 1
        tmp_ = node.next
        while tmp_.next:
            node.val = tmp_.val
            tmp_ = tmp_.next
            node = node.next
        node.val = tmp_.val
        node.next = None
        '''
        ''' Solution 2
        '''
        node.val = node.next.val
        node.next = node.next.next
        

        
# @lc code=end

