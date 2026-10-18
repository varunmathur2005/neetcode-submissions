class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = dict(zip(recipes, ingredients))
        supplies = set(supplies)
        visiting = set()
        impossible = set()

        def dfs(recipe):
            if recipe in supplies:
                return True

            if recipe not in adj or recipe in visiting or recipe in impossible:
                return False

            visiting.add(recipe)

            for ing in adj[recipe]:
                if not dfs(ing):
                    visiting.remove(recipe)
                    impossible.add(recipe)
                    return False

            visiting.remove(recipe)
            supplies.add(recipe)
            return True

        res = []
        for recipe in recipes:
            if dfs(recipe):
                res.append(recipe)

        return res