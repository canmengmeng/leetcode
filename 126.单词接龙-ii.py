#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        import collections
        """
        使用 BFS 构建前驱图 + DFS 回溯路径，解决单词接龙 II 问题。
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # --- 阶段一: BFS 构建前驱图 ---

        # predecessors: 记录每个单词的所有最短路径上的前驱节点
        predecessors = collections.defaultdict(set)
        # distances: 记录从 beginWord 到每个单词的最短距离
        distances = {beginWord: 0}
        
        queue = collections.deque([beginWord])
        found = False
        
        while queue and not found:
            # 逐层遍历
            level_size = len(queue)
            # 用一个子字典记录本层新发现的节点的距离，避免在同一层内重复计算
            sub_level_distances = {}

            for _ in range(level_size):
                current_word = queue.popleft()
                
                # 寻找所有邻居
                for i in range(len(current_word)):
                    for char_code in range(ord('a'), ord('z') + 1):
                        char = chr(char_code)
                        neighbor_word = current_word[:i] + char + current_word[i+1:]

                        # 确保邻居在词典中
                        if neighbor_word not in wordSet:
                            continue
                        
                        # 1. 如果邻居是新节点，或者邻居是从更短的路径到达的
                        if neighbor_word not in distances:
                            # 如果邻居不在本层的 sub_level_distances 中，说明是本层第一次遇到
                            if neighbor_word not in sub_level_distances:
                                sub_level_distances[neighbor_word] = distances[current_word] + 1
                                queue.append(neighbor_word)
                            predecessors[neighbor_word].add(current_word)

                        # 2. 如果是从另一条同样短的路径到达邻居，也加入前驱
                        # (这种情况在逐层遍历并用 sub_level_distances 控制后，只会发生在不同父节点指向同一子节点时)
                        # 比如 A->C, B->C 都在同一层，dist[A] == dist[B]
                        if distances.get(neighbor_word) == distances[current_word] + 1:
                            predecessors[neighbor_word].add(current_word)
                
            # 将本层发现的节点距离更新到主 distances 字典中
            distances.update(sub_level_distances)
            # 如果在本层找到了 endWord，标记 found 为 true，BFS 将在下一轮循环开始时停止
            if endWord in distances:
                found = True

        # --- 阶段二: DFS 回溯查找所有路径 ---
        
        results = []
        
        def dfs(word, current_path):
            # 递归基：如果回溯到了 beginWord，说明找到了一条完整路径
            if word == beginWord:
                # 将路径倒序后加入结果列表
                results.append(current_path[::-1])
                return

            # 递归地访问所有前驱节点
            if word in predecessors:
                for parent in predecessors[word]:
                    current_path.append(parent)
                    dfs(parent, current_path)
                    # 回溯，将父节点弹出，为同级的其他分支做准备
                    current_path.pop()

        # 从 endWord 开始，带着初始路径 ["endWord"] 进行 DFS
        if endWord in distances:
            dfs(endWord, [endWord])
            
        return results
        
# @lc code=end

