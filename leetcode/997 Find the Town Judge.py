from collections import Counter
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge_candidate = set(range(1, N+1))
        indeg = Counter()
        
        for f, t in trust:
            indeg[t] += 1
            judge_candidate.discard(f)
        
        if not judge_candidate or len(judge_candidate) > 1:
            return -1
        
        
        judge = judge_candidate.pop()
        
        if indeg[judge] != N-1:
            return -1
        return judge
