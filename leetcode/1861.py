class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for b in box:
            N, r = len(b), None
            for l in range(N-1, -1, -1):
                if b[l] == '*':
                    r = l-1
                if r is None and b[l] == '.':
                    r = l
                if b[l] == '#' and r is not None:
                    b[l] = '.'
                    b[r] = '#'
                    r -= 1
                
        ans = []
        for x in zip(*box):
            ans.append(x[::-1])
        return ans
