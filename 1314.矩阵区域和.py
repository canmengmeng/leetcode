#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # 初始化答案矩阵，大小与 mat 相同
        answer = [[0] * len(mat[0]) for _ in range(len(mat))]

        # 构造二维前缀和矩阵 prefix_sum
        # prefix_sum[i][j] 表示从 (0,0) 到 (i-1, j-1) 的矩形区域的元素和
        # 注意这里多加了一行一列（长度+1），用于方便处理边界情况
        prefix_sum = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]

        # 构建二维前缀和矩阵
        for i in range(1, len(prefix_sum)):
            for j in range(1, len(prefix_sum[0])):
                # 二维前缀和公式：
                # 当前格 = 上方 + 左方 - 左上角 + 当前mat值
                prefix_sum[i][j] = (
                    prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )
        
        # 遍历每一个位置 (i, j)，计算其“块区域”的和
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                # 确定块区域的上下左右边界（限制在矩阵范围内）
                upper = i - k if i - k >= 0 else 0
                lower = i + k if i + k < len(mat) else len(mat) - 1
                left = j - k if j - k >= 0 else 0
                right = j + k if j + k < len(mat[0]) else len(mat[0]) - 1

                # 使用前缀和快速计算矩形区域和
                # 注意：前缀和矩阵比原矩阵多1行1列，因此要 +1
                # 计算公式：
                # sum = A - B - C + D
                # 其中：
                # A = prefix_sum[lower+1][right+1]
                # B = prefix_sum[upper][right+1]
                # C = prefix_sum[lower+1][left]
                # D = prefix_sum[upper][left]
                answer[i][j] = (
                    prefix_sum[lower + 1][right + 1]
                    - prefix_sum[upper][right + 1]
                    - prefix_sum[lower + 1][left]
                    + prefix_sum[upper][left]
                )

        # 返回结果矩阵
        return answer


        
# @lc code=end

