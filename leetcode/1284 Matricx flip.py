class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flat_str(m):
            ret = []
            for x in m:
                ret += x
            return ''.join(map(str, ret))
        
        def generate(m):
            for i in range(len(m)):
                for j in range(len(m[0])):
                    mm = deepcopy(m)
                    mm[i][j] = 1 - mm[i][j]
                    if i - 1 >= 0:
                        mm[i-1][j] = 1 - mm[i-1][j]
                    if i + 1 < len(mm):
                        mm[i + 1][j] = 1 - mm[i + 1][j]
                    if j - 1 >= 0:
                        mm[i][j-1] = 1 - mm[i][j-1]
                    if j + 1 < len(mm[0]):
                        mm[i][j+1] = 1 - mm[i][j+1]
                    yield mm

        def zero(mm):
            for i in range(len(mm)):
                for j in range(len(mm[0])):
                    if mm[i][j] != 0:
                        return False
            return True

        seen = set()
        if zero(mat):
            return 0
        q = deque([(mat, 0)])

        while q:
            now, cost = q.popleft()
            for nx in generate(now):
                if zero(nx):
                    return cost + 1
                flat = flat_str(nx)
                if flat in seen:
                    continue
                seen.add(flat)
                q.append((nx, cost + 1))
        
        return -1
