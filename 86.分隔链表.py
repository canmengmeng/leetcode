#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode()  # < x region
        left_tail = left_head 
        right_head = ListNode()  # >=x region
        right_tail = right_head

        while head is not None:
            head_next = head.next
            head.next = None

            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next

            head = head_next

        # < x region is not empty
        left_tail.next = right_head.next
        return left_head.next
# @lc code=end

