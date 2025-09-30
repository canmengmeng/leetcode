#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        # dp[i][j] 表示 s[i..j] 中最长回文子序列的长度
        dp = [[0] * n for _ in range(n)]
        
        # Base Case: 所有长度为 1 的子串，其最长回文子序列长度都是 1
        for i in range(n):
            dp[i][i] = 1
            
        # 状态转移
        # i 必须从下往上遍历
        for i in range(n - 2, -1, -1):
            # j 必须从左往右遍历，且 j > i
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # 如果两端字符相同，则等于内部区间的长度 + 2
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # 如果两端字符不同，则等于去掉任意一端后的两种情况的最大值
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        # 最终结果是整个字符串 s[0..n-1] 的解
        return dp[0][n-1]

        
# @lc code=end

