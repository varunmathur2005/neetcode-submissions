class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        nei = defaultdict(list) # map each pattern to words
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        res = 1
        q = deque([beginWord])
        visit = set([beginWord])

        while q:
            for _ in range(len(q)):
                curWord = q.popleft()
                print(curWord)
                if curWord == endWord:
                    print(f"Reached")
                    return res
                
                for i in range(len(curWord)):
                    pattern = curWord[:i] + "*" + curWord[i + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0
        




