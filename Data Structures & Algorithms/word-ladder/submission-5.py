class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        adj_list = defaultdict(list) # Map pattern to words 

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj_list[pattern].append(word)
        
        visited = set()
        q = deque([(beginWord, 1)]) # word, num_of_transformation

        while q:
            for _ in range(len(q)):
                word, num = q.popleft()

                if word == endWord:
                    return num
                
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i + 1:]
                    for nei in adj_list[pat]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        q.append((nei, num + 1))
        return 0
        

                    
