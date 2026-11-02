class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        words, res = set(wordList), 0

        q = deque([beginWord])

        while q:
            res += 1
            for _ in range(len(q)):
                cur_word = q.popleft()
                if cur_word == endWord:
                    return res
                
                for i in range(len(cur_word)):
                    for c in range(97, 123): # a-z
                        if chr(c) == cur_word[i]:
                            continue
                        nei = cur_word[:i] + chr(c) + cur_word[i+1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        
        return 0
        




