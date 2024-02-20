#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#
# [1, 4, 3]
# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0 for _ in range(k)]
        self.left = 0
        self.right = 0
        self.size = 0
        self.limit = k


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.left = self.limit - 1 if self.left == 0 else self.left - 1
            self.deque[self.left] = value
            self.size += 1
            return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque[self.right] = value
            self.right = 0 if self.right == self.limit - 1 else self.right + 1
            self.size += 1
            return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left = 0 if self.left == self.limit - 1 else self.left + 1
            self.size -= 1
            return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.right = self.limit - 1 if self.right == 0 else self.right - 1
            self.size -= 1
            return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.left]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.limit - 1 if self.right == 0 else self.right - 1]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.limit



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

