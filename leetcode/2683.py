class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        N = len(derived)
        for f in [0, 1]:
            ans = [f]
            for i, v in enumerate(derived):
                ans.append(ans[-1] ^ v)
                if ans[i] ^ ans[(i + 1) % N] != v:
                    break
            else:
                return True
        return False
