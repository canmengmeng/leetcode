#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections
        """
        使用广度优先搜索 (BFS) 和预处理优化解决单词接龙问题。
        """
        # 1. 预处理：将 wordList 转换为集合，方便快速查找
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # 2. 预处理：构建a通用状态到单词列表的映射
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generic_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[generic_word].append(word)

        # 3. 初始化 BFS
        # 队列中存储 (单词, 路径长度)
        queue = collections.deque([(beginWord, 1)])
        # visited 集合存储已访问过的单词
        visited = {beginWord}

        # 4. 开始 BFS 循环
        while queue:
            current_word, level = queue.popleft()

            # 遍历当前单词的所有通用状态
            for i in range(len(current_word)):
                generic_word = current_word[:i] + "*" + current_word[i+1:]

                # 找到所有符合该通用状态的邻居单词
                for neighbor in all_combo_dict[generic_word]:
                    # 如果邻居就是 endWord，我们找到了最短路径
                    if neighbor == endWord:
                        return level + 1
                    
                    # 如果邻居没有被访问过
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        # 如果队列为空还没找到，说明无法转换
        return 0
        
# @lc code=end

