class Solution:
    def findEvenNumbers(self, dd: List[int]) -> List[int]:
        ans, N = set(), len(dd)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if i == k or j == k:
                        continue
                    if dd[i] == 0 or dd[k]%2!=0:
                        continue
                    # print(dd[i], dd[j], dd[k])
                    ans.add(int(f'{dd[i]}{dd[j]}{dd[k]}'))
        return sorted(ans)
