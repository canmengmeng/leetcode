#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = 0
        # prefix_dict 用来存储 "某个前缀和出现的次数"
        # 初始化为 {0:1}，表示前缀和为0出现过1次
        # 这样可以处理从开头开始的子数组
        prefix_dict = {0: 1}

        prefix_sum = 0  # 当前的前缀和
        for num in nums:
            prefix_sum += num  # 更新前缀和，表示 nums[0..i] 的累加和
            target = prefix_sum % k  # 计算当前前缀和对 k 取模的结果

            # 更新 prefix_dict，记录当前 prefix_sum 出现的次数
            if target in prefix_dict.keys():
                prefix_dict[target] += 1
            else:
                prefix_dict[target] = 1
            
            # 如果 target 出现过，说明存在某个 j 使得 prefix_sum[j] % k == target
            counts += (prefix_dict[target] - 1)


        # 返回总共有多少个子数组的和等于 k
        return counts
        
# @lc code=end

