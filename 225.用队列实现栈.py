#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:
    def __init__(self):
        self.deque1 = deque()
        self.deque2 = deque()

    def push(self, x: int) -> None:
        self.deque1.append(x)

    def pop(self) -> int:
        while len(self.deque1) > 1:
            self.deque2.append(self.deque1.popleft())
        tmp = self.deque1.popleft()
        while len(self.deque2) > 0:
            self.deque1.append(self.deque2.popleft())
        return tmp

    def top(self) -> int:
        while len(self.deque1) > 1:
            self.deque2.append(self.deque1.popleft())
        tmp = self.deque1[0]
        self.deque2.append(self.deque1.popleft())
        while len(self.deque2) > 0:
            self.deque1.append(self.deque2.popleft())
        return tmp

    def empty(self) -> bool:
        return len(self.deque1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

