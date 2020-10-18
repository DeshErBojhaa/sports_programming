# 1405. Longest Happy String
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        vals, ans = [[a, 'a'], [b, 'b'], [c, 'c']], ['#']
        
        while vals:
            # print(vals, ans)
            ln = len(ans)
            vals.sort(reverse=True)
            if ans[-1] == vals[0][1]:
                if len(vals) == 1:
                    break
                mv = min(1, vals[1][0])
                ans.extend(vals[1][1] * mv)
                if vals[1][0] - mv > 0:
                    vals[1] = [vals[1][0] - mv, vals[1][1]]
                else:
                    vals.pop(1)
            else:
                mv = min(2, vals[0][0])
                ans.extend(vals[0][1] * mv)
                if vals[0][0] - mv > 0:
                    vals[0] = [vals[0][0] - mv, vals[0][1]]
                else:
                    vals.pop(0)
            if len(ans) == ln:
                break
        
        return ''.join(ans[1:])
            
        
