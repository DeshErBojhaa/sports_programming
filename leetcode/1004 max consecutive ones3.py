def longestOnes(self, A: List[int], K: int) -> int:
        ans, zero_count, window = 0, 0, deque()
        
        for i, v in enumerate(A):
            if v == 1:
                window.append(1)
            if v == 0:
                while zero_count >= K and window:
                    x = window.popleft()
                    if not x:
                        zero_count -= 1
                if zero_count < K:
                    window.append(0)
                    zero_count += 1
            
            ans = max(ans, len(window))
            #print(list(window))
        return ans
        
