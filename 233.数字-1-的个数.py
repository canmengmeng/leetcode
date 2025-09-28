#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
from functools import lru_cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        length = len(s)

        # lru_cache 实现了记忆化搜索
        # dfs 函数的返回值是一个元组 (num_count, one_count)
        # num_count: 从当前 pos 位到末尾能构成的数字总数
        # one_count: 在这些数字的 pos 位到末尾部分，'1' 出现的总次数
        @lru_cache(None)
        def dfs(pos: int, is_limit: bool) -> (int, int):
            # 基线条件：如果所有位都填完了，说明构成了一个完整的数。
            # 这是一个有效的方案，但后缀部分没有数字，所以 '1' 的数量是 0。
            # 返回 (1, 0) 表示 "1个合法的数字，其中包含0个'1'" 是不准确的。
            # 这里应该返回 (1, 0) 当 is_leading_zero 为 False，(0, 0) 当 is_leading_zero 为 True 吗？
            # 更简单的理解是，base case 表示一个空后缀。空后缀有1种构成方式(什么都不填)，里面有0个1。
            if pos == length:
                return 1, 0

            total_num_count = 0
            total_one_count = 0
            
            # up 决定了当前位数字的上限
            up = int(s[pos]) if is_limit else 9

            for d in range(up + 1):
                # 如果当前位是前导零，且填的数字也是0
                sub_num_count, sub_one_count = dfs(pos + 1, is_limit and (d == up))

                total_num_count += sub_num_count
                total_one_count += sub_one_count
                
                # 如果当前位填的是 '1'，那么在所有 sub_num_count 种后缀组合中，
                # 当前位这个 '1' 都会出现一次。
                if d == 1:
                    total_one_count += sub_num_count
            
            return total_num_count, total_one_count

        # 初始调用：从第0位开始，受限制，是前导零
        # 我们只需要返回最终的 one_count
        return dfs(0, True)[1]
        
# @lc code=end

