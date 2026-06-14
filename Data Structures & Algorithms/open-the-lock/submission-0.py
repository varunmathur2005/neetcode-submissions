class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        visit = set(deadends)
        q = deque() # Combination, turns
        q.append(("0000", 0))

        def child_states(state):
            children = []
            for i in range(4):
                digit = str((int(state[i]) + 1) % 10)
                children.append(state[:i] + digit + state[i + 1:])
                digit = str((int(state[i]) -1 + 10) % 10)
                children.append(state[:i] + digit + state[i + 1:])
            return children

        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            
            children = child_states(state)

            for c in children:
                if c not in visit:
                    visit.add(c)
                    q.append((c, turns + 1))
        
        return -1
