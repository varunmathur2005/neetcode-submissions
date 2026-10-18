from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        supplies = set(supplies) 

        for i, r in enumerate(recipes):
            adj[r] = ingredients[i]

        cycle = set()
        res = []

        def dfs(recipe): # If we can make it return True        
            if recipe in supplies:
                return True
            
            if recipe in cycle or recipe not in adj:
                return False
            
            cycle.add(recipe)
            for ingredient in adj[recipe]:
                if dfs(ingredient) == False:
                    cycle.remove(recipe)
                    return False
            
            cycle.remove(recipe)
            supplies.add(recipe)
            return True

        for i in range(len(recipes)):
            if dfs(recipes[i]):
                res.append(recipes[i])
        
        return res

