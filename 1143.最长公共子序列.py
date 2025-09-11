#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        动态规划解法
        时间复杂度: O(m * n)
        空间复杂度: O(m * n)
        """
        m, n = len(text1), len(text2)
        # 创建 dp 表，并初始化为 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_len = 0          # 记录最长公共的长度
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])    
                else:
                    # 如果字符不匹配，连续性中断，长度归 0
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return max_len
        
# @lc code=end

