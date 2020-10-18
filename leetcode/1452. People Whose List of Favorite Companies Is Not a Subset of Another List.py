# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        N = len(favoriteCompanies)
        candidate = set(range(N))
        
        for i, v in enumerate(favoriteCompanies):
            favoriteCompanies[i] = set(v)
        
        for i in range(N):
            for j in range(i+1, N):
                if favoriteCompanies[i].issubset(favoriteCompanies[j]):
                    candidate.discard(i)
                if favoriteCompanies[j].issubset(favoriteCompanies[i]):
                    candidate.discard(j)
        
        return sorted(candidate)
