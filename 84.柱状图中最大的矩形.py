#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 在末尾添加哨兵，确保所有柱子都能被弹出计算
        heights.append(0)
        stack = [] # 单调递增栈
        max_area = 0
        
        for i, h in enumerate(heights):
            # 当当前高度小于栈顶高度时，可以计算栈顶元素的面积了
            while stack and heights[stack[-1]] >= h:
                # 弹出栈顶，以它的高度作为矩形的高
                height = heights[stack.pop()]
                # 宽度是当前索引 i 到 新的栈顶索引 之间的距离
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            
            # 当前索引入栈
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, height * width)
        
        return max_area
        
# @lc code=end

