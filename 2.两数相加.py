#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        add_tmp = 0
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + add_tmp
            add_tmp = tmp // 10
            tmp = tmp % 10
            tail.next = ListNode(val=tmp)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            tmp = l1.val + add_tmp
            add_tmp = tmp // 10
            tmp = tmp % 10
            tail.next = ListNode(val=tmp)
            tail = tail.next
            l1 = l1.next
        while l2 is not None:
            tmp = l2.val + add_tmp
            add_tmp = tmp // 10
            tmp = tmp % 10
            tail.next = ListNode(val=tmp)
            tail = tail.next
            l2 = l2.next
        if add_tmp > 0:
            tail.next = ListNode(val=add_tmp)
            tail = tail.next
        return head.next
# @lc code=end

