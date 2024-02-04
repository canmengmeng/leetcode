#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.left = 0
        self.right = 0
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.right] = value
            self.size += 1
            self.right = (self.right + 1) % self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.size -= 1
            self.left = (self.left + 1) % self.k
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.k - 1 if self.right == 0 else self.right - 1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

