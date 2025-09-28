#
# @lc app=leetcode.cn id=943 lang=python3
#
# [943] 最短超级串
#

# @lc code=start
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        '''给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。

        我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。

        

        示例 1：

        输入：words = ["alex","loves","leetcode"]
        输出："alexlovesleetcode"
        解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
        示例 2：

        输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
        输出："gctaagttcatgcatc"'''
        import collections
        n = len(words)
        if n == 1:
            return words[0]

        # 1. 预处理: 计算任意两个字符串之间的重叠长度和拼接成本
        overlaps = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # 寻找 words[i] 的后缀和 words[j] 的前缀的最大重叠
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlaps[i][j] = k
                        break
        
        # 2. 初始化DP和path数组
        # dp[mask][i]: 访问集合为mask，以words[i]结尾的最短超级串长度
        dp = [[float('inf')] * n for _ in range(1 << n)]
        # path[mask][i]: 达到dp[mask][i]最优时，i的前一个节点的索引
        path = [[-1] * n for _ in range(1 << n)]
        deque = collections.deque()

        # 初始化单元素路径
        for i in range(n):
            dp[1 << i][i] = len(words[i])
            deque.append((1 << i, i))

        while deque:
            mask, i = deque.popleft()
            for j in range(n):
                if (mask >> j) & 1 == 0:  # j不在mask中
                    new_mask = mask | (1 << j)
                    new_cost = dp[mask][i] + len(words[j]) - overlaps[i][j]
                    if new_cost < dp[new_mask][j]:
                        dp[new_mask][j] = new_cost
                        path[new_mask][j] = i
                        deque.append((new_mask, j))
        
        # 4. 寻找最优路径的终点
        min_len = float('inf')
        last_idx = -1
        final_mask = (1 << n) - 1
        for i in range(n):
            if dp[final_mask][i] < min_len:
                min_len = dp[final_mask][i]
                last_idx = i

        # 5. 回溯路径，得到拼接顺序
        p = []
        cur_mask = final_mask
        cur_idx = last_idx
        while cur_idx != -1:
            p.append(cur_idx)
            prev_idx = path[cur_mask][cur_idx]
            cur_mask ^= (1 << cur_idx)
            cur_idx = prev_idx
        
        p.reverse() # 得到正确的拼接顺序

        # 6. 根据顺序构造最终的超级串
        res = [words[p[0]]]
        for i in range(1, n):
            prev_word_idx = p[i-1]
            cur_word_idx = p[i]
            overlap_len = overlaps[prev_word_idx][cur_word_idx]
            res.append(words[cur_word_idx][overlap_len:])
            
        return "".join(res)

        
# @lc code=end

