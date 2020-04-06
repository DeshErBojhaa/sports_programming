from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            c = Counter(s)
            ans[tuple((k, c[k]) for k in sorted(c))].append(s)
        return list(ans.values())
