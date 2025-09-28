#
# @lc app=leetcode.cn id=1931 lang=python3
#
# [1931] 用三种不同颜色为网格涂色
#

# @lc code=start
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        import collections
        """
        使用状态压缩动态规划解决网格涂色问题
        """
        MOD = 10**9 + 7

        # 1. 生成所有有效的单列涂色状态
        # 状态用一个长度为 m 的元组表示，例如 (0, 1, 2)
        valid_states = []
        
        # 使用回溯法生成
        def generate_states(row_index, current_state):
            # 当一列填满时，将其加入有效状态列表
            if row_index == m:
                valid_states.append(tuple(current_state))
                return

            # 尝试三种颜色 (0, 1, 2)
            for color in range(3):
                # 检查是否与上一行的颜色冲突
                if row_index > 0 and color == current_state[row_index - 1]:
                    continue
                
                current_state.append(color)
                generate_states(row_index + 1, current_state)
                current_state.pop()

        generate_states(0, [])
        
        num_valid_states = len(valid_states)
        if num_valid_states == 0:
            return 0

        # 2. 构建状态之间的邻接关系（转移图）
        # adj[i] 存储了所有可以跟在 valid_states[i] 后面的状态的索引
        adj = collections.defaultdict(list)
        for i in range(num_valid_states):
            for j in range(num_valid_states):
                state1 = valid_states[i]
                state2 = valid_states[j]
                
                # 检查 state1 和 state2 是否可以相邻
                is_compatible = True
                for k in range(m):
                    if state1[k] == state2[k]:
                        is_compatible = False
                        break
                
                if is_compatible:
                    adj[i].append(j)

        # 3. 动态规划
        # dp[i] 表示当前列涂成 valid_states[i] 的方案数
        dp = [1] * num_valid_states

        # 从第二列开始，递推 n-1 次
        for _ in range(n - 1):
            new_dp = [0] * num_valid_states
            # 遍历上一列的所有可能状态
            for prev_state_idx in range(num_valid_states):
                # 遍历当前列可以接在 prev_state 后面的所有状态
                for curr_state_idx in adj[prev_state_idx]:
                    new_dp[curr_state_idx] = (new_dp[curr_state_idx] + dp[prev_state_idx]) % MOD
            dp = new_dp

        # 4. 计算最终结果
        # 结果是最后一列所有可能状态的方案数之和
        total_ways = sum(dp) % MOD
        return total_ways
        
# @lc code=end

