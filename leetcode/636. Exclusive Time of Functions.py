# 636. Exclusive Time of Functions
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack = [0] * n, []
        logs = [list(l.split(':')) for l in logs]
        agg_runtime = 0
        
        for id_, action, time in logs:
            id_, time = int(id_), int(time)
            if action == 'start':
                stack.append([id_, time])
                continue
            
            in_range = 0
            runtime = 0
            while stack:
                top = stack.pop()
                if len(top) == 1:
                    in_range += top[0]
                else:
                    runtime = time - top[1] + 1 - in_range
                    stack.append([time - top[1] + 1])
                    ans[id_] += runtime
                    break

        return ans
