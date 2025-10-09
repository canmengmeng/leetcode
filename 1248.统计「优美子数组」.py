#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # count：记录优美子数组的总数
        count = 0
        
        # prefix_sum：记录遍历到当前位置为止，奇数的累计个数（即奇数的前缀和）
        prefix_sum = 0
        
        # prefix_dict：哈希表，用来记录“奇数个数”出现的次数
        # 其中键是奇数的前缀和，值是该前缀和出现的次数
        # 初始化 {0: 1} 表示“前缀和为0”的情况出现过1次，
        # 这样可以处理从头开始的子数组（即前缀刚好有k个奇数的情况）
        prefix_dict = {0: 1}

        # 遍历整个数组
        for num in nums:
            # 如果 num 是奇数，则 num % 2 == 1；否则为 0。
            # 因此 prefix_sum 表示前缀中“奇数的数量”
            prefix_sum += num % 2

            # 当前前缀和 - k = target
            # 表示我们要找之前有多少个前缀的“奇数个数”为 target
            # 这样从那个前缀之后到当前位置之间，恰好包含 k 个奇数
            target = prefix_sum - k

            # 如果 target 存在于哈希表中，说明之前出现过这么多奇数的前缀
            # 每一种这样的前缀都能和当前位置构成一个优美子数组
            if target in prefix_dict.keys():
                count += prefix_dict[target]

            # 将当前的 prefix_sum 计入哈希表（出现次数 +1）
            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1
        
        # 返回最终的优美子数组数量
        return count
        
# @lc code=end

