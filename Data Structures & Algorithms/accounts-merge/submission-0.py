class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union-Find Algorithm
        par = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(node):
            res = par[node]
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        
        # Core Account Merge code
        email_to_account = {} # Map email to account id

        # Merge the accounts - updating the parent and rank logic
        for i, account in enumerate(accounts):
            emails = account[1:]
            for e in emails:
                if e in email_to_account:
                    union(i, email_to_account[e])
                else:
                    email_to_account[e] = i
        
        email_groups = defaultdict(list) # map account_id to email
        for e, i in email_to_account.items():
            par_id = find(i)
            email_groups[par_id].append(e)
        res = []
        for e_id, e in email_groups.items():
            name = accounts[e_id][0]
            res.append(
                [name] + sorted(e)
            )
        print(res)
        return res






