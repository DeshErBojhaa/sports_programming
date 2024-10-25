class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        f = sorted(folder, key=str)
        seen = set()
        # print(f)
        for i, x in enumerate(f):
            if i in seen:
                continue
            for j in range(i+1, len(f)):
                if len(x) == len(f[j]) and x == f[:len(x)]:
                    seen.add(j)
                    continue

                if f[j][:len(x)] == x and f[j][len(x)] == '/':
                    seen.add(j)
                else:
                    break
        ans = []
        for i in range(len(f)):
            if i not in seen:
                ans.append(f[i])
        return ans
