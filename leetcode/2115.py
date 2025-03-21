class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)
        g = defaultdict(list)

        for i, r in enumerate(recipes):
            g[r] = ingredients[i]
        
        
        def rec(cur, seen):
            if cur in sup:
                return True
            if len(g[cur]) == 0:
                return False
            seen.add(cur)
            ok = True
            for n in g[cur]:
                if n in seen:
                    return False
                ok &= rec(n, seen)
            if cur in seen:
                seen.remove(cur)
            return ok
        
        ans = []
        for x in recipes:
            if not rec(x, set()):
                continue
            ans.append(x)
        return ans
