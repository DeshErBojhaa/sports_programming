class Solution:
    def checkValidCuts(self, n: int, rr: List[List[int]]) -> bool:
        def segments(seg):
            ll, mv, stack, cnt = [], -1, [], 0
            for s, e in seg:
                mv = max(mv, e)
                ll.append([s, 's'])
                ll.append([e, 'e'])
            ll.sort()

            for v, t in ll:
                if t == 's':
                    stack.append(v)
                    continue
                stack.pop()
                if not stack and v < mv:
                    cnt += 1
                if cnt == 2:
                    return True
            return False
        
        hor, ver = [], []
        for a, b, c, d in rr:
            hor.append([a, c])
            ver.append([b, d])
        if segments(hor):
            return True
        if segments(ver):
            return True
        
        return False
            
