#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        原地哈希解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(nums)
        
        # --- 1. 放置元素阶段 ---
        # 目标：让 nums[i] 的位置上尽量放 i+1
        for i in range(n):
            # 使用 while 循环，确保换过来的元素也被放到正确的位置
            # 条件：
            # 1. nums[i] 是正数
            # 2. nums[i] 在 [1, n] 范围内
            # 3. nums[i] 不在它应该在的位置上 (nums[i] 应该在 nums[nums[i]-1] 上)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 获取 nums[i] 应该在的目标索引
                target_index = nums[i] - 1
                # 交换
                nums[i], nums[target_index] = nums[target_index], nums[i]
                
        # --- 2. 查找阶段 ---
        # 查找第一个 nums[i] != i+1 的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # --- 3. 边界情况 ---
        # 如果 [1, n] 都存在，那么缺失的就是 n+1
        return n + 1
        
# @lc code=end

