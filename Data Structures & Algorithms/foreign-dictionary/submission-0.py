class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            # the words have the same prefix but the prev word has a longer length
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])
                    break
            
        visit = set()
        cycle = set()
        res = []

        def dfs(c):
            # Found a cycle
            if c in cycle: 
                return True
            
            if c in visit:
                return False
            
            # Post order DFS
            # Visit children/leaf nodes then parent
            cycle.add(c)
            for nei in adj_list[c]:
                if dfs(nei):
                    return False
            
            cycle.remove(c)
            visit.add(c)
            res.append(c)
    
        for c in adj_list:
            # Found a cycle
            if dfs(c):
                return ""
            
        return "".join(res[::-1])

            