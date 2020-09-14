# 1585. Check If String Is Transformable With Substring Sort Operations
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False
        N = len(s)
        s = list(s)
        ind = 0
        pos = defaultdict(deque)
        
        for i, ch in enumerate(s):
            pos[ch].append(i)
        skip = [False] * N
        
        for i, ch in enumerate(t):
            while ind < N and skip[ind]:
                ind += 1
                
            if s[ind] < ch:
                return False
            next_ch = pos[ch].popleft()
            if next_ch < ind:
                return False
            skip[next_ch] = True
            
        return True
                    
