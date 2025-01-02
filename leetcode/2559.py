class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vv = {'a', 'e', 'i', 'o', 'u'}
        def ok(x):
            return int(x[0] in vv and x[-1] in vv)

        a = list(accumulate([ok(x) for x in words])) + [0]

        ans = []

        for x, y in queries:
            ans.append(a[y] - a[x-1])
        
        return ans
