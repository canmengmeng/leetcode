#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = 0
        # prefix_dict 用来存储 "某个前缀和出现的次数"
        # 初始化为 {0:1}，表示前缀和为0出现过1次
        # 这样可以处理从开头开始的子数组
        prefix_dict = {0: 1}

        prefix_sum = 0  # 当前的前缀和
        for num in nums:
            prefix_sum += num  # 更新前缀和，表示 nums[0..i] 的累加和

            # 我们希望找到一个 j < i，使得 nums[j+1..i] 的和 = k
            # 等价于：prefix_sum[i] - prefix_sum[j] = k
            # 即：prefix_sum[j] = prefix_sum[i] - k
            target = prefix_sum - k

            # 如果 target 在 prefix_dict 里，说明之前有 prefix_sum[j] = target
            # 那么以 j+1..i 为子数组的区间和就是 k
            if target in prefix_dict:
                counts = counts + prefix_dict[target]

            # 更新 prefix_dict，记录当前 prefix_sum 出现的次数
            if prefix_sum in prefix_dict:
                prefix_dict[prefix_sum] += 1
            else:
                prefix_dict[prefix_sum] = 1

        # 返回总共有多少个子数组的和等于 k
        return counts
        
# @lc code=end

