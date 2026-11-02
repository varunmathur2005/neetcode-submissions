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
                    # Check - words with one character difference
                    for c in "abcdefghijklmnopqrstuvwxyz": # a-z
                        if c == cur_word[i]:
                            continue
                        nei = cur_word[:i] + c + cur_word[i+1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        
        return 0
        




