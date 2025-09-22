#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        heights = [0] * (len(matrix[0]))
        for row in matrix:
            for j in range(len(row)):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
        

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

