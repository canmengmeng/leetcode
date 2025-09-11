#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []  # 单调递增栈，存储下标
        total_sum = 0
        
        # --- 主循环 ---
        for i in range(n):
            # 当栈不为空，且当前元素小于等于栈顶元素时
            # 注意这里用 <= 来处理重复值，与之前版本 > 稍有不同，但原理一致
            while stack and arr[stack[-1]] >= arr[i]:
                mid = stack.pop()
                
                # 手动处理左边界
                left_boundary = stack[-1] if stack else -1
                
                # 右边界就是当前元素的索引 i
                right_boundary = i
                
                count = (mid - left_boundary) * (right_boundary - mid)
                total_sum = (total_sum + arr[mid] * count) % MOD
                
            stack.append(i)

        # --- 清算循环：处理栈中剩余的元素 ---
        # 此时的右边界是数组的末尾 n
        right_boundary = n
        while stack:
            mid = stack.pop()
            
            # 手动处理左边界
            left_boundary = stack[-1] if stack else -1
            
            count = (mid - left_boundary) * (right_boundary - mid)
            total_sum = (total_sum + arr[mid] * count) % MOD

        return total_sum
        
# @lc code=end

