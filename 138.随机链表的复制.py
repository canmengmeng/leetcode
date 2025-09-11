#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        原地修改，O(1) 空间复杂度的深拷贝
        时间复杂度: O(n)
        空间复杂度: O(1) (不考虑新链表本身的存储空间)
        """
        if not head:
            return None

        # --- 第一次遍历: 将新节点编织到原链表中 ---
        # A -> B -> C  变为  A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # --- 第二次遍历: 设置新节点的 random 指针 ---
        curr = head
        while curr:
            # curr.next 是新节点
            if curr.random:
                # 新节点的 random 指向旧节点 random 的下一个节点（也就是 random 的拷贝）
                curr.next.random = curr.random.next
            curr = curr.next.next # 移动到下一个旧节点

        # --- 第三次遍历: 解开两个链表 ---
        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head
        
        while curr_old:
            # 恢复旧链表的 next
            curr_old.next = curr_new.next
            
            # 设置新链表的 next
            if curr_new.next:
                curr_new.next = curr_new.next.next
            
            # 移动指针
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head
        
# @lc code=end

